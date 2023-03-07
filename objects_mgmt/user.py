import uuid
from datetime import datetime

from models.models import Category, Income, Expense, User, Account


class UserMGMT:

    @staticmethod
    def create_partner(name: str) -> User:
        return User(
            id='',
            name=name,
            email='',
            incomes=[],
            expenses=[],
            accounts=[]
        )

    @staticmethod
    def create_partner2(user_id: str, email: str) -> User:
        return User(
            id=user_id,
            name='',
            email=email,
            incomes=[],
            expenses=[],
            accounts=[]
        )

    @staticmethod
    def add_income_to_partner(partner: User, name: str, income_sum: int) -> User:
        partner.incomes.append(
            Income(
                name=name,
                income_sum=income_sum
            )
        )

        return partner

    @staticmethod
    def add_expense_to_partner(partner: User, name: str, expense_sum: float, description: str, is_permanent: bool,
                               category: Category) -> User:
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
    def add_account_to_partner(partner: User, account: Account) -> User:
        partner.accounts.append(account)

        return partner
