class RestaurantTable:

    menus = {
        'pizza' : 5000,
        'cola' : 600,
        'apple juice' : 2000,
        'humburger' : 1500,
        'french fries' : 3000
    }

    def __init__(self) :
        self.total = 0
        self.orders = []

    def addOrder(self,order) :
        self.orders.append(order)
        self.total += self.menus[order]
        # print(f'{self.menus} self-order')
        # print(order)

    def printBill(self) :
        for order in self.orders :
            print(f'{order} : {self.menus[order]}$')
    
        print(f'total price is {self.total}$')


def StartProgram() :
    table = RestaurantTable() 

    while True :
        order = input('order :')
        table.addOrder(order)

        another = input('order more? y/n: ')
        if another == 'y' :
            continue
        else :
            table.printBill()
            break

StartProgram()