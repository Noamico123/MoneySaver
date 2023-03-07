from models.models import Account, User


class AccountMGMT:

    @staticmethod
    def create_account(name: str) -> Account:
        return Account(
            name=name,
            partners=[],
            total_income=0,
            total_expense=0,
            current_amount=0
        )

    @staticmethod
    def add_expense_to_account(account: Account, expense: float) -> Account:
        account.total_expense += expense
        return account

    @staticmethod
    def add_income_to_account(account: Account, income: float) -> Account:
        account.total_income += income
        return account

    @staticmethod
    def set_current_amount_to_account(account: Account) -> Account:
        account.current_amount = account.total_income - account.total_expense
        return account

    @staticmethod
    def add_partner_to_account(account: Account, partner: User) -> Account:
        account.partners.append({partner.id: partner.name})
        return account

