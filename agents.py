import random
from abygame import AbygameAgent

class Agent(AbygameAgent):
    def __init__(self, goods, money, utility, i, name):
        super().__init__(goods, money, i, name)
        self.goods = goods 
        self.money = money
        self.utility = utility

    def makes_an_offer(self):
        if self.goods  > 0 :
            offer_price = max(0, self.utility + random.gauss(0, 1))
            return offer_price
        else:
            return None
    
    def accepts_or_rejects_offer(self, price):
        if price < self.utility and price < self.money:
            self.goods += 1
            self.money -= price
            return 1  # how much I buy
        else:
            return 0
    
    def delivers(self, quantity, offer_price):
        self.goods -= quantity
        self.money += offer_price * quantity

    def __repr__(self):
        return f'goods: {self.goods}, money: {self.money}, utility: {self.utility} '