from queue import Queue
import numpy as np
import random
from time import sleep
import argparse


PRESENT_SIZES = np.array([1, 2, 5])
DEFAULT_NUMBER_OF_PRESENTS = 20


class PresentsQueue(Queue):
    """
    La queue pour les cadeaux
    """

    def __init__(self, number_of_presents):
        super().__init__(number_of_presents)
        random_presents_sizes_index = np.random.randint(0, 3, number_of_presents)
        random_present_sizes = PRESENT_SIZES[random_presents_sizes_index]
        for present_size in random_present_sizes:
            self.put(present_size)


class Sled(object):
    """
    Le traineau
    """
    def __init__(self):
        self.remaining_capacity = 12
        self.presents_weights = []
        self.responsable_elf = Elf()

    def add_is_possible(self, present_weight):
        return present_weight <= self.remaining_capacity

    def add_present_to_traineau(self, present_weight):
        self.responsable_elf.wrap_present(present_weight)
        self.presents_weights.append(present_weight)
        self.remaining_capacity -= present_weight
        if self.remaining_capacity == 0:
            self.responsable_elf.notify_work_done()

    def is_full(self):
        return self.remaining_capacity == 0

    def get_presents_weights(self):
        return self.presents_weights

    def set_presents_weights(self, present_weights):
        self.presents_weights = present_weights


class TooMuchWorksError(Exception):
    """Exception lorsque le nain a beaucoup travaillé."""
    def __init__(self, message):
        self.message = message

class Elf(object):
    """
    Le nain
    """
    def __init__(self, ):
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
        print('Traineau: Tiens notre cher nain! Le traineau est rempli! Bravo!')
        self.is_done_working = True


class Reindeer(object):
    """
    Le renne
    """
    def __init__(self, sled):
        self.TIME_TO_DELIVER_PER_PRESENT = .5
        self.sled = sled

    def deliver_presents(self):
        random_number = random.randint(0, 4)
        acknowledgment = 0
        if random_number > 0:
            print('Livraison lancee')
            for i, present in enumerate(self.sled.get_presents_weights()):
                print(
                    f'Cadeau numero {i + 1} est en cours de livraison'
                    f', ca prendra {self.TIME_TO_DELIVER_PER_PRESENT} secondes'
                )
                sleep(self.TIME_TO_DELIVER_PER_PRESENT)
                print('Livre')
            self.sled.set_presents_weights([])
            acknowledgment = 1
        else:
            print('Ils ont faim :/')

        return acknowledgment


class Santa(object):
    """
    Santa distributing presents
    """
    def __init__(self,number_of_presents):
        self.presents_queue = PresentsQueue(number_of_presents)
        self.non_filled_sleds = []

    def get_index_sled_to_fill(self, present_weight):

        for i, sled in enumerate(self.non_filled_sleds):
            if sled.add_is_possible(present_weight):
                return i
        new_sled = Sled()
        self.non_filled_sleds.append(new_sled)
        return len(self.non_filled_sleds)-1

    def distribute_presents(self):

        while not self.presents_queue.empty():

            current_present = self.presents_queue.get()
            print(f'Processing present of size: {current_present} Kg(s)')
            index_sled_to_fill = self.get_index_sled_to_fill(current_present)
            sled_to_fill = self.non_filled_sleds[index_sled_to_fill]
            sled_to_fill.add_present_to_traineau(current_present)
            if sled_to_fill.is_full():
                reindeer = Reindeer(sled_to_fill)
                reindeer.deliver_presents()
                del self.non_filled_sleds[index_sled_to_fill]
                del reindeer
                del sled_to_fill


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Appeler le pere noel pour distributer les cadeaux.')
    parser.add_argument('--n-presents', metavar='N', type=int, help='Nombre de cadeaux',
                        default=DEFAULT_NUMBER_OF_PRESENTS)

    args = parser.parse_args()
    print(args)
    n_presents = args.n_presents

    our_santa = Santa(n_presents)
    our_santa.distribute_presents()
