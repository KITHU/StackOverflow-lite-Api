# StackOverflow-lite-Api

[![Build Status](https://travis-ci.org/KITHU/StackOverflow-lite-Api.svg?branch=challenge2)](https://travis-ci.org/KITHU/StackOverflow-lite-Api)
[![Coverage Status](https://coveralls.io/repos/github/KITHU/StackOverflow-lite-Api/badge.svg?branch=challenge2)](https://coveralls.io/github/KITHU/StackOverflow-lite-Api?branch=challenge2)
[![Maintainability](https://api.codeclimate.com/v1/badges/fe902cc39221400126c7/maintainability)](https://codeclimate.com/github/KITHU/StackOverflow-lite-Api/maintainability)



# Description
StackOverflow-lite is a platform where users can ask questions and post answers to questions.

# Development
- This Application is powered by Python3 Language,  Flask and flask_restplus python flameworks
  
##### heroku link
- https://stackoverflow234-lite.herokuapp.com
##### github repo link
- https://github.com/KITHU/StackOverflow-lite-Api.git

## Features
- Users can post a question                       
- Users can get all questions
- Users can get a single question with its answers
- Users can post answers to questions
### end points
Endpoints                          | features
---------------------------------- | --------------------------------
GET  api/v1/question               | returns all questions
GET  api/v1/question/id            | returns a single question
POST api/v1/question               | post a question to app
POST api/v1/question/id/answer     | post an answer to a question 

## local setup and testing using postman
1. create a python3 virtual environment 
2. clone the repo ..link given above
3. install dependances from requirements.txt
4. create a .env file and add this code
 ```  
   source env/bin/activate

   export APP_SETTINGS="development"
   export JWT_SECRET_KEY="this is secret"

```  
5. to run the app type python run.py from the console
6. to run test type pytest --cov-report term-missing --cov=app on the console

7. open postman and start testing the above endpoints

### sample body data for post, question and answer
i. answer 
```
{"answer":"your answer"}
```
ii. question 
```
{"title":"question title",
 "body":"your question content in full"}
```