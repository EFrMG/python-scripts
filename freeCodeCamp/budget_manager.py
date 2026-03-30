class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        # sum also subtracts if the item begins with a minus sign
        return sum(item["amount"] for item in self.ledger)

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:  # Not enough funds
            return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:  # Not enough funds
            return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        # Format Specification Mini-Language
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            desc = f"{item['description'][:23]:<23}"
            # 7 chars; 2 digit; fixed-point
            amt = f"{item['amount']:>7.2f}"
            items += f"{desc}{amt}\n"
        total = f"Total: {self.get_balance()}"
        return title + items + total


def create_spend_chart(categories):
    spendings = []
    for cat in categories:
        spent = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        spendings.append(spent)

    total_spent = sum(spendings)
    percentages = [(s / total_spent * 100) // 10 * 10 for s in spendings]

    # Layout constants
    Y_LABEL_WIDTH = 3
    Y_OFFSET = Y_LABEL_WIDTH + 1
    BAR_SEP = "  "  # Between bars

    res = "Percentage spent by category\n"
    # Reverse range to count down from 100 to 0 included
    for i in range(100, -1, -10):
        res += f"{i:>{Y_LABEL_WIDTH}}| "
        for p in percentages:
            res += "o" + BAR_SEP if p >= i else " " + BAR_SEP
        res += "\n"

    # Horizontal line: starts after the labels, length covers all categories + 1 extra
    res += " " * Y_OFFSET + "-" * (len(categories) * 3 + 1) + "\n"

    names = [cat.name for cat in categories]
    max_len = max(len(n) for n in names)
    padded_names = [f"{n:<{max_len}}" for n in names]

    for i in range(max_len):
        # Vertical names start 1 space past the dash-line offset
        res += " " * (Y_OFFSET + 1)
        for name in padded_names:
            res += name[i] + BAR_SEP
        if i < max_len - 1:
            res += "\n"

    return res
