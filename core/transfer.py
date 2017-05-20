from collections import defaultdict

from . transaction import Transaction

class Transfer():
    def __init__(self, t1, t2):
        """ Init a pair of Transactions, between accounts """
        #print(f"Transfer::__init__({t1}, {t2})")
        self.fr = t1
        self.to = t2

    @property
    def fr(self):
        return self._fr

    @fr.setter
    def fr(self, t):
        self._fr = self._parse_transaction(t)

    @property
    def to(self):
        return self._to

    @to.setter
    def to(self, t):
        self._to = self._parse_transaction(t)

    def _parse_transaction(self, t):
        """ TODO Break up str into relevant parts and return"""
        #print(f"Transfer::_parse_transaction({t.dump()})\t# dump()")
        return t


class TransferManager():

    @staticmethod
    def BuildTransfers(transactions):
        """ Build list of paired Transfers using given Transaction[] """

        transfer_pairs = []
        tmp_transfers      = defaultdict(dict)

        for transaction in transactions:
            id = transaction.description.split(' ')[0]

            if "TFR-FR" in transaction.description:
                tmp_transfers[id]["fr"] = transaction

            elif "TFR-TO" in transaction.description:
                tmp_transfers[id]["to"] = transaction

        # TODO handle transactions with no pair somehow ...
        for id, pair in tmp_transfers.items():
            if len(pair) < 2:
                #print(f"Transaction with no pair {id}!")
                continue

            transfer_pairs.append(Transfer(*pair.values()))

