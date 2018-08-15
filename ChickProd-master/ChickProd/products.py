class Product:
    def __init__(self,prodName, maxKanban, maxPerKanban, proportions, id):
        self.prodName = prodName
        self.maxKanban = maxKanban
        self.maxPerKanban = maxPerKanban
        self.proportions = proportions
        self.id = id

    def maxProdtobeMade (self):
        max = self.maxKanban * self.maxPerKanban
        return max

# This is for testing purposes
    def printProduct(self):
        s = [self.prodName, self.maxKanban, self.maxPerKanban, self.proportions]
        for i in s:
            print(i)