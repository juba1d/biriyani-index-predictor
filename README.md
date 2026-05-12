# Biryani Index Predictor 🍛

A specialized time-series project predicting the price of a plate of Kacchi in Dhaka using Exogenous Economic Factors.

## Why this exists?
Standard inflation models are boring. The **Biryani Index** is a real-world reflection of supply-chain pressure (rice/mutton) and cultural seasonality (Shukrobar spikes and Eid festivities).

## Tech Stack
* **Simulation:** Procedural data generation for market modeling.
* **Forecasting:** `skforecast` + `scikit-learn`.
* **Complexity:** Handles **Multi-variate forecasting** (Price + Festival labels).

## How to use
1. `python src/generator.py` - Creates the simulated bazaar data.
2. `python src/model.py` - Trains the forecaster.

## Foodie Insights
This project demonstrates my ability to handle **Exogenous Features**. In forecasting, knowing *when* it's a holiday is often more important than the historical price itself.
