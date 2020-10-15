from queue import Queue
import numpy as np
import random

present_sizes = np.array([1, 2, 5])
number_of_presents = 20


class PresentsQueue(Queue):

    def __init__(self, number_of_presents):
        super().__init__(number_of_presents)
        random_presents_sizes_index = np.random.randint(0, 3, number_of_presents)
        random_present_sizes = present_sizes[random_presents_sizes_index]
        for present_size in random_present_sizes:
            self.put(present_size)


if __name__=='__main__':

    presents_queue = PresentsQueue(10)
    while not presents_queue.empty():
        current_present = presents_queue.get()
        print(f'Processing present of size: {current_present} Kg(s)')

    print('Hey! I\'working')
