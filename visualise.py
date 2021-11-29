import pandas
import logging
from datetime import datetime
import seaborn
import matplotlib.pyplot as plt
import geopandas

"""
Script to create a map that demonstrates the sampling intensity of the rainbow skink across the ACT. This script 
utilises pandas for data manipulation and seaborn/matplotlib for plotting.

The map is saved to result.png. The elapsed time is also tracked. 
"""

logging.basicConfig(level=logging.WARN, format="%(asctime)s %(levelname)s: %(message)s", datefmt="%Y-%m-%d  %H:%M:%S")
LOGGER = logging.getLogger(__name__)


def main():
    # Set logging level to display at the INFO level, which will include elapsed time, warnings, and errors.
    LOGGER.setLevel(logging.INFO)
    # This script will record how long it takes to complete
    start_time = datetime.now()
    LOGGER.info('Starting time: ' + str(start_time))

    # Read in the data and filter entries for the rainbow skink
    data = pandas.read_csv('data/ALA_EcoCommons_Data_Analyst_dataset.csv')
    filtered_data = data[data.scientificName.eq('Lampropholis delicata')]

    # Visualise the distribution of the observations in the dataset using a kernel density estimate (KDE)
    fig, ax = plt.subplots()
    seaborn.kdeplot(data=filtered_data,
                    x='decimalLongitude',
                    y='decimalLatitude',
                    fill=True,
                    cmap='Greens',
                    vmin=0,
                    vmax=25,
                    n_levels=11,
                    cbar_kws={'ticks': []},  # This removes the default labels from the colorbar
                    cbar=True,
                    ax=ax,
                    clip=((148, 149.5), (-35, -36)))  # Clip to only plot the ACT
    # Set the position and size of the colorbar.
    colorbar = fig.axes[1]  # Using kdeplot() makes it difficult to access the colorbar, so fetch it from the axes.
    colorbar.set_position([0.75, 0.3, 0.1, 0.4])
    # Create labels for the colorbar.
    plt.text(1.07, 0.72, 'High', transform=ax.transAxes)
    plt.text(1.07, 0.26, 'Low', transform=ax.transAxes)

    # Read in the shapefile and plot the border of the ACT to give some context to the map
    shires = geopandas.read_file('shapefiles/gadm36_AUS_1.shp')
    shires = shires[shires['NAME_1'] == 'Australian Capital Territory']
    shires.plot(color='None', edgecolor='black', ax=ax)

    # This removes the black border and axes from the plot.
    plt.axis('off')

    # Adds the title
    plt.title('Sampling Intensity of the Rainbow Skink in ACT')

    # Save the result to file
    plt.savefig('result.png', dpi=100, bbox_inches='tight')

    # Record how long the script took
    end_time = datetime.now()
    LOGGER.info('End time: ' + str(end_time))
    elapsed_time = end_time - start_time
    LOGGER.info('Elapsed time: ' + str(elapsed_time))


if __name__ == '__main__':
    main()
