import unittest
import random
from queue import Queue
from exercice_coralie import PresentsQueue


class PresentsQueueTest(unittest.TestCase):

    def test_is_queue(self):
        random_presents_queue_size = random.randint(5, 11)
        random_presents_queue = PresentsQueue(random_presents_queue_size)
        self.assertIsInstance(random_presents_queue, Queue)

    def test_size_is_good(self):
        random_presents_queue_size = random.randint(5, 11)
        random_presents_queue = PresentsQueue(random_presents_queue_size)
        self.assertEqual(random_presents_queue.qsize(), random_presents_queue_size)

    def test_weights_are_good(self):
        random_presents_queue_size = random.randint(5, 11)
        random_presents_queue = PresentsQueue(random_presents_queue_size)
        while not random_presents_queue.empty():
            present_weight = random_presents_queue.get()
            self.assertIn(present_weight, [1, 2, 5])

