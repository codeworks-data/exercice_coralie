import unittest
from presents_distributing_lib import Sled


class SledTest(unittest.TestCase):

    def test_should_be_able_to_add_present_when_enough_space(self):
        sample_sled = Sled()
        sample_sled.presents_weights = [2, 5]

        self.assertTrue(sample_sled.can_add_present(5))
        self.assertTrue(sample_sled.can_add_present(2))
        self.assertTrue(sample_sled.can_add_present(1))

    def test_should_not_be_able_to_add_present_when_no_enough_space(self):
        sample_sled = Sled()
        sample_sled.presents_weights = [1, 5, 5]

        self.assertFalse(sample_sled.can_add_present(5))
        self.assertFalse(sample_sled.can_add_present(2))

    def test_remaining_capacity_decrease_by_weight_when_present_is_added(self):
        sample_sled = Sled()
        initial_remaining_capacity = sample_sled.get_remaining_capacity()
        present_weight_to_add = 2
        expected_capacity = initial_remaining_capacity-present_weight_to_add

        sample_sled.add_present(present_weight_to_add)
        actual_capacity = sample_sled.get_remaining_capacity()

        self.assertEqual(expected_capacity, actual_capacity)

    def test_the_weight_is_added_at_the_end_of_the_sled_when_present_is_added(self):
        present_weight_to_add = 2

        sample_sled = Sled()
        sample_sled.add_present(present_weight_to_add)
        last_present_weight = sample_sled.presents_weights[-1]

        self.assertEqual(present_weight_to_add, last_present_weight)

    def test_remaining_capacity_increase_by_weight_when_present_is_removed(self):
        initial_presents = [2, 1, 5]

        sample_sled = Sled()
        sample_sled.presents_weights = initial_presents.copy()
        initial_remaining_capacity = sample_sled.get_remaining_capacity()
        expected_remaining_capacity = initial_remaining_capacity+initial_presents[0]

        sample_sled.remove_present()
        actual_remaining_capacity = sample_sled.get_remaining_capacity()

        self.assertEqual(expected_remaining_capacity, actual_remaining_capacity)

    def test_present_is_removed(self):
        initial_presents = [2, 1, 5]

        sample_sled = Sled()
        sample_sled.presents_weights = initial_presents.copy()
        expected_remainig_presents = initial_presents[1:]

        sample_sled.remove_present()
        actual_remaining_presents = sample_sled.presents_weights

        self.assertListEqual(expected_remainig_presents, actual_remaining_presents)
