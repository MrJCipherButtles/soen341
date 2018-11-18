from abc import ABC


class Loanable(ABC):
    def __init__(self, clientId=None, loanDate=None, dueDate=None, returnDate=None):
        self.client_id = clientId
        self.loan_date = loanDate
        self.due_date = dueDate
        self.return_date = returnDate
