import numpy as np
temperatureArray_in_Celcius = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

max_temp = np.max(temperatureArray_in_Celcius)
min_temp = np.min(temperatureArray_in_Celcius)

print(f"Max Temperature: {max_temp}°C")
print(f"Min Temperature: {min_temp}°C")

#convert temperature as FerenFahrenheit
fahrenheit_Temperature = (temperatureArray_in_Celcius * 9/5) +32

# Print the results
print(f"Celsius temperatures: {temperatureArray_in_Celcius}")
print(f"Fahrenheit temperatures: {fahrenheit_Temperature}")

noOfDaysBelow20 = []

for i in range(len(temperatureArray_in_Celcius)):
    if temperatureArray_in_Celcius[i] > 20:
        noOfDaysBelow20.append(i)

print("Indices of days where temperature exceeded 20°C:", len(noOfDaysBelow20))
