import datetime

class Transaction():
    def __init__(self, account, record):
        """ Build Transaction object on transaction record, and account name
        :param account: str account name
        :param record: [ date, description, debit, credit ]
        """
        if len(record) < 4:
            raise Exception(f"Invalid record '{record}'")

        self.account = account

        self.date   = record[0]
        self.desc   = record[1]
        self.debit  = record[2]
        self.credit = record[3]

    def dump(self):
        """ Return formatted str summary """
        return f"{self.date} - {self.account}: {self.description} {self.credit}, {self.debit}"

    @property
    def account(self):
        return self._account

    @property
    def date(self):
        """ Return simple date str.
        For access to datetime obj, use `Transaction._date` """
        return self._date.strftime("%Y-%m-%d")

    @property
    def description(self):
        return self._desc

    @property
    def debit(self):
        return self._debit

    @property
    def credit(self):
        return self._credit

    @account.setter
    def account(self, acct):
        self._account = acct.upper()

    @date.setter
    def date(self, d):
        """ Convert to proper datetime object """
        self._date = datetime.datetime.strptime(d, "%m/%d/%Y")

    @description.setter
    def desc(self, d):
        """ Set member to given str, no validation """
        self._desc = d

    @debit.setter
    def debit(self, d):
        """ Set member to given float, else set to 0.0 """
        if len(d) < 1:
            d = 0.0
        self._debit = float(d) * -1

    @credit.setter
    def credit(self, d):
        """ Set member to given float, else set to 0.0 """
        if len(d) < 1:
            d = 0.0
        self._credit = float(d)

