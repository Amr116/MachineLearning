from random import seed
from random import randrange
from csv import reader
from math import sqrt

# Load the observations dataFile => csv file.
def LoadCsv(fn):
	dataSet = list()
	with open(fn, 'r') as f:
		csvReader = reader(f)
		for row in csvReader:
			if not row:
				continue
			dataSet.append(row)
	return dataSet


# # convert string attributes to float
def ConvertAttributeColumnToFloat(dataset):
    for row in dataset:
        for i in range(0, len(row)-1):
            row[i] = float(row[i].strip())


# Convert string label to Int
def ConvertLabelColumnToInt(dataset):
    labelIndex = len(dataset[0])-1
    labels = [row[labelIndex] for row in dataset]
    unique = set(labels)
    lookup = dict()
    for idx, val in enumerate(unique):
        lookup[val] = idx
    for row in dataset:
        row[labelIndex] = lookup[row[labelIndex]]
    return lookup