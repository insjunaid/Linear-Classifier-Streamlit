# Linear Classifier Streamlit Project

Welcome to the **Linear Classifier Streamlit Project**, a machine learning application designed to classify fish species (Blue Fish and Orange Fish) based on water depth and temperature data. This project was developed as part of a learning exercise to implement a logistic regression model and deploy it using Streamlit, with data visualization capabilities.

![{9962440B-F852-46BA-8DAD-C48A97087AA7}](https://github.com/user-attachments/assets/1c08a7bf-5e4a-4998-a9bb-ea81a4b2d810)

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

## The Story of the dataset
Imagine a small coastal town called Seaview, known for its vibrant marine life and bustling fishing community. The town has two types of fish that are particularly important to the local ecosystem and economy: the Bluefin Snapper (represented by blue dots) and the Orangetail Grouper (represented by orange dots). Marine biologists in Seaview are studying these fish to understand their habitats better and ensure sustainable fishing practices.

The scatter plot you see is part of their research. The x-axis (feature1) represents the water depth (in meters) where the fish are typically found, scaled to a range for analysis. Negative values indicate shallower waters closer to the shore, while positive values represent deeper waters further out in the ocean. The y-axis (feature2) represents the water temperature (also scaled), with lower values indicating colder waters and higher values indicating warmer waters.

The biologists collected data on hundreds of fish, marking each one as either a Bluefin Snapper (target 0, blue) or an Orangetail Grouper (target 1, orange). Their goal was to see if they could predict the type of fish based on depth and temperature alone—potentially helping fishermen target specific species more efficiently.

However, the plot tells a complicated story. The Bluefin Snappers tend to prefer slightly shallower and colder waters (more blue dots on the left and lower parts of the plot), while the Orangetail Groupers are often found in deeper and warmer waters (more orange dots on the right and upper parts). But there’s a problem: there’s a lot of overlap! In the middle of the plot—around average depths and temperatures—both fish species are found together, making it hard to tell them apart just by these two measurements.

This overlap suggests that depth and temperature alone aren’t enough to distinguish between the two species. Maybe other factors, like salinity, ocean currents, or the type of food available in those waters, play a role in where these fish live. The biologists might need to collect more data or use a more sophisticated model to predict the fish species accurately.

For the fishermen of Seaview, this means they can’t rely on a simple rule like “fish in deep, warm waters for Orangetail Groupers.” They’ll need to work closely with the biologists to find better ways to identify the fish—or perhaps adjust their fishing practices to avoid catching too many of the wrong species. In the meantime, this scatter plot is a reminder of the complexity of nature, where even two seemingly straightforward measurements can reveal a tangled web of life beneath the waves.

![{D1E35659-4F1D-4119-ABC1-7366256FF599}](https://github.com/user-attachments/assets/2f18fed5-3096-41b6-83f1-1bdc37f9c669)
![{933BF7B1-D124-401D-9181-D6071DBD5E81}](https://github.com/user-attachments/assets/985d51cb-936c-4d91-a9b6-185703ee1cfc)





