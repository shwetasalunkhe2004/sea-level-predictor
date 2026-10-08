import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():

    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # First line of best fit
    result = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    years = range(1880, 2051)

    predicted = [
        result.slope * year + result.intercept
        for year in years
    ]

    plt.plot(
        years,
        predicted
    )

    # Second line of best fit
    df_2000 = df[df["Year"] >= 2000]

    result_2000 = linregress(
        df_2000["Year"],
        df_2000["CSIRO Adjusted Sea Level"]
    )

    years_2000 = range(2000, 2051)

    predicted_2000 = [
        result_2000.slope * year + result_2000.intercept
        for year in years_2000
    ]

    plt.plot(
        years_2000,
        predicted_2000
    )

    # Labels
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot
    plt.savefig("sea_level_plot.png")

    return plt.gca()