library("lme4")        
#library("afex")        
#library("broom.mixed") 
#library("tidyverse")
#library("grid")
#library("coefplot")
#library("nlme")
library(dplyr)
library("ggplot2")
data <- read.csv("../derivatives/seg_vol.csv")
data$Session <- factor(recode(data$Session, "1" = "ses-1", "2" = "ses-2", "3" = "ses-3", "4" = "ses-4"))

zmargin <- theme(panel.margin=unit(0,"lines"))
ggplot(data,aes(Session,Total))+
  geom_point()+ geom_line(aes(group=Subject))+ facet_grid(.~Group)+ zmargin

ggplot(data = data, aes(x = Session, y = Total, group = Subject, color = Group)) + geom_line() +
  facet_wrap(~Subject)

mod_sim <- lmer(Total ~ Group*Session + (1 | Subject), data = data, REML = FALSE)
summary(mod_sim, corr = FALSE)

# stripchart with linked observations
p <- ggplot(data,aes(x = Session, y = Total, fill = Session, group = Subject, shape = Group)) +
  geom_line(size=0.8, alpha=1) +
  geom_point(colour = "black", size = 2, stroke = 1) +
  scale_shape_manual(values=c(22,21)) +
  scale_fill_manual(values = c("grey90", "grey60","grey30", "grey10")) +
  theme(axis.text.x = element_text(colour="grey20",size=16),
        axis.text.y = element_text(colour="grey20",size=16),  
        axis.title.x = element_blank(),
        axis.title.y = element_blank(),
        plot.title = element_text(colour="grey20",size=20),
        legend.position="none",
        # plot.margin = unit(c(150,100,5.5,5.5), "pt")
        plot.margin = unit(c(5.5,5.5,5.5,5.5), "pt"))

linkedstrip <- p + facet_grid(. ~ Group) +
  theme(strip.text.x = element_text(size = 20, colour = "white"),
        strip.background = element_rect(colour="darkgrey", fill="darkgrey"))
linkedstrip
