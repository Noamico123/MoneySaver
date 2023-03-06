from Models.models import Account, Partner


class AccountMGMT:

    @staticmethod
    def create_account(name: str, number_of_partners: int) -> Account:
        return Account(
            name=name,
            number_of_partners=number_of_partners,
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
    def add_partner_to_account(account: Account, partner: Partner) -> Account:
        account.partners.append({partner.id: partner.name})
        return account

