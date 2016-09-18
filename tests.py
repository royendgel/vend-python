from vend import Vend
import os

from unittest import TestCase
import unittest


class TestVendSuite(TestCase):
    def setUp(self):
        token = os.getenv('VENDTOKEN')
        company_name = os.getenv('VENDCOMPANY')
        self.vend = Vend(company_name=company_name, access_token=token)
        self.one_customer_id = self.vend.get_customers()

    def test_list_product(self):
        # there need to be more then one product
        products = self.vend.get_products()
        self.assertGreater(len(products), 1)

    def test_one_product(self):
        pass

    def test_add_product(self):
        pass

    def test_list_customer(self):
        # there need to be more then one customer
        customers = self.vend.get_customers()
        self.assertGreater(len(customers), 1)

    def tes_one_customer(self):
        customer = self.vend.get_customer(self.one_customer_id)

    def test_add_cutsomer(self):
        pass

    def test_list_sales(self):
        # there need to be more then one sale
        sales = self.vend.get_sales()
        self.assertGreater(len(sales), 1)

    def tes_one_sale(self):
        pass

    def test_add_sale(self):
        pass


if __name__ == '__main__':
    unittest.main()
