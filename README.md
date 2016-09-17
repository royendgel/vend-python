VEND PYTHON
===========

### My intend to migrate my private repo to opensource and public

###Installation
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
`customer = vend.get_customer()`

### add customer
 ```python
customer = vend.add_customer({})
 ```


### What works ?
- customer list
- product list 

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
 