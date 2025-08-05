#import numpy
import numpy as np

#define array for rainfall
sample_rainfall = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]
#convert it ito the array
rainFallArray = np.array([sample_rainfall])

#print the list as array 
print(f"Rain fall as aray : {rainFallArray}")

#total
sumOfRainnFall = np.sum(rainFallArray)
print(f"Sum of the total rainfall : {sumOfRainnFall}")

#Avarege
avaregeOfRainfall = np.average(sample_rainfall)
print(f"Average of the total rainfall : {avaregeOfRainfall}")

#find Zero rain fall days
#mtd1
count = 0
for i in sample_rainfall:
    if i==0:
        count = count + 1
print(f"Total number of zero rainfall days : {count}")

#Mtd2
count1=0
for i in range(len(sample_rainfall)):
    if sample_rainfall[i]==0:
        count1 = count1 +1
print(f"Total number of zero rainfall days : {count1}")

#Print the days (by index) where the rainfall was more than 5 mm
for i in range(len(sample_rainfall)):
    if sample_rainfall[i]>5:
        print(f"Print the days (by index) where the rainfall was more than 5 mm Index {i} : {sample_rainfall[i]}")

