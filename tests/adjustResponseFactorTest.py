import unittest
import pathlib
import sys

# importing parseCsvShimadzu  
sys.path.append('../src')
from adjustResponseFactor import adjustResponseFactor

# test data
file_path='data/ghana/calibration/K.csv'
file_content = pathlib.Path(file_path).read_text()

a=adjustResponseFactor(file_content)
print(a)


"""
class Test_parseCsvShimadzu(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(parseCsvShimadzu(file_content)['sample'],"AFR390")

    def test_current(self):
        self.assertEqual(parseCsvShimadzu(file_content)['current'],1000)

    def test_livetime(self):
        self.assertEqual(parseCsvShimadzu(file_content)['livetime'],959)

if __name__ == '__main__':
    unittest.main()
"""
