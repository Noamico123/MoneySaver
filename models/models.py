from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict


@dataclass(frozen=False)
class Category:
    name: str = None
    sub_category: List[str] = None


@dataclass(frozen=False)
class Expense:
    name: str = None
    category: Category = None
    description: str = None
    expense_sum: float = None
    date: datetime = None
    is_permanent: bool = None


@dataclass(frozen=False)
class Income:
    name: str = None
    income_sum: float = None


@dataclass(frozen=False)
class Account:
    id: str = None
    name: str = None
    partners: List[Dict[str, str]] = None
    total_income: float = 0
    total_expense: float = 0
    current_amount: float = 0


@dataclass(frozen=False)
class User:
    id: str = None
    name: str = None
    email: str = None
    incomes: List[Income] = None
    expenses: List[Expense] = None
    accounts: List[Account] = None


