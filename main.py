import os
import csv

from core.transaction import Transaction

# TODO place in config/config.cfg
input_dir  = os.path.join("in")
output_dir = os.path.join("out")

transactions = []

for file in os.listdir(input_dir):
    in_file_path = os.path.join(input_dir, file)

    print(in_file_path)

    with open(in_file_path) as fp:
        csv_reader = csv.reader(fp)

        for row in csv_reader:

            trans_date = row[0]
            trans_desc = row[1]
            debit      = row[2]
            credit     = row[3]

            transactions.append(Transaction([trans_date,
                                             trans_desc,
                                             debit,
                                             credit]))

for transaction in transactions:
    print(f"{transaction.credit}")

