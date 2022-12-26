"""
December 2022
Project: sprouts
Author: Leonard Vaughn (@aqualen)
"""

import unittest


class TestMyClass(unittest.TestCase):
    def test_serial_to_msg(self):
        # serial.readline returns a byte-string, b'blah blah' which strip doesn't understand.
        readline_result = b'[Greenhouse.Temperature] 71.9059982299\r\n'
        # use decode('ASCII') to 'convert' to python str class, and voilà! the crap goes away
        # when strip() is called.
        msg = readline_result.decode('ASCII').strip()
        print(msg)
        self.assertEqual("[Greenhouse.Temperature] 71.9059982299", msg)  # add assertion here


if __name__ == '__main__':
    unittest.main()
