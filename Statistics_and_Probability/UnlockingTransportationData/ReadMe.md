# Analysis Transportation Data
![image](https://github.com/MohidulHaqueTushar/Skills-Based-Projects/blob/main/Statistics_and_Probability/UnlockingTransportationData/Data/baseball_flights.png)

## Project Overview

This project explores transportation time series data analysis to uncover patterns and forecast travel costs. The focus is on unlocking the value of transportation data, with a particular emphasis on scheduling challenges and optimizing travel for professional sports teams.

## Project Description

Embark on a data-driven journey into the world of transportation time series analysis, specifically targeting the dynamic scheduling problems faced by professional sports leagues. The project explores flight patterns and employs forecasting techniques to estimate travel costs. The insights gained aim to optimize flight schedules and predict fuel expenditures for the upcoming season.

## Project Instructions

To assist **The League** in optimizing flight schedules, the following tasks have been carried out:

1. **Jet Fleet Optimization:**
   - Analyze flight schedules to determine the maximum number of jets **The League** should own.
   - Create a time series graph displaying the number of teams “in flight” throughout the 2102 season.
   - Identify the maximum number of teams simultaneously in flight.
   - Store the result in the variable `max_teams_in_flight`.

2. **Fuel Cost Projection:**
   - Utilize 2101's jet fuel prices to project prices for 2102.
   - Apply these projections to all flights scheduled for the 2102 season to estimate the overall fuel costs.
   - Store the total projected fuel expense in the variable `total_fuel_spend_2102_dollars`.

This analysis provides actionable insights for **The League** to manage resources efficiently and minimize operational costs in the upcoming season.

## Project Approach

### 1. Visualize the Number of Teams Simultaneously Flying
- **Objective:** Determine how many teams are in-flight at the same time throughout the season.
- **Steps:**
  - Concatenate the `departure_datetime` and `landing_datetime` into a single sorted array for visualization.
  - Create a table with two columns: `datetime` and `number_in_air` to track how many teams are in the air at any given time.
  - Sort the datetimes chronologically, ensuring proper visualization, such as using a line graph.
  - Iterate through each flight to check if it was mid-air at a specific time and increment the `number_in_air` accordingly.

- **Visualization:** Use a line or scatter plot to visualize the trends and identify the maximum number of teams in flight.

### 2. Project Next Year’s Fuel Spend
- **Objective:** Estimate fuel costs for the 2102 season using a SARIMAX model for fuel price forecasting.
- **Steps:**
  - Use SARIMAX with parameters `order = (1, 1, 1)` for linear growth and `seasonal_order = (1, 0, 0, 7)` for weekly seasonality to forecast fuel prices for 2102.
  - Create a DataFrame for future dates and join it with the forecasted fuel prices.
  - Match forecasted fuel prices to flight data based on departure date and ensure date formats are compatible.
  - Compute fuel costs per flight by multiplying fuel prices with the flight distance.
  - Sum the costs to determine the total fuel expenditure for the 2102 season.
