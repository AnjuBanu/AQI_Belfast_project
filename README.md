# Air Quality Index Prediction using Machine learning model

---
### Introduction

The aim of this project is to build the Air quality index prediction model with Machine learning algorithm.
This is a simple web app model which predicts the Air quality index of a city given the Maximum Temperature, minimum Temperature, wind speed, visibility etc !


### Project version

version 1.0

### Executions
#### Functional Code:    app.py<br>


### ML model and Accuracy
The Machine learning model used is "Random forest" and The accuracy is 90%.


### Web app link
https://aqiproject.herokuapp.com/


### Tools
![img_1.png](img/img_1.png)
![img_2.png](img/img_2.png)
![img_3.png](img/img_3.png)


### Code Briefing

- Below is a simple code tree structure to give an overview of the job performed by each file generated.  
- The required data is already downloaded and placed under csvData directory.

    https://en.tutiempo.net (Independent Features)
  
    https://www.weather.com (Dependent Features)

  ````code
    
  |___ static                       <- All images required to load in html
  |___ output                       <- html files for user interface
  |___ model
  |       |___ AQI                  <- Dependent feature csv files
  |       |___ Data                 <- Independent feature csv files
  |       |___ models               <- Different Machine learning models
  |       |___ pickle               <- Pickled files of Machine learning models
  |       |___ src                  <- Code to perform feature engineering
  |___ app.py                       <- Deployment code
     
    ````



### Author
Anjum Banu Ismail
