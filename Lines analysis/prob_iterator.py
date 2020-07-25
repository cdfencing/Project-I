#DataFrame should have the format of L_data
def prob_iterator(df):
    #intialize line_names
    line_names = ['Red', 'Blue', 'Green', 'Brown',  'Purple', 'Purple Express', 'Yellow', 'Pink', 'Orange' ]
    
    #Set agg method
    agg_method={'rides':'sum'}
    for line in line_names:
        key = line+'_frac'
        agg_method[key] = 'sum'
        
    #Set renaming 
    rename_dict ={}

    for line in line_names:
        key = line + '_frac'
        rename_dict[key] = line +'_weight'
        

    #aggregate line data by day
    df_agg = df.groupby('date').agg(agg_method)[[line + '_frac' for line in line_names]].reset_index().rename(columns = rename_dict)
    
    #merge df with df_agg
    df_merged = df.merge(df_agg, on = 'date', how= 'left')
    
    #set weight to 0 if the line does not pass through the station
    for line in line_names:
        df_merged[line+'_weight'] = df_merged[line].astype(int) * df_merged[line+'_weight']
    
    #compute the normalization constant for each station
    df_merged['normalization'] = df_merged[[line+'_weight' for line in line_names]].sum(axis=1)
    
    #update the probabilities for each line at each station and compute the fraction of rides for each line
    for line in line_names:
        df_merged[line+'_frac'] = (df_merged[line+'_weight'] / df_merged['normalization']) * df_merged['rides']
        
    #clean up columns so that it returns a dataframe with the same columns as the original 
    df_final = df_merged.drop([line+'_weight' for line in line_names], axis =1)

    return df_final