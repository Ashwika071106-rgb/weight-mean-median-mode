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

#getting the mean
n = len(new_data)
total = 0

for x in new_data:
    total = total+x

mean = total/n
print("Mean is : " + str(mean))