"""Test teacher cases."""
import unittest
from test_case.models.driver import chrome
from test_case.models.function import login_bigben


class TeacherTest(unittest.TestCase):
    """Prepare for teacher test."""

    def setUp(self):
        """Prepare driver and login as teacher."""
        self.driver = chrome()
        login_bigben(self.driver, "educator-1", "xxxxx")

    def tearDown(self):
        """Quit driver (close browser)."""
        self.driver.quit()
