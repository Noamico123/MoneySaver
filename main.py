from typing import Dict

from consts import ID, EMAIL, USERS
from objects_mgmt.account import AccountMGMT
from objects_mgmt.categories import CategoriesMGMT
from firebase_auth import is_sign_up, is_logged_in
from objects_mgmt.user import UserMGMT


def test_functionality():
    categories = CategoriesMGMT.init_base_categories()

    first_partner = UserMGMT.create_partner(name="Bob")

    first_account = AccountMGMT.create_account(
        name="MyAccount",
    )

    AccountMGMT.add_partner_to_account(account=first_account, partner=first_partner)
    UserMGMT.add_account_to_partner(partner=first_partner, account=first_account)

    print(f'\n##1##\n{first_partner}')
    print(f'\n##1##\n{first_account}')

    UserMGMT.add_income_to_partner(partner=first_partner, name="Work", income_sum=10000)

    for income in first_partner.incomes:
        AccountMGMT.add_income_to_account(account=first_account, income=income.income_sum)

    print(f'\n##2##\n{first_partner}')
    print(f'\n##2##\n{first_account}')

    UserMGMT.add_expense_to_partner(
        partner=first_partner,
        name="shopping",
        description="",
        expense_sum=400,
        category=categories[10],
        is_permanent=False,
    )

    UserMGMT.add_expense_to_partner(
        partner=first_partner,
        name="gas",
        description="",
        expense_sum=150,
        category=categories[8],
        is_permanent=False,
    )

    for expense in first_partner.expenses:
        AccountMGMT.add_expense_to_account(account=first_account, expense=expense.expense_sum)

    AccountMGMT.set_current_amount_to_account(account=first_account)

    print(f'\n##3##\n{first_partner}')
    print(f'\n##3##\n{first_account}')

    print(f'\ntotal_expense  {first_account.total_expense}')
    print(f'\ntotal_income  {first_account.total_income}')
    print(f'\ncurrent_amount  {first_account.current_amount}')


def test2(user_id: str, email: str):

    first_partner = UserMGMT.create_partner2(
        user_id=user_id,
        email=email
    )

    print(f'\n# {first_partner}')


def init_app() -> Dict:
    answer = input('new user? [y/n]')

    if answer == 'y':
        if is_sign_up():
            return is_logged_in()

        else:
            return {}

    if answer == 'n':
        return is_logged_in()


if __name__ == '__main__':
    res = init_app()

    if not res:
        print('An error occurred')

    else:
        users = res.get(USERS)

        if len(users) == 1:
            email = users[0].get(EMAIL)
            user_id = users[0].get(ID)
            print(f'# ID: {user_id} \n# Email: {email}')
            # test2(user_id=user_id, email=email)




