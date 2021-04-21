"Pritam Basnet"
"DA 401"
"Dr. Anthony Bonifonte"

library(readr)
library(ggplot2)
library(dplyr)
library(ggfortify)
library(caret)
library(plotly)
library(ggplot2)
library(knitr)
library(broom)
library(sjPlot)
library(data.table)

# DATA READING, CLEANING AND ADDING VARIABLES

data <- read_csv('/home/basnet_p1/DA401/FinalDataForDraft.csv')

filteredData <- data %>% filter(data$`+14`>-1)

filteredData1 <- filteredData %>% select(-c("Total Awards Received"))

names <- c("Unnamed: 0","Symbol","Stock","Post Flair","Score","Upvote ratio",
           "Number of Comments","Post Date", "Post Id","Posted by","Total Awards Received","Date","Present Day",
           "-1" ,"+1","-2","+2","-3" ,"+3","-4","+4", "-5","+5" ,"-6","+6","-7" ,"+7","-8" ,"+8","-9",
           "+9","-10" ,"+10","-11","+11","-12","+12","-13","+13","-14","+14")

filteredData1 <- setnames(filteredData1,names)

filteredData1 <- filteredData1 %>% 
  filter(filteredData1$`-14`< 5 | filteredData1$`+14` < 5 | filteredData1$`Present Day` < 5)

  
filteredData["DifferenceFourteen"] = filteredData$`+14`-filteredData$`-14`
filteredData["DifferenceSeven"] = filteredData$`+7`-filteredData$`-7`
filteredData["Difference1to14"] = filteredData$`+14`-filteredData$`-1`
filteredData["Difference1to7"] = filteredData$`+7`-filteredData$`-1`
filteredData["Difference1to1"] = filteredData$`+2`-filteredData$`-1`
filteredData["Difference-7to1"] = filteredData$`+2` - filteredData$`-7`
filteredData["DD"] = ifelse(filteredData$`Post Flair`== "DD" | filteredData$`Post Flair`=="DD :DD:", 1, 0)
filteredData["Catalyst"] = ifelse(filteredData$`Post Flair`== "Catalyst" | filteredData$`Post Flair`=="Catalyst :Bagger:", 1, 0)
filteredData["Bullish"] = ifelse(filteredData$`Post Flair`== "Bullish :Bullish:", 1, 0)
filteredData["Technical Analysis"] = ifelse(filteredData$`Post Flair`== "technical analysis" | filteredData$`Post Flair`=="Technical Analysis", 1, 0)
filteredData["Megathread"] = ifelse(filteredData$`Post Flair`== "Megathread", 1, 0)

filteredData["IncreasedSeven"]= ifelse(filteredData$DifferenceSeven > 0, 1, 0)
filteredData["IncreasedFourteen"]= ifelse(filteredData$DifferenceFourteen > 0, 1, 0)
filteredData["Increased1to7"] = ifelse(filteredData$Difference1to7 > 0, 1, 0)
filteredData["Increased1to14"] = ifelse(filteredData$Difference1to14 > 0, 1, 0)
filteredData["Increased1to1"] = ifelse(filteredData$Difference1to1 > 0, 1, 0)
filteredData["CommentsMorethan20"] = ifelse(filteredData$`Number of Comments`>20, 1, 0)
filteredData["UpvoteMorethan.6"] = ifelse(filteredData$`Upvote ratio` > 0.6, 1, 0)

# Calculating percentage change
check <- filteredData %>% filter(filteredData$`-1` == 0)
filteredData <- filteredData %>% filter(filteredData$`-1` != 0)
filteredData["1to1percentage"] = filteredData$Difference1to1/filteredData$`-1`
filteredData["1to7percentage"] = filteredData$Difference1to7/filteredData$`-1`

mean(filteredData$`Number of Comments`)
mean(filteredData$`1to7percentage`)
mean(filteredData$`1to1percentage`)
mean(filteredData$`Upvote ratio`)

nrow(filteredData[filteredData$Megathread == 1, ])/nrow(filteredData)

#Getting the training and test data
## 80% of the sample size
smp_size <- floor(0.8 * nrow(filteredData))

## set the seed to make your partition reproducible
set.seed(123)
train_ind <- sample(seq_len(nrow(filteredData)), size = smp_size)

trainingData <- filteredData[train_ind, ]
testData <- filteredData[-train_ind, ]

mean(trainingData$Score)

# Making the first linear regression model

lmDiff <- lm(`Difference1to7` ~ `Number of Comments`+ `Total Awards Received` + 
               `Upvote ratio` + DD + Catalyst + Bullish + 
               Megathread + `Technical Analysis`, 
             data = trainingData)
summary(lmDiff)

# Making the first logisitic regression model

logModel <- glm(Increased1to7 ~ DD + Catalyst + Bullish + 
                   Megathread + CommentsMorethan20 + UpvoteMorethan.6,
                family=binomial, data=trainingData)

summary(logModel)


# Making the scatterplot with the trendline

max(trainingData$`Number of Comments`)
min(trainingData$Difference1to1)
max(trainingData$Difference1to1)

ddPost <- filteredData %>% filter(DD == 1)

plot1 <- ggplot(filteredData, aes(x = Score, y = `Difference1to7`)) +
  geom_point(alpha = 0.3) + geom_smooth(method=lm , color="red") + 
  xlab("The total Score of the post") + ylab("Difference in price on 7th day and the day before the post") +
  ggtitle("Effect of total score of posts on the price movement")
 

ggsave(filename="score1.png", plot=plot1+ xlim(0, 70) + ylim(-5, 10), device="png", path='/home/basnet_p1/DA401/', dpi =500)









subset1 <- data





# 



