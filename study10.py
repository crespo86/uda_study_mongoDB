"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in the range as described above,
  write that line to the output_good file
- if the value of the field is not a valid year as described above,
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
import pprint

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

def process_file(input_file, output_good, output_bad):

    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        for row in reader:
            # validate URI value
            if row['URI'].find("dbpedia.org") < 0:
                continue

            ps_year = row['productionStartYear'][:4]
            try: # use try/except to filter valid items
                ps_year = int(ps_year)
                row['productionStartYear'] = ps_year
                if (ps_year >= 1886) and (ps_year <= 2014):
                    data_good.append(row)
                else:
                    data_bad.append(row)
            except ValueError: # non-numeric strings caught by exception
                if ps_year == 'NULL':
                    data_bad.append(row)
'''
    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        good = []
        bad = []
        for line in reader:
            if (line['productionStartYear'][0] == '1' or
                line['productionStartYear'][0] == '2'):
                if (int(line['productionStartYear'][0:4]) > 1886 and
                    int(line['productionStartYear'][0:4]) < 2014):
                    line['productionStartYear'] = line['productionStartYear'][0:4]
                    good.append(line)
                else:
                    bad.append(line)
            else:
                if line['URI'][0:8] == "http://d":
                    bad.append(line)
'''

        with open(output_good, "w") as g:
            writer = csv.DictWriter(g, delimiter=",", fieldnames= header)
            writer.writeheader()
            for row in good:
                writer.writerow(row)

        with open(OUTPUT_BAD, "w") as g:
            writer = csv.DictWriter(g, delimiter=",", fieldnames= header)
            writer.writeheader()
            for row in bad:
                writer.writerow(row)


        #COMPLETE THIS FUNCTION



def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()
