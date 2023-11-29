"""Recommender system with content-based filtering."""

import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, MinMaxScaler


def build_user_item_networks(layer_units):
    """Creates two neural networks with the same architecture for users and items.

    Args:
        layer_units (list): A list of numbers of units per hidden layer (and output layer).

    Returns:
        tuple: The neural networks for users and items.
    """
    user_NN = tf.keras.models.Sequential()
    item_NN = tf.keras.models.Sequential()

    num_layers = len(layer_units)

    for i in range(num_layers):
        num_units = layer_units[i]

        if i != num_layers - 1: # relu for all middle layers
            user_NN.add(tf.keras.layers.Dense(num_units, activation="relu"))
            item_NN.add(tf.keras.layers.Dense(num_units, activation="relu"))
        else: # linear for last layer
            user_NN.add(tf.keras.layers.Dense(num_units))
            item_NN.add(tf.keras.layers.Dense(num_units))

    return user_NN, item_NN


def build_model(user_NN, item_NN, num_user_features, num_item_features):
    """Builds a network of neural networks that takes user and item inputs and outputs a prediction.

    Args:
        user_NN (tf.keras.models.Sequential): The user neural network.
        item_NN (tf.keras.models.Sequential): The item neural network.
        num_user_features (int): Number of user features.
        num_item_features (int): Number of item features.

    Returns:
        tf.keras.Model: The model consisting of two neural networks and a dot product output.
    """
    user_input = tf.keras.layers.Input(num_user_features)
    vu = user_NN(user_input)
    vu = tf.linalg.l2_normalize(vu, axis=1)

    item_input = tf.keras.layers.Input(num_item_features)
    vr = item_NN(item_input)
    vr = tf.linalg.l2_normalize(vr, axis=1)

    # Output: dot product of computed user and item vectors
    output = tf.keras.layers.Dot(axes=1)([vu, vr])

    # Model: run user and item inputs through their NNs, then take dot product
    model = tf.keras.Model([user_input, item_input], output)
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
        loss=tf.keras.losses.MeanSquaredError()
    )

    return model


def scale_data(data, scaler_type):
    """Scales data using a scaler type.

    Args:
        data (np.ndarray): Matrix of data to scale.
        scaler_type (str: 'standard' or 'minmax'): The type of scaler to use.

    Raises:
        Exception: If an invalid scaler type is given.

    Returns:
        tuple: The scaled data and its scaler object.
    """
    if scaler_type == "standard":
        data_scaler = StandardScaler()
    elif scaler_type == "minmax":
        data_scaler = MinMaxScaler()
    else:
        raise Exception("Invalid scaler type (must be 'standard' or 'minmax')")

    data_scaler.fit(data)
    data = data_scaler.transform(data)
    return data, data_scaler


def predict_ratings(model, user_test, item_test, y_scaler):
    """Predicts user ratings for items.

    Args:
        model (tf.keras.Model): Model of two chained neural networks with a dot product as the result.
        user_test (np.ndarray): Matrix of test users.
        item_test (np.ndarray): Matrix of test items.
        y_scaler (sklearn.preprocessing.MinMaxScaler): Scaler for rating data.

    Returns:
        np.ndarray: Vector of predictions for users on items.
    """
    scaled_y_pred = model.predict([user_test, item_test])

    # Rescale output
    rescaled = y_scaler.inverse_transform(scaled_y_pred)

    return np.array([x[0] for x in rescaled])
