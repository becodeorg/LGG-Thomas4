# Football Match Prediction Project (Belgian Jupiler Pro League)

- Repository: `football-prediction`
- Type of Challenge: `Consolidation`
- Duration: `8 days`
- Deadline: `13/09/2024 5PM`
- Team challenge: Team (4)

## Learning Objectives

Build an end-to-end system that predicts football match outcomes using scraping, machine learning, and data visualization.

At the end of this challenge, you should:

- Be able to scrape and process data from football websites.
- Be able to train a machine learning model on historical match data.
- Be able to create a Streamlit app for live data visualization and predictions.
- Be able to manage the entire data pipeline using Airflow for automation.

## The Mission

Your mission is to build a prediction system for the Belgian Jupiler Pro League football matches. You'll combine historical match data with scraped real-time data (odds, recent matches) to predict the outcome of upcoming games.

This project will be split into two parts:
1. **Data Engineering**: Scraping and scheduling tasks using Airflow, and managing the data pipeline.
2. **Data Analysis**: Training a prediction model, building a Streamlit app, and exploring additional model improvements.

### Dataset

A CSV containing match results from the past 5 years will be provided it comes from [this website](https://www.football-data.co.uk/) (thank you Rıdvan <3), with the following key columns:

- Date = Match Date (dd/mm/yy)
- Time = Match Kick-off Time
- HomeTeam = Home Team
- AwayTeam = Away Team
- FTHG = Full Time Home Team Goals
- FTAG = Full Time Away Team Goals
- FTR = Full Time Result (H=Home Win, D=Draw, A=Away Win)

Additional statistics are included (shots, fouls, cards, etc.), which you can use to train your model. There also are historical odds given for each matches, the definitions of all columns is given [here](https://www.football-data.co.uk/notes.txt).

This dataset will help out the Data Engineers in figuring out what the Data Analysts want. It will also help out the Data Analysts in trying to train a model and showing stuff on streamlit. Consider it the bridge in the team

### Must-have features

- **Streamlit Dashboard**:
  - Display upcoming 3 matches and predicted outcomes using a machine learning model.
  - Show outcome odds for the upcoming matches.
  - Display stats for each team over the last 5 matches (goals, shots, etc.).

- **Web Scraping and Database**:
  - Historical match data should be stored in a database.
  - Build a scraper to fetch recent match data and betting odds.
  - Automate scraping using Airflow to update the database periodically.
  - Use SQLite or any free hosting service (e.g., Heroku Postgres, ElephantSQL).

- **Model Training and Scheduling Retraining**:
  - Train a machine learning model on historical match data to predict the outcome of future matches.
  - Periodically retrain the model with recent match data and updated statistics.

### Nice-to-have features

- **Automated Betting Simulation**:
  - Simulate betting 1 virtual euro per game day using model predictions.
  - Track the betting performance over one month and compare the results.

- **Model Exploration**:
  - Investigate adding additional features (e.g., possession stats, player absences) to improve model accuracy.

### Some tips and content to support you

- **Hosting database**: 
  - [Heroku Postgres](https://www.heroku.com/postgres)
  - [ElephantSQL](https://www.elephantsql.com/)
  - [SummaryOfOptions](https://gist.github.com/bmaupin/0ce79806467804fdbbf8761970511b8c) (thank you Loic <3)

- **Bookmaker odds**: Scrape odds from the following sources:
  - [WhoScored](https://www.whoscored.com/)
  - [SportsGambler](https://www.sportsgambler.com/)
  - [OddsChecker](https://www.oddschecker.com/)
  - [BetFirst](https://betfirst.dhnet.be/)

## Deliverables

1. **GitHub Repository**:
   - Publish your code on GitHub.
   - Include a README with:
     - Project description
     - Installation steps
     - Usage instructions
     - (Optional visuals)
     - (Contributors)
     - (Timeline)
     - (Challenges and solutions)

2. **Streamlit App**:
   - A dashboard displaying match predictions, team stats, and upcoming matches with odds.

3. **Presentation**:
   - How did you approach the problem?
   - Who did what in the team?
   - What were the challenges and how did you solve them?

### Steps

1. **Set up repository** and study the project requirements.
2. **Split the work**:
   - Build a web scraper. - DE
   - Set up the database. - DE
   - Train your prediction model using historical data. - DA
   - Build and deploy the dashboard. - DA
   - Automate scraping and model updates using Airflow. - DE

## A final note of encouragement

_"Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful."_
\- Albert Schweitzer

![You've got this!](https://i.giphy.com/media/JWuBH9rCO2uZuHBFpm/giphy.gif)
