# Heartbeat Analysis Project

## Overview

This project focuses on heartbeat analysis, including preloaded models, logistic regression for heart disease prediction, and visualization using Streamlit.

## Dataset Organization

The datasets required for this project are included in the `datasets` directory. Organize the data as instructed in `modelbuilding.py`.
Heart Beat analysis from the given dataset. Labelling it through built rnn model Load the dataset with correct path from the following link

      http://www.peterjbentley.com/heartchallenge/ 
      
InpatientCharges.csv can be downloaded for heartpatients: 
          https://drive.google.com/file/d/1Yamomu-PMajHLvdtNjP4hz4FrhgVJSgV/view?usp=sharing

## Model Building

The script `modelbuilding.py` provides instructions for organizing the dataset and building models. Follow the guidelines to structure the data properly for model training.

### Preloaded Model

A preloaded model is stored in `Modelrnn/Best_model_trained.hdf5`. This model can be used for analysis.

### Database Usage

If needed, utilize `Modelrnn/mysqcon.py` to store datasets in a database. Modify the script based on your database configuration.

## Logistic Regression

The file `heart.csv` contains data for logistic regression for heart disease prediction. Use this dataset to build a logistic regression model.

## Hospital Statistics

The number of heart patients in a hospital is available in `inpatients.csv`.

## Running the Application

Execute the `Home.py` script to run the application. This script will launch a Streamlit application.

### Streamlit Pages

The Streamlit pages are organized in the `pages` folder. There are 6 pages that follow the `Home.py` execution.

### Images and HTML Pages

Necessary images for the application are stored in the `images` folder. An HTML page for plots can be found in the `htmlpage` directory.

## Project Structure

- `datasets/`: 
- `Modelrnn/`: Includes preloaded models and database connectivity script.
- `modelbuilding.py`: Provides instructions for organizing the dataset and building models.
- `heart.csv`: Dataset for logistic regression.
- `inpatients.csv`: Hospital statistics dataset.
- `Home.py`: Main script to run the Streamlit application.
- `pages/`: Streamlit pages.
- `images/`: Images for the application.
- `htmlpage/`: HTML page for plots.

## Usage

1. Organize datasets as per instructions in `modelbuilding.py`.
2. Train models using the provided scripts.
3. Run `Home.py` to launch the Streamlit application.

## Contributing

Contributions are welcome! Fork the repository, make your changes, and submit pull requests.

