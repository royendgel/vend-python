import requests


class Vend:
    def __init__(self, company_name, access_token):
        self.company_name = company_name
        self.access_token = access_token
        self.base_url = "https://{}.vendhq.com/api".format(self.company_name)
        self.__params = {}
        self.data = []

    def __headers(self):
        return {'Authorization': 'Bearer {}'.format(self.access_token)}

    def __build_build_url(self, endpoint):
        return "{}/{}".format(self.base_url, endpoint)

    def __build_get_request(self, endpoint):
        url = self.__build_build_url(endpoint)
        try:
            response = requests.get(url, headers=self.__headers(), params=self.__params)
            if response.status_code != 200:
                raise AssertionError()

            json_response = response.json()
            return json_response
        except Exception as e:
            # FIXME handle this
            return None

    def __get_response(self, endpoint):
        response = self.__build_get_request(endpoint=endpoint)
        return self.process_get_response(response=response, endpoint=endpoint)

    def process_get_response(self, response, endpoint):
        if 'pagination' in response:
            self.pages = response['pagination']['pages']
            self.page = response['pagination']['page']
            self.data += response[endpoint]

            if self.page < self.pages:
                self.page += 1
                self.__params.update({'page': self.page})
                self.__get_response(endpoint)

        else:
            return response[endpoint]

        return self.data

    def add_customer(self):
        return self.__build_post_request('customers', data=data)

    def add_product(self):

        return self.__build_get_request('products', data=data)

    def get_products(self):

        return self.__get_response(endpoint='products')

    def get_customers(self):
        return self.__build_get_request('customers')

    def get_one_customer(self):
        pass

    def get_one_product(self):
        pass

    def get_sales(self):
        # https://developers.vendhq.com/documentation/api/0.x/register-sales.html
        # in the documentation: Dont rely on being able to get all the register sales for a retailer in a single API call.
        return self.__get_response(endpoint='register_sales')

    def get_sale(self):
        # https://developers.vendhq.com/documentation/api/0.x/register-sales.html
        # in the documentation: Dont rely on being able to get all the register sales for a retailer in a single API call.
        return self.__get_response(endpoint='register_sales')


"""
Stock Control
Customers
Outlets
Payment Types
Products
Register Sales
Registers
Suppliers
Taxes
Users
Webhooks
"""
