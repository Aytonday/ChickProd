from products import Product;
import json
from pprint import pprint

def loadandextractProducts ():
    # Open the Product file and load in its contents into 'data'.
    with open('ProductList.json') as productList:
        data = json.load(productList)

    print(data)
    ProductListProduced = []
    for i in data:
        x=0
        name = data['productList'][x]["name"]
        maxK = data['productList'][x]['maxKanban']
        maxPK = data['productList'][x]['maxPerKanban']
        proportions = data['productList'][x]['proportions']
        print(proportions)
        print(type(proportions))
        ProductListProduced.append(Product(name,maxK, maxPK))
        x+=1

loadandextractProducts()