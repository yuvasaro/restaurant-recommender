# Restaurant Recommender

Dataset: https://www.kaggle.com/datasets/uciml/restaurant-data-with-consumer-ratings


## Overview

This is a Restaurant Recommender System that uses content-based filtering through a neural network 
trained on user information, restaurant information, and user ratings on restaurants to provide 
restaurant recommendations for users.

`restaurant_recommender.ipynb` contains the code to train and test the recommender system.

`rec_sys.py` contains neural network and recommender system code.

`utils.py` contains utility functions for loading and manipulating the dataset.

`constants.py` contains constant lists and dictionaries used within the project.

`data` contains CSV files of the Kaggle dataset used in this project.


## Setup Instructions

1. Download the repository and `cd` into it:

    `git clone https://github.com/yuvasaro/restaurant-recommender`

    `cd restaurant-recommender`

2. Create a virtual environment:

    `python3 -m venv venv`

3. Install all required libraries:

    `pip install -r requirements.txt`

4. Run the cells one by one in `restaurant_recommender.ipynb`.


## Quick Note

This recommender system does not work nearly as well as I want it to. I am currently limited
by my own knowledge in figuring out how to better approach building this recommender system.
I know it has something to do with incorrectly using categorical data to train the neural
network. I will come back to this project later on to rework the neural network architecture
and find a good way to encode the categorical data such that the neural network can be
trained on it appropriately.
