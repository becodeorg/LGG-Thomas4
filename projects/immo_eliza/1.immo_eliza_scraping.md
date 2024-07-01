# Collecting Data

- Repository: `challenge-collecting-data`
- Type of Challenge: `Consolidation`
- Duration: `5 days`
- Deadline: `28/06/2024 17:00`
- Team challenge : Team (3)

## Learning objectives

Use a Python library to collect as much data as possible.

At the end of this challenge, you should :

- Be able to scrape a website.
- Be able to build a dataset from scratch
- Be able to implement a strategy to collect as much data as possible

## The Mission

As you know the real estate company "ImmoEliza" wants to create a Machine Learning model to make price predictions on real estate sales in Belgium.

In that mission your first task is to build a dataset gathering information about at least 10.000 properties all over Belgium from [immoweb](https://www.immoweb.be/en). This dataset will be used later as a training set for your prediction model.

This dataset should be a `csv` file with the following columns:

- Locality
- Type of property (House/apartment)
- Subtype of property (Bungalow, Chalet, Mansion, ...)
- Price
- Type of sale (Exclusion of life sales)
- Number of rooms
- Living Area (m²)
- Fully equipped kitchen (Yes/No)
- Furnished (Yes/No)
- Open fire (Yes/No)
- Terrace (Yes/No)
  - If yes: Area (m²)
- Garden (Yes/No)
  - If yes: Area (m²)
- Surface of the plot (m²)
- Number of facades
- Swimming pool (Yes/No)
- State of the building (New, to be renovated, ...)

### Must-have features

- Data all over Belgium.
- Minimum 10 000 inputs without duplicates
- No empty row. If you are missing information, set the value to `None`.
- The dataset must be clean. Try as much as possible to record only numerical values.
  **Example**: Instead of defining whether the kitchen is equipped using `"Yes"`, use binary values.


### Some tips and content to support you

- You will find more content about scraping [here](../../01-TheField/02-Python/02-PythonAdvanced/05-Scraping/01-beautifulsoup-basics.ipynb)
- Think to [pandas](https://pandas.pydata.org/) for creating your dataset
- Use concurrency [here](../../01-TheField/02-Python/02-PythonAdvanced/06-Concurrency/01-concurrency.ipynb) to increase the speed of data collection
- You might have to work around CAPTCHA and other measures to slow you down. Be creative ;-)
- Another great tool for web scraping worth exploring : [scrapy](https://scrapy.org/)

## Deliverables

1. Publish your source code on a GitHub repository.
2. Pimp up the README file:
   - Description
   - Installation
   - Usage
   - (Visuals)
   - (Contributors)
   - (Timeline)
   - (Personal situation)
3. Small presentation :
   - How you did it ?
   - Who did what ?
   - What went wrong ?
   - How you solved it ?

### Steps

1. Create the repository
2. Study the request (What & Why ?)
3. Identify technical challenges (How ?)

## Evaluation criteria

| Criteria       | Indicator                                  | Yes/No |
| -------------- | ------------------------------------------ | ------ |
| 1. Is complete | Contains a minimum of 10,000 inputs.       | [ ]    |
|                | Contains data for all of Belgium.          | [ ]    |
|                | No empty row present in the dataset.       | [ ]    |
|                | Non-numeric values have been minimized.    | [ ]    |
| 2. Is great    | Used threading to speed up the collection. | [ ]    |

## A final note of encouragement

_Attempts to create thinking machines will be a great help in discovering how we think ourselves._
_- Alan Turing_

![You've got this!](https://i.giphy.com/media/JWuBH9rCO2uZuHBFpm/giphy.gif)
