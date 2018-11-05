import csv

with open('goibibo_com-travel_sample.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print 'Column names are ', row
            line_count += 1
        else:
            print 'line number: ', line_count
            line_count += 1
    print 'Processed ', line_count, 'lines.\n'