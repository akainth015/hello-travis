import unittest

from app import get_startup_message

class TestStartup(unittest.TestCase):
    def test_message(self):
        assert get_startup_message() == "Our app is running"


if __name__ == "__main__":
    unittest.main()

