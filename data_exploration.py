import pandas

# Load the data from file using pandas
data = pandas.read_csv('data/ALA_EcoCommons_Data_Analyst_dataset.csv')

# Quick preview of the first few records in the file
print('Preview:')
print(data.head())
print('\n')

print('Columns: ' + ', '.join(data.columns))