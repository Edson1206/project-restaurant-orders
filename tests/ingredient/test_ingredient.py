from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient('gluten')
    ingredient2 = Ingredient('lactose')

    assert ingredient.name == 'gluten'
    assert ingredient2.name == 'lactose'
    assert hash(ingredient) == hash('gluten')
    assert repr(ingredient) == "Ingredient('gluten')"
    assert ingredient.restrictions == set()
    assert ingredient == ingredient
    assert ingredient != ingredient2
