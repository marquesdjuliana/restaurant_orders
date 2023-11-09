from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501!


# Req 1
def test_ingredient():
    queijo_mussarela = Ingredient("queijo mussarela")
    queijo_prov = Ingredient("queijo provolone")

    assert queijo_mussarela.name == "queijo mussarela"
    assert queijo_mussarela.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
    assert hash(queijo_mussarela) == hash(queijo_mussarela.name)
    assert queijo_mussarela == Ingredient("queijo mussarela")
    assert queijo_mussarela != queijo_prov
    assert repr(queijo_mussarela) == "Ingredient('queijo mussarela')"

    assert queijo_prov.name == "queijo provolone"
    assert queijo_prov.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
    assert hash(queijo_prov) == hash(queijo_prov.name)
    assert queijo_prov == Ingredient("queijo provolone")
    assert repr(queijo_prov) == "Ingredient('queijo provolone')"
