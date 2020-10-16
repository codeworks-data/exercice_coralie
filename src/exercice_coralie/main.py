from queue import Queue
import numpy as np
import random
from time import sleep

present_sizes = np.array([1, 2, 5])
number_of_presents = 20


class PresentsQueue(Queue):
    """
    La queue pour les cadeaux
    """

    def __init__(self, number_of_presents):
        super().__init__(number_of_presents)
        random_presents_sizes_index = np.random.randint(0, 3, number_of_presents)
        random_present_sizes = present_sizes[random_presents_sizes_index]
        for present_size in random_present_sizes:
            self.put(present_size)


class Sled(object):
    """
    Le traineau
    """
    def __init__(self):
        self.remaining_capacity = 12
        self.gift_weight = []
        self.responsable_elf = Elf()

    def add_is_possible(self, present_weight):
        return present_weight <= self.remaining_capacity

    def add_present_to_traineau(self, present_weight):
        self.gift_weight.append(present_weight)
        self.remaining_capacity -= present_weight
        if self.remaining_capacity == 0:
            self.responsable_elf.notify_work_done()

    def is_full(self):
        return self.remaining_capacity==0

class TooMuchWorksError(Exception):
    """Exception lorsque le nain a beaucoup travaillé."""
    def __init__(self, message):
        self.message = message

class Elf(object):
    """
    Le nain
    """
    def __init__(self):
        self.weight_to_wrapping_time = {
            1: .5,
            2: 1,
            5: 2,
        }
        self.is_done_working = False

    def wrap_present(self, present_weight):
        if self.is_done_working:
            raise TooMuchWorksError(
                'Calling \'Elf.wrap_present\' is porhibited while \'is_done_working\' is True'
            )
        print(f'Wrapping present of size {present_weight}Kg(s)')
        print(f'Time to wrap: {self.weight_to_wrapping_time[present_weight]}s')
        print(f'Present wrapped')

    def notify_work_done(self):
        print('Traineau: Tiens notre cher nain! Le traineau est rempli8 Bravo!')
        self.is_done_working = True


if __name__ == '__main__':

    presents_queue = PresentsQueue(number_of_presents)
    filled_traineaux = []
    non_filled_traineaux = []
    def traineau_to_fill(available_sleds, presend_weight):
        for i, sled in enumerate(available_sleds):
            if sled.add_is_possible(presend_weight):
                return i
        new_sled = Sled()
        available_sleds.append(new_sled)
        return len(available_sleds)-1

    while not presents_queue.empty():

        current_present = presents_queue.get()
        print(f'Processing present of size: {current_present} Kg(s)')
        index_sled_to_fill = traineau_to_fill(non_filled_traineaux, current_present)
        sled_to_fill = non_filled_traineaux[index_sled_to_fill]
        sled_to_fill.add_present_to_traineau(current_present)
        if sled_to_fill.is_full():
            filled_traineaux.append(sled_to_fill)
            del non_filled_traineaux[index_sled_to_fill]

    for x in filled_traineaux:
        print(x.gift_weight)
    print("*"*10)
    for x in non_filled_traineaux:
        print(x.gift_weight)
    print()



    print('Hey! I\'working')
