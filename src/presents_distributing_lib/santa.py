import random

from .elf import Elf
from .reindeer import Reindeer
from .constants import PRESENT_SIZES


class Santa:
    """
    Santa has for role to deliver an 'n' number of presents, by orchestrating the work with the elves and reindeers
    """
    def __init__(self, number_of_presents: int):
        self.presents_queue = random.choices(PRESENT_SIZES, k=number_of_presents)
        self.elf = Elf()
        self.reindeer = Reindeer()

    def add_more_presents(self, number_of_presents: int):
        """
        Add more presents to presents' queue of
        """
        random_presents_weights_to_add = random.choices(PRESENT_SIZES, k=number_of_presents)
        self.presents_queue.extend(random_presents_weights_to_add)

    def distribute_presents(self):
        """
        Distribute the presents present in the queue
        :return: None
        """
        while self.presents_queue:

            current_present = self.presents_queue.pop(0)
            print(f'Processing present of size: {current_present} Kg(s)')

            can_add_current_present = self.elf.can_add_present(current_present)
            if can_add_current_present:
                self.elf.wrap_present(current_present)
            if (not can_add_current_present) or (not len(self.presents_queue)):
                self.elf.notify_work_done()
                sled = self.elf.get_sled()

                self.reindeer.set_sled(sled)
                acknowledgment = self.reindeer.deliver_presents()
                # If the reindeer refuse to work ask them again
                while not acknowledgment:
                    acknowledgment = self.reindeer.deliver_presents()

                self.elf.put_back_to_work()

                # Add the present that couldn't be added
                if not can_add_current_present:
                    self.elf.wrap_present(current_present)
