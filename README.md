# Modelling the NBA

We've implemented 2 models for evaluating player performance.
1) PER Model
2) Network Model

1) PER Model

First, run scraper.py 
It does the following
- Parses basketball-reference.com and gets the data.
- Uses the collected data to calculate Team PER for each team.
- Calculates win ratio for every team.
Finally, use per_model.R to build linear regression models and plot graphs.

2) Network Model

Dataset was downloaded from http://www/basketballvalue.com/downloads.php
Run mean.py for each season to calculate mean of the points scored for each 5-man unit.
Run network_model.R to build a Bayesian hierarchical model and estimate the parameters using a Gibbs Sampler.
Finally, run gen_matrix.py to build the network and calculate centrality scores.
