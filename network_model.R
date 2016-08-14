install.packages("rstan")
install.packages("igraph")
library(rstan)
library(igraph)

# Read the csv file and assign all the variables
units <- read.delim("sample.csv", header=FALSE)
View(units)
J <- nrow (units)
y <- units$V5
sigma <- units$V6

# Gibbs sampler

# Conditional distributions
theta_update <- function (){
  theta_hat <- (mu/tau^2 + y/sigma^2)/(1/tau^2 + 1/sigma^2)
  V_theta <- 1/(1/tau^2 + 1/sigma^2)
  rnorm (J, theta_hat, sqrt(V_theta))
}
mu_update <- function (){
  rnorm (1, mean(theta), tau/sqrt(J))
}
tau_update <- function (){
  sqrt(sum((theta-mu)^2)/rchisq(1,J-1))
}

# Iteratively sample and build chains
chains <- 5
iter <- 1000
sims <- array (NA, c(iter, chains, J+2))
dimnames (sims) <- list (NULL, NULL,
                         c (paste ("theta[", 1:6290, "]", sep=""), "mu", "tau"))
for (m in 1:chains){
  mu <- rnorm (1, mean(y), sd(y))
  tau <- runif (1, 0, sd(y))
  for (t in 1:iter){
    theta <- theta_update ()
    mu <- mu_update ()
    tau <- tau_update ()
    sims[t,m,] <- c (theta, mu, tau)
  }
}

#monitor (sims)

# Write the thetas back to the csv file to create the network model
units$V7 = theta
write.csv(units, file = 'units_2.csv')

# Network Model

fradj = read.csv("matrix.csv", header=FALSE)
View(fradj)
colnames(fradj) = 1:442

fradj1 = matrix(unlist(fradj), ncol = 442, byrow = TRUE)

frnet = graph.adjacency(fradj1)

#plot(frnet)

evcent(frnet)