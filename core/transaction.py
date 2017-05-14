
class Transaction():
    def __init__(self, record):
        """ Build Transaction object on transaction record
        :param record: [ date, description, debit, credit ]

        TODO set empty debit/credit to 0
        TODO convert date to datetime object

        """
        if len(record) < 4:
            raise Exception(f"Invalid record '{record}'")

        # TODO validate these values
        self._date   = record[0]
        self._desc   = record[1]
        self._debit  = record[2]
        self._credit = record[3]

    @property
    def date(self):
        return self._date

    @property
    def description(self):
        return self._desc

    @property
    def debit(self):
        return self._debit

    @property
    def credit(self):
        return self._credit
