import pandas
import logging
from datetime import datetime
import seaborn
import matplotlib.pyplot as plt
import geopandas

logging.basicConfig(level=logging.WARN, format="%(asctime)s %(levelname)s: %(message)s", datefmt="%Y-%m-%d  %H:%M:%S")
LOGGER = logging.getLogger(__name__)


def main():
    # Set logging level to display at the INFO level, which will include elapsed time, warnings, and errors.
    LOGGER.setLevel(logging.INFO)
    # This script will record how long it takes to complete
    start_time = datetime.now()
    LOGGER.info('Starting time: ' + str(start_time))

    data = pandas.read_csv('data/ALA_EcoCommons_Data_Analyst_dataset.csv')
    filtered_data = data[data.scientificName.eq('Delma impar')]
    fig, ax = plt.subplots()

    shires = geopandas.read_file('shapefiles/gadm36_AUS_1.shp')
    shires = shires[shires['NAME_1'] == 'Australian Capital Territory']
    shires.plot(color='white', edgecolor='black', ax=ax)
    seaborn.kdeplot(data=filtered_data,
                    x='decimalLongitude',
                    y='decimalLatitude',
                    fill=True,
                    cmap='Greens',
                    alpha=0.5,
                    gridsize=200,
                    levels=5,
                    ax=ax)
    plt.show()

    # Record how long the script took
    end_time = datetime.now()
    LOGGER.info('End time: ' + str(end_time))
    elapsed_time = end_time - start_time
    LOGGER.info('Elapsed time: ' + str(elapsed_time))


if __name__ == '__main__':
    main()
