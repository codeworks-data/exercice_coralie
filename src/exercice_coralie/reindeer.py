import random
from time import sleep


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


