#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0, total = 0):
    self.discount = discount
    self.total = total
    self.items = []
    
  def add_item(self, title, price, quantity = 1):
    self.quantity = quantity
    self.price = price
    self.total += price * quantity
    for _ in range(quantity):
      self.items.append(title)
    
  def apply_discount(self):
    self.total -= self.discount/100 * self.total
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      print(f"After the discount, the total comes to ${int(self.total)}.")
    
  def void_last_transaction(self):
    self.total -= self.price * self.quantity
    
