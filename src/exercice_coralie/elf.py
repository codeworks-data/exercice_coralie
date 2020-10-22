from time import sleep

from sled import Sled
from exceptions import TooMuchWorksError


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
        print('Sled: Hey elf! The sled is full! Bravo!')
        self.is_done_working = True


