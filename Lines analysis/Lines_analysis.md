## Analysis of 'L' Ridership by line

Using open transit data from the CTA [(Data)](https://data.cityofchicago.org/Transportation/CTA-Ridership-L-Station-Entries-Daily-Totals/5neh-572f). We analyze trends in ridership on the Chicago transit system brokendown by 'L' line. We are particularly interested in changes in trends during the March 2020 to present time period.

### Approximating ridership by line

The CTA records the number of riders entering stations and the data reports these totals daily. A number of stations are served by multiple line (for example Belmont is served by the Red, Brown, and Purple line express). We thus have no a priori way of knowing how many of the riders who checked into the Belmont station took a Red line train. To circumvent this gap in the data we approximate ridership on each line. 

Our approximation is based on a iterative approach. In which we specify a distribution which describes the probability that a rider at a statin will use each line. Using this distribution we compute total ridership on each line for each day. We then use this aggregated data to update our distribution. In our analysis we intialized the procedure using a uniform distribution and took 10 iterations. We expect other choices of approximation methods to yeild similar results.

### Ridership by line 2010 - 2020

