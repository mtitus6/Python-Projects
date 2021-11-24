import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig,ax = plt.subplots(1)
    df.plot(x='Year', y="CSIRO Adjusted Sea Level", ax=ax, kind="scatter")

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    year=np.arange(1880,2051)
    x = pd.Series(year)
    line = [round(res.slope*n + res.intercept,7) for n in year]
    plt.plot(year, line, label="Fitted Line", color='red',linewidth=1)

    # Create second line of best fit
    res = linregress(df.loc[df['Year']>=2000,'Year'], df.loc[df['Year']>=2000,'CSIRO Adjusted Sea Level'])
    year=np.arange(2000,2051)
    x = pd.Series(year)
    line2 = [round(res.slope*n + res.intercept,7) for n in year]
    plt.plot(year, line2, label="Fitted Line 2", color='orange',linewidth=1)

    # Add labels and title
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()