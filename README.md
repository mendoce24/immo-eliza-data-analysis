# Immo Eliza - Data Analysis

A solo project @ [BeCode.org](https://becode.org/) as part of the **AI Bootcamp** in Gent

## Project description

This is a project to create a Machine Learning (ML) model to predict sell prices of real estate properties in Belgium.

The previous task was to clean the data (at least 19,000 entries) of the Belgian real estate market. These data was used to display graphs and do model analysis.

The current task is to make the analysis and exploration of the date to build a model to predict de sell price of the properties.

The dataset used a `csv` file scraped from [ImmoWeb](https://www.immoweb.be/en) website, which was provided from the  [ImmoEliza-DataScraper](https://github.com/vitaly-shalem/ImmoEliza-DataScraper) project.

## Installation

1. Clone [Immo Eliza Data Analysis](https://github.com/mendoce24/immo-eliza-data-analysis) repository
2. Change directory to the root of the repository
3. Install required libraries by running `pip install -r requirements.txt`

## Usage
### Data Exploration
- Within Jupyter Notebook  `immo_eliza_data_analysis.ipynb` you will be able to navigate and consult differents graphs.
- The following graphics were generated with Plotly, as part of the analysis of the data provided.
![Map Belgium](output/map.png)
![Amount Properties](output/Plot_amount_properties_per_district.png)
![Price District](output/Plot_mean_price_per_district.png)

### Model Building
- Within Jupyter Notebook  `immo_eliza_data_exploration.ipynb` you will be able to navigate and consult differents graphs and methos to clean the data and prepared to be usefull to the model, in this version we used only numerical data.
- Within Jupyter Notebook  `immo_eliza_data_exploration_categorical.ipynb` you will be able to navigate and consult differents graphs and methos to clean the data and prepared to be usefull to the model, in this version we used also the categorical data to used in the model.
- To perform the model prediction we used four different models to find the best way to obtain the maximum prediction score.
When carrying out the model with the different regression methods we can obtain better results with Random Forest Regressor.

- Linear Regression `immo_eliza_data_building.ipynb`
  
![Linear Regression](output/linear_r.png)

- XGB Regressor `immo_eliza_data_building_XGBBoost.ipynb`
  
![XGB Regressor](output/XG_boots.png)

- Tree Regressor `immo_eliza_data_building_tree.ipynb`
  
![Tree Regressor](output/tree_decision.png)

- Random Forest Regressor `immo_eliza_data_building_tree.ipynb`
  
![Random Forest Regressor](output/random_forest.png)

## Timeline

Second stage of the project lasted 4 days in the week of July 17-20, 2023.
First stage of the project lasted 5 days in the week of July 05-11, 2023.

## The Team

The stage was made by:

- César E. Mendoza V. [LinkedIn](https://www.linkedin.com/in/mendoce24/) | [GitHub](https://github.com/mendoce24)

## Instruction

The stage was made under the supervision of [Vanessa Rivera Quiñones](https://www.linkedin.com/in/vriveraq/) and [Samuel Borms](https://www.linkedin.com/in/sam-borms/?originalSubdomain=be)

Gent | July 20, 2023
