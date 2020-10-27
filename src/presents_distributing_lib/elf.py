from time import sleep

from .sled import Sled
from .exceptions import TooMuchWorksError
from .constants import WEIGHT_TO_WRAPPING_TIME


class Elf:
    """
    The elf has for role to wrap the presents and fill put them in the sled
    """
    def __init__(self):
        self.is_done_working = False
        self.sled = Sled()

    def can_add_present(self, present_weight: int):
        """
        Check if a present can be added to the sled
        :param present_weight: int, the wieght of the present
        :return: bool, True if there is remaining space in the sled
        """
        return self.sled.can_add_present(present_weight)

    def wrap_present(self, present_weight: int):
        """
        Wrap present and add it to the sled. Time it takes to wrap a present depends on it's weight.
        :param present_weight: int, the weight of the present
        :return: None
        """
        if self.is_done_working:
            raise TooMuchWorksError(
                'Calling \'Elf.wrap_present\' is prohibited while \'is_done_working\' is True'
            )
        print(f'Wrapping present of size {present_weight}Kg(s)')
        time_to_wrap = WEIGHT_TO_WRAPPING_TIME[present_weight]
        print(f'Time to wrap: {time_to_wrap}s')
        sleep(time_to_wrap)
        print(f'Present wrapped')
        self.sled.add_present(present_weight)

    def get_sled(self):
        """
        Return the sled being filled by the elf
        :return: Sled, the sled the elf was filling
        """
        return self.sled

    def notify_work_done(self):
        """
        Change the flag for when the elf completed his job on one sled
        :return: None
        """
        print('Sled: Hey elf! The sled is full! Bravo!')
        self.is_done_working = True

    def put_back_to_work(self):
        """
        Change the flag for when the elf completed his job on one sled
        :return: None
        """
        print('The elf is back to work!')
        self.is_done_working = False

