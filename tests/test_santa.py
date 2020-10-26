import unittest
from presents_distributing_lib import Santa


class SantaTest(unittest.TestCase):

    def test_number_of_presents_added_matches_the_parameter(self):
        number_of_presents_initial = 4
        number_of_presents_to_add = 3
        expected_number_of_presents = number_of_presents_initial + number_of_presents_to_add

        sample_santa = Santa(number_of_presents_initial)
        sample_santa.add_more_presents(number_of_presents_to_add)

        actual_number_presents = len(sample_santa.presents_queue)
        self.assertEqual(expected_number_of_presents, actual_number_presents)

    def test_weights_of_presents_added_are_in_the_norm(self):
        normal_weights = [1, 2, 5]
        number_of_presents_initial = 4
        number_of_presents_to_add = 3

        sample_santa = Santa(number_of_presents_initial)
        sample_santa.add_more_presents(number_of_presents_to_add)

        weights_of_presents_added = sample_santa.presents_queue[-number_of_presents_to_add:]
        all_weights_are_normal_bool = all([weight in normal_weights for weight in weights_of_presents_added])

        self.assertTrue(all_weights_are_normal_bool)
