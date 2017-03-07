VEND PYTHON
===========

### My intend to migrate my private repo to opensource and public

###Installation
`pip install vendpos`
clone/download this project
python setup.py install
 


##Usage

### initialize

You need an access token , you can use oath or get an personal token in vend ( setup -> Personal tokens)

```python
from vend import Vend
vend = Vend(company_name=company_name)
```

## Customers

### get list of customers
`customers = vend.get_customers()`
 
### get one customer
`customer = vend.get_customer(id)`

### add customer
 ```python
customer = vend.add_customer({})
 ```
 

## Products

### get list of products
`products = vend.get_products()`
 
### get one product
`product = vend.get_product(id)`

### add product
 ```python
product = vend.add_product({})
 ```
 

## Register Sales

### get list of sales
`sales = vend.get_sales()`
 
### get one sale
`sale = vend.get_sale(id)`

### add sale
 ```python
sale = vend.add_sale({})
 ```
 


### What works ?
- customer list
- one customer
- product list
- one product
- sales list
- one sale
- tests 

TODO: 

- Stock Control
- Customers
- Outlets
- Payment Types
- Products
- Register Sales
- Registers
- Suppliers
- Taxes
- Users
- Webhooks
- django integration (maybe separate package)
 