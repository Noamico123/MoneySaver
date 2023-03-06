from account import AccountMGMT
from categories import CategoriesMGMT
from partner import PartnerMGMT

if __name__ == '__main__':

    categories = CategoriesMGMT.init_base_categories()

    first_partner = PartnerMGMT.create_partner(name="Bob")

    first_account = AccountMGMT.create_account(
        name="MyAccount",
        number_of_partners=1
    )

    AccountMGMT.add_partner_to_account(account=first_account, partner=first_partner)
    PartnerMGMT.add_account_to_partner(partner=first_partner, account=first_account)

    print(f'\n##1##\n{first_partner}')
    print(f'\n##1##\n{first_account}')

    PartnerMGMT.add_income_to_partner(partner=first_partner, name="Work", income_sum=10000)

    for income in first_partner.incomes:
        AccountMGMT.add_income_to_account(account=first_account, income=income.income_sum)

    print(f'\n##2##\n{first_partner}')
    print(f'\n##2##\n{first_account}')

    PartnerMGMT.add_expense_to_partner(
        partner=first_partner,
        name="shopping",
        description="",
        expense_sum=400,
        category=categories[10],
        is_permanent=False,
    )

    PartnerMGMT.add_expense_to_partner(
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
