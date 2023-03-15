#!/usr/bin/env python3

class CashRegister:
    
  def __init__(self, discount=0):
    self.discount=discount
    self.total=0
    self.last_transaction=0
    self.items=[]

  def apply_discount(self):
    if self.discount>0:
      self.total=self.total*((100-self.discount)/100)

      print(f"After the discount, the total comes to ${self.total:.0f}.")
    else:
      print("There is no discount to apply.")

  def add_item(self, item, price, quant=1):
    self.last_transaction=price*quant
    self.total+=self.last_transaction
    for x in range(quant):
      self.items.append(item)

  def void_last_transaction(self):
    self.total-=self.last_transaction


cash=CashRegister(10)
cash.add_item("orange", 1)
cash.add_item("apple", 1, 3)
cash.add_item("milk",4)
cash.add_item("paper towels", 3, 2)

cash.apply_discount()

