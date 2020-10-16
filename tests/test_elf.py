import unittest
from exercice_coralie import Elf, TooMuchWorksError


class ElfTest(unittest.TestCase):

    def test_work_is_done_initialized_false(self):
        sample_elf = Elf()
        self.assertEqual(sample_elf.is_done_working, False)

    def test_notify_work_is_done(self):
        sample_elf = Elf()
        sample_elf.notify_work_done()
        self.assertEqual(sample_elf.is_done_working, True)

    def test_wrap_when_sled_empty(self):
        sample_elf = Elf()
        sample_elf.is_done_working = False
        raised = False
        try:
            sample_elf.wrap_present(2)
        except:
            raised = True
        self.assertFalse(raised, 'Exception raised')

    def test_dont_wrap_when_sled_full(self):
        sample_elf = Elf()
        sample_elf.is_done_working = True
        self.assertRaises(TooMuchWorksError, sample_elf.wrap_present, 1)

