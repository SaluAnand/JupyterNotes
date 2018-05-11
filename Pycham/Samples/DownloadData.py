import urllib
# import os
import csv
import tempfile
import matplotlib.pyplot as plt

file = tempfile.NamedTemporaryFile()
dest = file.name + 'data.csv'
print(dest)
Year = []
population = []


def download():
    source = "http://api.worldbank.org/countries/all/indicators/SP.POP.TOTL?format=csv"
    # urllib.request.Request(source,dest)
    urllib.request.urlretrieve(source, dest)


def process():
    # un-pivot the table
    # fo = open(dest)
    # lines = [ row for row in csv.reader(fo) ]
    # headings = lines[0]
    # lines = lines[1:]
    #
    # outheadings = [ 'Country Name', 'Country Code', 'Year', 'Value' ]
    # outlines = []
    #
    # for row in lines:
    #    for idx, year in enumerate(headings[2:]):
    #        if row[idx+2]:
    #            # do not convert to float as we end up with scientific notation
    #            value = row[idx+2]
    #            outlines.append(row[:2] + [int(year), value])
    #
    # writer = csv.writer(open('population.csv', 'w'))
    # writer.writerow(outheadings)
    # writer.writerows(outlines)
    with open('population.csv', 'r') as f:
        reader = csv.reader(f)
        rownum = 0
        for row in reader:
            if (rownum >= 1):
                Year.append(row[2])
                population.append(row[3])
            rownum = rownum + 1


download()
process()
plt.plot(Year, population)
print(plt.show())
