import os
import csv

from core.transaction import Transaction
from core.transfer import Transfer, TransferManager

# TODO place in config/config.cfg
input_dir  = os.path.join("in")
output_dir = os.path.join("out")

transactions = []
transfers    = []

for file in os.listdir(input_dir):
    in_file_path = os.path.join(input_dir, file)

    account_name = file.split('.')[0]

    with open(in_file_path) as fp:
        csv_reader = csv.reader(fp)

        for row in csv_reader:
            transactions.append(Transaction(account_name, row))


# Sort Transactions by date, descending
transactions.sort(key=lambda t : t.date, reverse=True)

for transaction in transactions:
    print(transaction.dump())

# Build list of Transfers (NOTE: unused)
transfers = TransferManager.BuildTransfers(transactions)

