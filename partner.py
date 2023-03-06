import uuid
from datetime import datetime

from Models.models import Category, Income, Expense, Partner, Account


class PartnerMGMT:

    @staticmethod
    def create_partner(name: str) -> Partner:
        return Partner(
            id=str(uuid.uuid4()),
            name=name,
            incomes=[],
            expenses=[],
            accounts=[]
        )

    @staticmethod
    def add_income_to_partner(partner: Partner, name: str, income_sum: int) -> Partner:
        partner.incomes.append(
            Income(
                name=name,
                income_sum=income_sum
            )
        )

        return partner

    @staticmethod
    def add_expense_to_partner(partner: Partner, name: str, expense_sum: float, description: str, is_permanent: bool,
                               category: Category) -> Partner:
        partner.expenses.append(
            Expense(
                name=name,
                expense_sum=expense_sum,
                category=category,
                description=description,
                date=datetime.now(),
                is_permanent=is_permanent,
            )
        )
        return partner

    @staticmethod
    def add_account_to_partner(partner: Partner, account: Account) -> Partner:
        partner.accounts.append(account)

        return partner
