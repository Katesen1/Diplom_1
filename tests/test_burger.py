from extra.burger import Burger
from extra.bun import Bun
from tests import data
import pytest


class TestBurger:
    def test_burger_init(self, burger: Burger):
        assert burger.bun is None and burger.ingredients == []

    def test_set_buns(self, burger: Burger):
        bun = Bun(*data.bun_red)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredients(self, burger: Burger):
        ingredient = data.ing_dino
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    @pytest.mark.parametrize(
        "ingredients, index, expected_ingredients",
        [[[data.ing_dino], 0, []], [[data.ing_dino, data.ing_cream], 0, [data.ing_cream]], [[data.ing_dino, data.ing_cream], 1, [data.ing_dino]]])
    def test_remove_ingredient(self, burger: Burger, ingredients, index, expected_ingredients):
        burger.ingredients = ingredients
        burger.remove_ingredient(index)
        assert burger.ingredients == expected_ingredients

    @pytest.mark.parametrize('ingredients, index',
                             [[[], 0], [[data.ing_dino], 1]])
    def test_remove_ingredient_error(self, burger: Burger, ingredients, index):
        burger.ingredients = ingredients
        with pytest.raises(IndexError):
            burger.remove_ingredient(index)

    def test_move_ingredients(self, burger: Burger):
        burger.ingredients = [data.ing_dino, data.ing_cream]
        index = 0
        new_index = 1
        burger.move_ingredient(index, new_index)
        assert burger.ingredients[0] == data.ing_cream and burger.ingredients[1] == data.ing_dino

    def test_move_zero_ingredients(self, burger: Burger):
        burger.ingredients = []
        index = 0
        new_index = 1
        with pytest.raises(IndexError):
            burger.move_ingredient(index, new_index)
        
    def test_move_more_than_ingredients(self, burger: Burger):
        burger.ingredients = [data.ing_dino, data.ing_cream]
        index = 2
        new_index = 1
        with pytest.raises(IndexError):
            burger.move_ingredient(index, new_index)

    def test_get_price(self, burger: Burger):
        burger.bun = Bun(*data.bun_black)
        burger.ingredients = [data.ing_dino, data.ing_cream]
        price = burger.get_price()
        assert price == 600
        
    def test_get_receipt(self, burger: Burger):
        burger.bun = Bun(*data.bun_black)
        burger.ingredients = [data.ing_dino, data.ing_cream]
        receipt = burger.get_receipt()
        assert '(==== black bun ====)\n= filling dinosaur =\n= sauce sour cream =\n(==== black bun ====)\n\nPrice: 600' == receipt