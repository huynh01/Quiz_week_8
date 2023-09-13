import matplotlib.pyplot as plt
import pandas as pd


# Load data from the CSV file
data = pd.read_csv('climate.csv')

# Extract the columns from the data
years = data['Year']
co2 = data['CO2']
temp = data['Temperature']

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 

