"""Utility functions for loading data."""

import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

from constants import *


def encode_features(df, feature_options, ignore_id=False):
    """Encodes a Pandas DataFrame using the given feature options encoding.

    Args:
        df (DataFrame): Pandas DataFrame.
        feature_options (dict): Dictionary of feature options from constants.py.
        ignore_id (bool, optional): Whether to ignore the first (ID) column. Defaults to False.

    Returns:
        pd.DataFrame: The resulting encoded DataFrame.
    """
    encoded_df = pd.DataFrame(0., index=df.index, columns=df.columns, dtype=float)

    for i, row in df.iterrows():
        indices = row.index
        if ignore_id:
            id = indices[0]
            encoded_df[id] = df[id]
            indices = indices[1:]

        for feature in indices:
            value = row[feature]
            if type(value) == str: # encode feature with list indices from constants.py
                encoded_df.at[i, feature] = feature_options[feature].index(value)
            else:
                encoded_df.at[i, feature] = value # numeric
    
    return encoded_df


def load_data():
    """Loads all user, restaurant, and rating data into matrices.

    Returns:
        tuple: User matrix, user vectors, restaurant matrix, restaurant vectors, rating matrix, num users, num restaurants.
    """
    # Sort users in lexicographical order
    user_df = pd.read_csv(
        "data/userprofile.csv", 
        index_col="userID",
        usecols=USER_FEATURES
    ).sort_index()

    # One hot encode user preferred cuisines
    # user_cuisine_df = pd.read_csv("data/usercuisine.csv", index_col="userID").sort_index()
    # user_cuisine_one_hot_df = pd.DataFrame(0, index=user_df.index, columns=USER_CUISINES)
    # for user, row in user_cuisine_df.iterrows():
    #     user_cuisine_one_hot_df.at[user, row["Rcuisine"]] = 1
    # user_df = pd.concat([user_df, user_cuisine_one_hot_df], axis=1)
    user_df = user_df.reset_index()
    user_df["userID"] = user_df["userID"].apply(lambda id: int(id[1:])) # convert id strings to ints to avoid errors

    num_users = user_df.shape[0]

    # Sort restaurants in lexicographical order
    restaurant_df = pd.read_csv(
        "data/geoplaces2.csv", 
        index_col="placeID",
        usecols=RESTAURANT_FEATURES
    ).sort_index()

    # One hot encode restaurant cuisines
    # restaurant_cuisine_df = pd.read_csv("data/chefmozcuisine.csv", index_col="placeID").sort_index()
    # restaurant_cuisine_one_hot_df = pd.DataFrame(0, index=restaurant_df.index, columns=RESTAURANT_CUISINES)
    # for restaurant, row in restaurant_cuisine_df.iterrows():
    #     if restaurant in restaurant_cuisine_one_hot_df.index:
    #         restaurant_cuisine_one_hot_df.at[restaurant, row["Rcuisine"]] = 1
    # restaurant_df = pd.concat([restaurant_df, restaurant_cuisine_one_hot_df], axis=1)
    restaurant_df = restaurant_df.reset_index()

    num_restaurants = restaurant_df.shape[0]

    ratings_df = pd.read_csv(
        "data/rating_final.csv", 
        index_col="userID",
        usecols=["userID", "placeID", "rating"]
    ).sort_index().reset_index()
    ratings_df["userID"] = ratings_df["userID"].apply(lambda id: int(id[1:])) # convert id strings to ints to avoid errors

    # Encode features in user and restaurant data
    user_df = encode_features(user_df, USER_FEATURE_OPTIONS, ignore_id=True)
    restaurant_df = encode_features(restaurant_df, RESTAURANT_FEATURE_OPTIONS, ignore_id=True)

    user_train = []
    restaurant_train = []
    y_train = []

    for _, rating_info in ratings_df.iterrows():
        # Find user and restaurant feature vectors based on lex order
        user = user_df.loc[user_df["userID"] == rating_info["userID"]]
        restaurant = restaurant_df.loc[restaurant_df["placeID"] == rating_info["placeID"]]

        user_train.append(np.array(user)[0])
        restaurant_train.append(np.array(restaurant)[0])
        y_train.append(rating_info["rating"])

    user_train = np.array(user_train)
    restaurant_train = np.array(restaurant_train)
    y_train = np.array(y_train)

    user_vectors = []
    for _, user_info in user_df.iterrows():
        user_vectors.append(np.array(user_info))
    user_vectors = np.array(user_vectors)

    restaurant_vectors = []
    for _, restaurant_info in restaurant_df.iterrows():
        restaurant_vectors.append(np.array(restaurant_info))
    restaurant_vectors = np.array(restaurant_vectors)

    return user_train, user_vectors, restaurant_train, restaurant_vectors, y_train, num_users, num_restaurants


def get_restaurant_names_cuisines(place_id_list):
    """Returns the restaurant names and cuisines for the given list of restaurant IDs.

    Args:
        place_id_list (np.ndarray): List of restaurant IDs.

    Returns:
        tuple: List of restaurant names and list of restaurant cuisines for the given IDs.
    """
    restaurant_df = pd.read_csv(
        "data/geoplaces2.csv", 
        index_col="placeID",
    )

    cuisine_df = pd.read_csv(
        "data/chefmozcuisine.csv",
        index_col="placeID"
    )

    names = []
    cuisines = []

    for id in place_id_list:
        names.append(restaurant_df.loc[id]["name"])

        try:
            cuisine_str = ""
            cuisine_loc = cuisine_df.loc[id]
            num_cuisines = len(cuisine_loc)

            if num_cuisines > 1:
                cuisine_arr = cuisine_loc["Rcuisine"]
                for i in range(num_cuisines):
                    if i != num_cuisines - 1:
                        cuisine_str += cuisine_arr[i] + ", "
                    else:
                        cuisine_str += cuisine_arr[i]
            else:
                cuisine_str += cuisine_loc["Rcuisine"]
            
            cuisines.append(cuisine_str)
        except:
            cuisines.append("?")
            continue

    return names, cuisines
