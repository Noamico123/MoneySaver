from typing import List

from models.models import Category


class CategoriesMGMT:

    @staticmethod
    def init_base_categories() -> List[Category]:
        return [
            Category(name='Insurance', sub_category=['Car', 'Home']),
            Category(name='Internet', sub_category=[]),
            Category(name='Electricity', sub_category=[]),
            Category(name='Water', sub_category=[]),
            Category(name='Home Tax', sub_category=[]),
            Category(name='TV', sub_category=[]),
            Category(name='Digital Account', sub_category=['Google', 'Netflix', 'Spotify', 'Norton']),
            Category(name='Transportation', sub_category=['Scooter', 'Taxi', 'Bus', 'Fuel']),
            Category(name='Pets', sub_category=['Food', 'Toys', 'Accessories']),
            Category(name='Food', sub_category=['Market', 'Deliveries', 'Grocery']),
            Category(name='pleasures',
                     sub_category=['Clothing', 'Vacation', 'Sports', 'Smokes', 'Restaurants', 'Concerts', 'Pubs']),
        ]

    @staticmethod
    def add_category(categories_to_edit: List[Category], category_name: str, sub_category_name: List[str] = None) -> List[
        Category]:
        categories_to_edit.append(Category(name=category_name, sub_category=sub_category_name))

        return categories_to_edit

    @staticmethod
    def add_sub_category_to_category(categories: List[Category], category_name: str, sub_category_name: str) -> List[Category]:
        for category in categories:
            if category.name == category_name:
                category.sub_category.append(sub_category_name)

        return categories
