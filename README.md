# Linear Classifier Streamlit Project

Welcome to the **Linear Classifier Streamlit Project**, a machine learning application designed to classify fish species (Blue Fish and Orange Fish) based on water depth and temperature data. This project was developed as part of a learning exercise to implement a logistic regression model and deploy it using Streamlit, with data visualization capabilities.

## Overview

This project simulates a scenario where marine biologists and fishermen from a coastal town (inspired by the fictional Seaview) study two fish species:
- **Blue Fish** (target = 0, represented by blue dots): Prefers shallower, colder waters.
- **Orange Fish** (target = 1, represented by orange dots): Prefers deeper, warmer waters.

The application uses a synthetic dataset to predict the fish species based on two features:
- `water_depth` (scaled meters): Negative values indicate shallower waters, positive values indicate deeper waters.
- `temp` (scaled °C): Lower values indicate colder waters, higher values indicate warmer waters.

Despite some overlap in habitats, the logistic regression model provides reasonable predictions, with an accuracy typically around 85–90%.

## Features
- Train a logistic regression model on synthetic fish data.
- Interactive Streamlit app to input water depth and temperature for predictions.
- Visualization of the dataset with a scatter plot, including the decision boundary and user input point.


