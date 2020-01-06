

class TestGeography:
    """
    Test class for the geography of the landscape
    """

    def test_init(self):
        """
        Tests the init of the geography class
        :return:
        """
        pass

    def test_locations(self):
        """
        Test that the tiles are in the right place
        :return:
        """
        pass

    def test_no_food_in_mountains_or_desert(self):
        """
        Test if there is any food in the mountains or in the desert
        :return:
        """
        pass


class TestAnimals:
    """
    Test class for animal properties
    """
    def test_fitness(self):
        """
        Test that the fitness is calculated porperly
        :return:
        """
        pass

    def test_move(self):
        """
        Test that both animal types can move porperly
        :return:
        """
        pass

    def test_mountain_and_water_impassable(self):
        """
        Test that animals cannot move through mountains or water
        :return:
        """
        pass

    def test_eating(self):
        """
        Test that eating works as it should
        :return:
        """
        pass

    def test_mating_and_weight(self):
        """
        Test the mating function, and that there is no offspring if offsprings
        weight surpasses the weight of the mother
        :return:
        """
        pass

    def test_death(self):
        """
        Test that an animal dies if its fitness is 0
        :return:
        """
        pass

    def test_hunting(self):
        """
        Test the hunting capabilities of the predators. Go for the herbivore
        with lowest fitness and stop if all herbivores have been attempted
        :return:
        """
        pass


class TestYearCycle:

    def test_order_actions(self):
        """
        Regrowth at the beginning of each year, herbivores eat first,
        migration, aging, loss of weight, death
        :return:
        """
        pass

    def test_non_negative_values(self):
        """
        Test that fitness, age and weight cannot be negative
        :return:
        """
        pass
