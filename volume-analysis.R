library("lme4")        
#library("afex")        
#library("broom.mixed") 
#library("tidyverse")
#library("grid")
#library("coefplot")
#library("nlme")
library(dplyr)
library("ggplot2")
data <- read.csv("seg_vol.csv")
data$Session <- factor(recode(data$Session, "1" = "ses-1", "2" = "ses-2", "3" = "ses-3", "4" = "ses-4"))

zmargin <- theme(panel.margin=unit(0,"lines"))
ggplot(data,aes(Session,Total))+
  geom_point()+ geom_line(aes(group=Subject))+ facet_grid(.~Group)+ zmargin

ggplot(data = data, aes(x = Session, y = Total, group = Subject, color = Group)) + geom_line() +
  facet_wrap(~Subject)

mod_sim <- lmer(Total ~ Group*Session + (1 | Subject), data = data, REML = FALSE)
summary(mod_sim, corr = FALSE)