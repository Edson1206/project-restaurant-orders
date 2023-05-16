from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    dish = Dish("batata", 450.00)
    ingredient = Ingredient("batata")
    dish.add_ingredient_dependency(ingredient, 450)

    with pytest.raises(TypeError):
        Dish("name", None)
    with pytest.raises(ValueError):
        Dish("name", -10.00)

    assert dish.name == "batata"
    assert dish.get_restrictions() == set()
    assert dish.__repr__() == "Dish('batata', R$450.00)"
    assert dish == dish
    assert hash(dish) == hash(repr(dish))
    assert dish.get_ingredients() == set({ingredient})
