import unittest
 
class TestNumber(unittest.TestCase):   

   def test_add(self):
       self.assertEqual(1 + 2, 3)
       self.assertEqual(6 + 6, 12)

   def test_sub(self):
       self.assertEqual(1 - 2, -1)
       self.assertEqual(4 - 2, 2)
       
   def test_Multiply(self):
       self.assertEqual(1 * 1, 1)
       self.assertEqual(9 * 8, 72)

   def test_divide(self):
       self.assertEqual(6 / 3, 2)
       self.assertEqual(2 / 2, 1)
 
if __name__ == '__main__':
   unittest.main()
