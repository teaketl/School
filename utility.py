import csv;

def readCSV(file):
        allData = []; #store everything in 2d array
        for line in file:
            newRow = line.split(",") #line = each individual line
            newLastvalue = newRow[len(newRow) -1];
            newRow[len(newRow) -1] = newLastvalue[0:len(newLastvalue) -1];
            allData.append(newRow);
        return allData;

def appendCSV(file, newData):
    openFile = open(file,'a',newline='');
    writer = csv.writer(openFile);
    writer.writerow(newData);
    file.close();
