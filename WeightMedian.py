import csv

with open("py2/HeightWeight.csv",newline= '') as f:
    reader = csv.reader(f) #reading the csv file
    file_data = list(reader) #storing the data in a list

file_data.pop(0) #removing the title list from the data
#print(file_data)
#sorting data to get height of the people
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))

n = len(new_data)
new_data.sort()#sorting the data in ascending order

#using floor division to get the nearest whole number
#floor division is shown by //
if(n % 2 == 0):
    #getting the 1st number
    median1 = float(new_data[n//2])
    #getting the 2nd number
    median2 = float(new_data[n//2-1])
    #getting the mean of those numbers
    median = (median1+median2)/2

else:
    median = new_data[n//2]
    
print("Median is : " + str(median))