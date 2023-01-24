import priceCheck
import recursiveDigitSum
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(priceCheck.price_check(products=['eggs', 'milk', 'cheese'],
productPrices=[2.89, 3.29, 5.79],
productSold=['eggs', 'eggs', 'cheese', 'milk'],
soldPrice=[2.89, 2.99, 5.97, 3.29]
), 2)

    def test2(self):
        self.assertEqual(priceCheck.price_check(products=['rice', 'sugar', 'wheat', 'cheese'],
	productPrices=[16.89, 56.92, 20.89, 345.99],
	productSold=['rice', 'cheese'],
	soldPrice=[18.99, 400.89]), 2)

    def test3(self):
        self.assertEqual(recursiveDigitSum.recursive_sum_of_digits(2347623),27)

if __name__ == '__main__':
    unittest.main()
