from queue import Queue
import numpy as np
import random
from time import sleep
import argparse

SLED_MAX_CAPACITY = 12
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
    def __init__(self, MAX_CAPACITY=12):
        self.MAX_CAPACITY = 12
        self.presents_weights = []

    def get_remaining_capacity(self):
        return self.MAX_CAPACITY-sum(self.presents_weights)

    def can_add_present(self, present_weight):
        return present_weight <= self.get_remaining_capacity()

    def add_present(self, present_weight):
        self.presents_weights.append(present_weight)

    def is_empty(self):
        return len(self.presents_weights) == 0

    def remove_present(self):
        del self.presents_weights[0]

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
        self.sled = Sled()

    def can_add_present(self, present_weight):
        return self.sled.can_add_present(present_weight)

    def wrap_present(self, present_weight):
        if self.is_done_working:
            raise TooMuchWorksError(
                'Calling \'Elf.wrap_present\' is porhibited while \'is_done_working\' is True'
            )
        print(f'Wrapping present of size {present_weight}Kg(s)')
        time_to_wrap = self.weight_to_wrapping_time[present_weight]
        print(f'Time to wrap: {time_to_wrap}s')
        sleep(time_to_wrap)
        print(f'Present wrapped')
        self.sled.add_present(present_weight)

    def get_sled(self):
        return self.sled

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
        acknowledgment = False
        if random_number > 0:
            print('Livraison lancee')
            counter = 1
            while not self.sled.is_empty():
                print(
                    f'Cadeau numero {counter} est en cours de livraison'
                    f', ca prendra {self.TIME_TO_DELIVER_PER_PRESENT} secondes'
                )
                sleep(self.TIME_TO_DELIVER_PER_PRESENT)
                self.sled.remove_present()
                counter = counter+1
                print('Livre')
            acknowledgment = True
        else:
            print('Ils ont faim :/')

        return acknowledgment


class Santa(object):
    """
    Santa distributing presents
    """
    def __init__(self, number_of_presents):
        self.presents_queue = PresentsQueue(number_of_presents)
        self.elf = Elf()

    def distribute_presents(self):

        while not self.presents_queue.empty():

            current_present = self.presents_queue.get()
            print(f'Processing present of size: {current_present} Kg(s)')

            if self.elf.can_add_present(current_present):
                self.elf.wrap_present(current_present)
            else:
                self.elf.notify_work_done()
                sled = self.elf.get_sled()
                reindeer = Reindeer(sled)
                acknowledgment = reindeer.deliver_presents()
                while not acknowledgment:
                    acknowledgment = reindeer.deliver_presents()
                del reindeer
                self.elf = Elf()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Appeler le pere noel pour distributer les cadeaux.')
    parser.add_argument('--n-presents', metavar='N', type=int, help='Nombre de cadeaux',
                        default=DEFAULT_NUMBER_OF_PRESENTS)

    args = parser.parse_args()

    n_presents = args.n_presents
    #presents = random.choices(PRESENT_SIZES, k=n_presents)

    our_santa = Santa(n_presents)
    our_santa.distribute_presents()
