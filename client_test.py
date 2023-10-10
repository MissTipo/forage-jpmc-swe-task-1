import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        self.assertEqual(getDataPoint(quotes[0]), (quotes[0]['stock'], quotes[0]['top_bid']['price'],
                         quotes[0]['top_ask']['price'], (quotes[0]['top_bid']['price']+quotes[0]['top_ask']['price'])/2))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        self.assertEqual(getDataPoint(quotes[0]), (quotes[0]['stock'], quotes[0]['top_bid']['price'],
                         quotes[0]['top_ask']['price'], (quotes[0]['top_bid']['price']+quotes[0]['top_ask']['price'])/2))

    """ ------------ Add more unit tests ------------ """

    def test_getRatio_calculateRatio(self):
        prices = [
            {'price_a': 119.2, 'price_b': 120.48},
            {'price_a': 121.68, 'price_b': 117.87}
        ]
        self.assertEqual(getRatio(
            prices[0]['price_a'], prices[0]['price_b']), prices[0]['price_a']/prices[0]['price_b'])

    def test_getRatio_calculateRatioPriceBZero(self):
        prices = [
            {'price_a': 119.2, 'price_b': 0},
            {'price_a': 121.68, 'price_b': 117.87}
        ]
        self.assertEqual(
            getRatio(prices[0]['price_a'], prices[0]['price_b']), None)


if __name__ == '__main__':
    unittest.main()
