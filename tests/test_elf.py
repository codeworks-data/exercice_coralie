import unittest
from presents_distributing_lib import Elf, TooMuchWorksError


class ElfTest(unittest.TestCase):

    def test_work_is_done_initialized_false(self):
        sample_elf = Elf()
        self.assertEqual(sample_elf.is_done_working, False)

    def test_notify_work_is_done(self):
        sample_elf = Elf()
        sample_elf.notify_work_done()
        self.assertTrue(sample_elf.is_done_working)

    def test_no_exception_when_not_done_working(self):
        sample_elf = Elf()
        sample_elf.is_done_working = False
        raised = False
        try:
            sample_elf.wrap_present(2)
        except:
            raised = True
        self.assertFalse(raised, 'Exception raised')

    def test_exception_when_done_working(self):
        sample_elf = Elf()
        sample_elf.is_done_working = True
        self.assertRaises(TooMuchWorksError, sample_elf.wrap_present, 1)

