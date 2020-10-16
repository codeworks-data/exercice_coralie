import unittest
from exercice_coralie import Sled


class SledTest(unittest.TestCase):

    def test_add_is_possible(self):
        sample_sled = Sled()
        sample_sled.remaining_capacity = 6
        self.assertTrue(sample_sled.add_is_possible(5), 'Case 1')
        self.assertTrue(sample_sled.add_is_possible(2), 'Case 1')
        self.assertTrue(sample_sled.add_is_possible(1), 'Case 1')
        sample_sled.remaining_capacity = 3
        self.assertFalse(sample_sled.add_is_possible(5), 'Case 2')
        self.assertTrue(sample_sled.add_is_possible(2), 'Case 2')
        self.assertTrue(sample_sled.add_is_possible(1), 'Case 2')
        sample_sled.remaining_capacity = 0
        self.assertFalse(sample_sled.add_is_possible(5), 'Case 3')
        self.assertFalse(sample_sled.add_is_possible(2), 'Case 3')
        self.assertFalse(sample_sled.add_is_possible(1), 'Case 3')

    def test_add_present_to_traineau_sled_arrtibutes(self):
        sample_sled = Sled()
        initial_remaining_capacity = sample_sled.remaining_capacity
        present_weight_to_add = 2
        sample_sled.add_present_to_traineau(present_weight_to_add)
        self.assertEqual(sample_sled.remaining_capacity, initial_remaining_capacity-present_weight_to_add)
        self.assertEqual(sample_sled.gift_weight[-1], present_weight_to_add)

    def test_is_full(self):
        sample_sled = Sled()
        sample_sled.remaining_capacity = 6
        self.assertFalse(sample_sled.is_full())
        sample_sled.remaining_capacity = 0
        self.assertTrue(sample_sled.is_full())

