import csv
import argparse


def remove_uncategorized_products(file_input):
    try:
        with open(file_input, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return [row for row in reader if row["Categories"]]
    except FileNotFoundError:
        err = f"{file_input} does not exist on your root dirctory."
        raise FileNotFoundError(err)


def export_categorized_products(file_input, file_output):
    categorized_products = remove_uncategorized_products(file_input)
    if not categorized_products:
        return None

    with open(file_output, 'w', newline='') as csvfile:
        fieldnames = list(categorized_products[0].keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for product in categorized_products:
            writer.writerow(product)


def is_csv(filename):
    return 'csv' == filename.split('.')[-1]


def process_file(file_input, file_output):
    try:
        if not is_csv(file_input):
            print(f"{file_input} is not a valid csv file.")
            return
        if not is_csv(file_output):
            print(f"{file_output} is not a valid csv file.")
            return
        export_categorized_products(file_input, file_output)
        print(f"successfully process file {file_input}", end=' ')
        print(f"results can be found at {file_output}")
    except FileNotFoundError as e:
        print(e)


parser = argparse.ArgumentParser(description='Products CSV Reader and Writer')
parser.add_argument('--file-input', type=str, required=True,
                    help='The file to be read')
parser.add_argument('--file-output', type=str, required=True,
                    help='The exported csv file with categorized products.')
args = parser.parse_args()
process_file(args.file_input, args.file_output)
