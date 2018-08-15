from products import Product;
import json

ProductListProduced = []

# This function loads in the settings and contents of the products from a JSON file.
# It puts each section (Name, Max Kanban Number, Max Per Kanban Number, Proportions List,
# and Ingredients List) into respective list for each product. Then it creates objects
# per Product containing relvent information pertaining to it.
def loadandextractProducts():
    # Open the Product file and load in its contents into 'data'.
    with open('ProductList.json', 'r') as productList:
        data = json.load(productList)
    name = []
    maxK = []
    maxPK = []
    proportionsList = []
    ingredientsList = []
    ListofDict = []
    x = 0
    t = 0
    for i in data["productList"]:
        proportionsList.clear()
        ingredientsList.clear()
        name.append(data['productList'][x]["name"])
        maxK.append(data['productList'][x]['maxKanban'])
        maxPK.append(data['productList'][x]['maxPerKanban'])
        y = len(data['productList'][x]['proportions'])
        for r in range(y):
            proportionsList.append(data['productList'][x]['proportions'][r])
            ingredientsList.append(data['productList'][x]['ingredients'][r])
            t += 1
        dicti = getIngredientsandProportions(proportionsList, ingredientsList)
        ListofDict.append(dicti)
        x += 1
    t = len(name)
    ProductListProduced = [Product(name[x], maxK[x], maxPK[x], ListofDict[x], x) for x in range(t)]


# Takes in the proportion numbers and matches it with Ingredients in a Dictionary
def getIngredientsandProportions(proportions, ingredients):
    returndict = dict(zip(ingredients, proportions))
    return returndict


loadandextractProducts()
