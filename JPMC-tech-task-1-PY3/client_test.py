import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))


  """ ------------ Add more unit tests ------------ """

  def testing_getRatio_priceA0(self):
    price_a = 0
    price_b = 120.3
    self.assertEqual(getRatio(price_a, price_b), 0)

  def testing_getRatio_priceB0(self):
    price_a = 121.2
    price_b = 0
    self.assertIsNone(getRatio(price_a, price_b))

  def testing_getRatio_greater_than_1(self):
    price_a = 412.47
    price_b = 186.39
    self.assertGreater(getRatio(price_a, price_b), 1)

  def testing_getRatio_less_than_1(self):
    price_a = 186.39
    price_b = 412.47
    self.assertLess(getRatio(price_a, price_b), 1)

  def test_getRatio_exactly_1(self):
    price_a = 412.47
    price_b = 412.47
    self.assertEqual(getRatio(price_a, price_b), 1)
    
       
if __name__ == '__main__':
    unittest.main()
