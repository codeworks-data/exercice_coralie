import random
from time import sleep

from .sled import Sled


class Reindeer(object):
    """
    The reindeer has for role to deliver the presents one by one from the sled
    """
    def __init__(self, sled: Sled):
        self.TIME_TO_DELIVER_PER_PRESENT = .5
        self.sled = sled

    def deliver_presents(self):
        """
        Deliver the presents in the sled.
        One in 5 times, reindeers refuse to work. This simulated by picking a random number
        :return:
        """
        random_number = random.randint(0, 4)
        acknowledgment = False
        if random_number > 0:
            print('Delivery started')
            counter = 1
            while not self.sled.is_empty():
                print(
                    f'Present number {counter} is being delivered'
                    f', It will take {self.TIME_TO_DELIVER_PER_PRESENT} seconds'
                )
                sleep(self.TIME_TO_DELIVER_PER_PRESENT)
                self.sled.remove_present()
                counter = counter+1
                print('Delivered')
            acknowledgment = True
        else:
            print('The reindeers are hungry :/')

        return acknowledgment


