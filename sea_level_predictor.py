import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10,9), dpi=120)
    ax.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'],s=15, c='r', marker='x', linewidths=0.5)

    # Create first line of best fit
    regr_CSIRO = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    slope_CSIRO = regr_CSIRO.slope
    intercept_CSIRO = regr_CSIRO.intercept
    # Create an array with the years 1880 through 2050 for x-values
    x_vals_CSIRO = np.array(list(range(1880, 2051)))
    # Create the y-values
    y_vals_CSIRO = intercept_CSIRO + slope_CSIRO * x_vals_CSIRO
    # Plot the line
    ax.plot(x_vals_CSIRO, y_vals_CSIRO)


    # Create second line of best fit
    df_later= df.loc[df['Year'] >= 2000]
    regr_later = linregress(x=df_later['Year'], y=df_later['CSIRO Adjusted Sea Level'])
    slope_later = regr_later.slope
    intercept_later = regr_later.intercept
    x_vals_later = np.array(list(range(df_later['Year'].iloc[0], 2051)))
    y_vals_later = intercept_later + slope_later * x_vals_later
    ax.plot(x_vals_later, y_vals_later)


    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()