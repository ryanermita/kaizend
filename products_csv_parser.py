import csv


def remove_uncategorized_products(csvFile):
    with open('sample_products.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader if row["Categories"]]


def export_categorized_products(csvFile):
    categorized_products = remove_uncategorized_products(csvFile)
    if not categorized_products:
        return None

    with open('names.csv', 'w', newline='') as csvfile:
        fieldnames = list(categorized_products[0].keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for product in categorized_products:
            writer.writerow(product)


export_categorized_products('sample_products.csv')
