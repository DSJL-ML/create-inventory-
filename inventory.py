'''
Product Inventory Project - Create an application which manages an inventory of products. 
Create a product class which has a price, id, and quantity on hand.
Then create an inventory class which keeps track of various products and can sum up the inventory value.
(additional requirement: name, sku number, batch number)
'''

class Product(object):
    def __init__(self, name = None, sku_num = None, batch_num = None,
                 unit_cost = None, unit_price = None, batch_quantity = None, receive_date = None):
        self.name = name
        self.sku_num = sku_num
        self.batch_num = batch_num
        self.unit_cost = unit_cost
        self.unit_price = unit_price
        self.batch_quantity = batch_quantity
        self.receive_date = receive_date
        
    def entry(self):
        self.sku_num = input("Enter SKU number: ")
        self.name = input("Enter product name: ")
        self.batch_num = input("Enter batch number: ")
        self.batch_quantity = float(input("Enter batch quantity: "))
        self.unit_cost = float(input("Enter unit cost($): "))
        self.unit_price = float(input("Enter unit price($): "))
        self.receive_date = input("Enter product receiving date(YYYY-MM-DD): ")
        
    def value(self):
        return self.unit_cost*self.batch_quantity

class Inventory(object):

    def __init__(self, product_dict = {}):
        self.product_dict = product_dict
        
    def entry(self, product):
        # Enter product information into inventory
        if product.sku_num not in self.product_dict:
            self.product_dict[product.sku_num] = []
        self.product_dict[product.sku_num].append(product)
            
    def product_num(self):
        # number of products in inventory
        return len(self.product_dict)
    
    def product_list(self):
        # report the list of the products in inventory as a tuple of sku number & sku name
        list_prod = []
        for product in self.product_dict:
            sku_number = self.product_dict[product][0].sku_num
            sku_name = self.product_dict[product][0].sku_name
            if (sku_number, sku_name) not in list_prod:
                list_prod.append(sku_number, sku_name)
            else:
                continue
                
        return list_prod
    
    def value(self):
        # Calculate total inventory value
        value_sum = 0
        for product in self.product_dict:
            for entry in self.product_dict[product]:
                value_sum+=entry.value()
        
        return value_sum
            
    def inventory_report(self):
        list_report = []
        request = input("Enter SKU number: ")
        for entry in self.product_dict[request]:
            list_report.append((entry.sku_num, 
                              entry.name, 
                              entry.batch_num, 
                              entry.batch_quantity,
                              entry.value(),
                              entry.receive_date))
        
        return list_report


import unittest

class Test_Inventory(unittest.TestCase):
    
    def setUp(self):
        self.product_1_B1 = Product('sleep bag','100-1','1709001',10,29.99,100, '2017-10-01')
        self.product_1_B2 = Product('sleep bag','100-1','1710002',10,29.99,50, '2017-10-14')
        self.product_2_B1 = Product('tent','110-22','1701001',25,79.99,250, '2017-03-17')
        self.product_2_B2 = Product('tent','110-22','1705002',25,79.99,110, '2017-06-22')
        self.product_3_B1 = Product('lamp','43-05','1605001',2.25,14.99,700, '2017-06-22')
        self.product_3_B2 = Product('lamp','43-05','1609002',2.25,14.99,900, '2017-08-15')
        self.product_4_B1 = Product('airbed','20-11','1612001',19.80,49.99,400, '2017-02-28')
        self.product_4_B2 = Product('airbed','20-11','1703002',19.80,49.99,800, '2017-05-25')
        self.inventory = Inventory()
        self.inventory.entry(self.product_1_B1)
        self.inventory.entry(self.product_1_B2)
        self.inventory.entry(self.product_2_B1)
        self.inventory.entry(self.product_2_B2)
        self.inventory.entry(self.product_3_B1)
        self.inventory.entry(self.product_3_B2)
        self.inventory.entry(self.product_4_B1)
        self.inventory.entry(self.product_4_B2)

    def test_value(self):
        self.assertEqual(self.inventory.value(), 37860)

    def test_product_num(self):
        self.assertEqual(self.inventory.product_num(), 4)

    def test_inventory_report(self):
        self.assertEqual(self.inventory.inventory_report(),
                         [('100-1','sleep bag','1709001',100,1000,'2017-10-01'),
                          ('100-1','sleep bag','1710002',50,500,'2017-10-14'),
                          ('110-22','tent','1701001',250,6250,'2017-03-17'),
                          ('110-22','tent','1705002',110,2750,'2017-06-22'),
                          ('43-05','lamp','1605001',700,1575,'2017-06-22'),
                          ('43-05','lamp','1609002',900,2025,'2017-08-15'),
                          ('20-11','airbed','1612001',400,7920,'2017-02-28'),
                          ('20-11','airbed','1703002',800,15840,'2017-05-25')])

    def __del__(self):
        pass

    def tearDown(self):
        del self.product_1_B1
        del self.product_1_B2
        del self.product_2_B1
        del self.product_2_B2
        del self.product_3_B1
        del self.product_3_B2
        del self.product_4_B1
        del self.product_4_B2
        del self.inventory
        print("Test objects are deleted!")
                
if __name__ == '__main__':
    unittest.main(verbosity=2)

    
