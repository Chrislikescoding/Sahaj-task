# from unittest import TestCase, main # for all examples
import unittest
from create_order import Order
from product_order import ProductOrder


class TestOrder(unittest.TestCase):
# 1 create an order -
    def test_create_order(self):
        test_order = Order('DRAFT', 0)
        self.assertTrue(test_order.create_order('DRAFT', 0))
# should have an order 1 but no Python course

    def test_product_order_1(self):
        test_product_order = ProductOrder(1, ' ', 2)
        self.assertFalse(test_product_order.create_product_order(1, 'Python Course', 2))

# assuming we won't have an order 99 as it's a lot of test data to enter

    def test_product_order_2(self):
        test_product_order = ProductOrder(99, ' ', 2)
        self.assertFalse(test_product_order.create_product_order(99, 'dog biscuits', 2))
# assuming we will have an order 1 and product eggs

    def test_product_order_3(self):
        test_product_order = ProductOrder(1, ' ', 2)
        self.assertTrue(test_product_order.create_product_order(1, 'eggs', 12))


if __name__ == '__main__':
    unittest.main()
