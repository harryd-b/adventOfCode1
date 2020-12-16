import unittest
from Util.file import load_file_to_list


class MyTestCase(unittest.TestCase):
    def test_something(self):
        passport_map = []
        load_file_to_list('../venv/Include/ppt.txt', passport_map)
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
