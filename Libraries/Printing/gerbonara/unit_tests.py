import unittest
from gerbonara import LayerStack

# https://gerbolyze.gitlab.io/gerbonara/


class UnitTests(unittest.TestCase):
    # ok
    def test_Basic_operations(self):
        print('test_Basic_operations')

        stack = LayerStack.from_directory('gerber')
        w, h = stack.outline.size('mm')
        print(f'Board size is {w:.1f} mm x {h:.1f} mm')


if __name__ == '__main__':
    unittest.main()
