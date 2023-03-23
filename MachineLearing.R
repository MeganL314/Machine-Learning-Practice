install.packages("caret", dependencies = c("Depends", "Suggests"))
library(caret)

#https://topepo.github.io/caret/
#https://cran.r-project.org/web/packages/caret/vignettes/caret.html


install.packages('rlang')
install.packages('caret')
# load in packages
library(caret)
library(ranger)
library(tidyverse)
library(e1071)

#https://topepo.github.io/caret/
#https://cran.r-project.org/web/packages/caret/vignettes/caret.html

# Preprocess tools
## preProcess 

# Data splitting
## createDataPartition
## createResample
## createTimeSlices

# Training/testing function
## train 
## predict

# Model comparison
## confusionMatrix

library(caret); library(kernlab); data(spam)
inTrain <- createDataPartition(y=spam$type, p=0.75,
                               list=FALSE)  #75% to train and 25% to test
training <- spam[inTrain,] #in training set
testing <- spam[-inTrain,] #in test set
dim(training)

set.seed(4292)
folds <- createFolds(y=spam$type, k=10, list=TRUE, 
		     returnTrain=TRUE) #pass outcome to split on (type) and number of folds (10)


folds[[1]][1:10]
tme <- 1:1000
folds <- createTimeSlice(y=tme, initialWindow=20, horizon=10)
folds$train[[1]]
folds$test[[1]]

set.seed(1112)
modelFit <- train(type ~.,data=training, method='glm')
modelFit$finalModel

predictions <- predict(modelFit, newdata=testing)
predictions

confusionMatrix(predictions, testing$type)




 
