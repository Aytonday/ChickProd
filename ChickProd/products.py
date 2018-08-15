class Product:
    def __init__(self,prodName, maxKanban, maxPerKanban, **proportions):
        self.prodName = prodName
        self.maxKanban = maxKanban
        self.maxPerKanban = maxPerKanban
        self.proportions = proportions

    def maxProdtobeMade (self):
        max = self.maxKanban * self.maxPerKanban
        return max