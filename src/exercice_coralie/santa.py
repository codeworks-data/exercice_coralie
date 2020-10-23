import random

from .elf import Elf
from .reindeer import Reindeer

PRESENT_SIZES = [1, 2, 5]


class Santa(object):
    """
    Santa has for role to deliver an 'n' number of presents, by orchestrating the work with the elves and reindeers
    """
    def __init__(self, number_of_presents: int):
        self.presents_queue = random.choices(PRESENT_SIZES, k=number_of_presents)
        self.elf = Elf()

    def distribute_presents(self):
        """
        Distribute the presents present in the queue
        :return: None
        """
        while len(self.presents_queue):

            current_present = self.presents_queue[0]
            del self.presents_queue[0]
            print(f'Processing present of size: {current_present} Kg(s)')

            present_to_add = self.elf.can_add_present(current_present)
            if present_to_add:
                self.elf.wrap_present(current_present)
            if (not present_to_add) or (not len(self.presents_queue)):
                self.elf.notify_work_done()
                sled = self.elf.get_sled()
                sled.set_status('delivering')
                reindeer = Reindeer(sled)
                acknowledgment = reindeer.deliver_presents()
                # If the reindeer refuse to work ask them again
                while not acknowledgment:
                    acknowledgment = reindeer.deliver_presents()
                del reindeer
                self.elf = Elf()
