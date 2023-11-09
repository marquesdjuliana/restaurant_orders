from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    lasanha = Dish("Lasanha", 30.0)
    pizza = Dish("Pizza", 25.0)

    assert lasanha.name == "Lasanha"
    assert lasanha.price == 30.0
    assert repr(lasanha) == "Dish('Lasanha', R$30.00)"

    queijo_mussarela = Ingredient("queijo mussarela")
    presunto = Ingredient("presunto")
    lasanha.add_ingredient_dependency(queijo_mussarela, 200)
    lasanha.add_ingredient_dependency(presunto, 150)

    assert queijo_mussarela in lasanha.get_ingredients()
    assert presunto in lasanha.get_ingredients()

    assert lasanha.recipe[queijo_mussarela] == 200
    assert lasanha.recipe[presunto] == 150

    assert pizza.name == "Pizza"
    assert pizza.price == 25.0
    assert repr(pizza) == "Dish('Pizza', R$25.00)"

    molho_tomate = Ingredient("molho de tomate")
    queijo_prov = Ingredient("queijo provolone")
    pizza.add_ingredient_dependency(molho_tomate, 150)
    pizza.add_ingredient_dependency(queijo_prov, 180)

    assert molho_tomate in pizza.get_ingredients()
    assert queijo_prov in pizza.get_ingredients()

    assert pizza.recipe[molho_tomate] == 150
    assert pizza.recipe[queijo_prov] == 180

    lasanha_copy = Dish("Lasanha", 30.0)
    assert lasanha == lasanha_copy
    assert lasanha != pizza

    assert hash(lasanha) == hash(lasanha_copy)
    assert hash(pizza) != hash(lasanha)

    assert lasanha.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }

    assert pizza.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.LACTOSE,
    }

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("InvalidDish", "invalid_price")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("InvalidDish", 0.00)
