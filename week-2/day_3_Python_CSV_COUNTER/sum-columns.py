import csv
import sys

def sum_column(filename, column_number):
    total = 0.0
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)

        # Ensure that column_number is valid
        if column_number < 1 or column_number > len(header):
            print(f"Error: Invalid column number. Please select between 1 and {len(header)}")
            return

        # Loop through rows to sum values in the desired column
        for row in reader:
            try:
                value = float(row[column_number - 1])  # Convert value to float
                total += value
            except ValueError:
                # Skip rows with non-numeric values in the column
                continue

    print(f"The total '{header[column_number-1]}' is {total:,.1f}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: sum-columns.py <filename.csv> <column_number>")
        sys.exit(1)
    filename = sys.argv[1]
    try:
        column_number = int(sys.argv[2])
    except ValueError:
        print("Error: Invalid column number. It should be an integer.")
        sys.exit(1)

    sum_column(filename, column_number)
