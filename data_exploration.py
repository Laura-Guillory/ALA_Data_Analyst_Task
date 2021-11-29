import pandas

"""
Script to explore the contents of the data provided. 

Exploratory code here is kept separate from productive code so that each can be run individually as needed. Rerunning 
exploration code is not necessary when testing code in visualise.py.
"""


def main():
    # Load the data from file using pandas
    data = pandas.read_csv('data/ALA_EcoCommons_Data_Analyst_dataset.csv')

    # Quick preview of the first few records in the file
    print('Preview: \n' + str(data.head()) + '\n')

    # List the columns in the file
    print('Columns: \n' + '\n'.join(data.columns) + '\n')

    # List the species in the file (with no repeats)
    print('Species in file: \n' + str(pandas.unique(data['scientificName'])) + '\n')

    # Filter the data for Delma impar (Striped Legless Lizard)
    filtered_data = data[data.scientificName.eq('Delma impar')]
    print('No. entries for Striped Legless Lizard: ' + str(filtered_data.recordID.count()) + '\n')
    # Provide a summary of longitude and latitudes for this species
    print('Longitude/latitude summary for Striped Legless Lizard: \n' + str(filtered_data.describe()) + '\n')


if __name__ == '__main__':
    main()
