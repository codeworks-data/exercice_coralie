import unittest
from exercice_coralie import Sled


class SledTest(unittest.TestCase):

    def test_add_is_possible_when_enough_space(self):
        sample_sled = Sled()
        sample_sled.presents_weights = [2, 5]
        self.assertTrue(sample_sled.can_add_present(5))
        self.assertTrue(sample_sled.can_add_present(2))
        self.assertTrue(sample_sled.can_add_present(1))

    def test_add_not_possible_when_no_enough_space(self):
        sample_sled = Sled()
        sample_sled.presents_weights = [1, 5, 5]
        self.assertFalse(sample_sled.can_add_present(5))
        self.assertFalse(sample_sled.can_add_present(2))

    def test_present_is_added(self):
        sample_sled = Sled()
        initial_remaining_capacity = sample_sled.get_remaining_capacity()
        present_weight_to_add = 2
        sample_sled.add_present(present_weight_to_add)
        self.assertEqual(sample_sled.get_remaining_capacity(), initial_remaining_capacity-present_weight_to_add)
        self.assertEqual(sample_sled.presents_weights[-1], present_weight_to_add)

    def test_present_is_removed(self):
        sample_sled = Sled()
        initial_presents = [2, 1, 5]
        sample_sled.presents_weights = initial_presents.copy()
        initial_remaining_capacity = sample_sled.get_remaining_capacity()
        sample_sled.remove_present()
        self.assertEqual(sample_sled.get_remaining_capacity(), initial_remaining_capacity+initial_presents[0])
        self.assertListEqual(sample_sled.presents_weights, initial_presents[1:])
