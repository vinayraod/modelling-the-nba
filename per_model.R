#scores <- read.csv("/run/media/vinay/01CDE15DC7F9FDF0/Vinay/Study/4th year/Major Project/data/fin/1996_Scores.csv")
scores <- read.csv("D:/Vinay/Study/4th year/Major Project/data/fin/2012_Scores.csv")

#View(scores)

model = lm(scores$W.L ~ log(scores$score))

#summary(model)

plot(log(scores$score), scores$W.L, main = 'Correlation between Team PER and Win Ratio (Season 2011-12)',xlab = 'Team PER', ylab = 'Win Ratio (% Wins/Total Games Played * 100)', col='blue', pch=19, cex = 1, lty = "solid", lwd = 2)

text(log(scores$score), scores$W.L, labels = scores$Tm, cex=0.7, pos=3)
abline(model, col='red')
legend("topleft", bty="n", legend=paste("Adjusted R-squared = ",format(summary(model)$adj.r.squared, digits=4)))