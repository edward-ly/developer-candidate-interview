import csv

if __name__ == "__main__":
    with open('instructor_availability.csv', 'rb') as inst_csv:
        inst_reader = csv.reader(inst_csv)
        for row in inst_reader:
            print ', '.join(row)

    with open('input.csv', 'rb') as input_csv:
        input_reader = csv.reader(input_csv)
        for row in input_reader:
            print ', '.join(row)
