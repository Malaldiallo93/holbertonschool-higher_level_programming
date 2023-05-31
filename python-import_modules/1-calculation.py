#!/usr/bin/python3
from calculator_1 import add, subtract, multiply, divide
a = 10
b = 5

somme = add(a, b)
difference = subtract(a, b)
produit = multiply(a, b)
quotient = divide(a, b)

print("Résultats des opérations :")
print("Somme de {} et {} = {}".format(a, b, somme))
print("Différence entre {} et {} = {}".format(a, b, difference))
print("Produit de {} par {} = {}".format(a, b, produit))
print("Quotient de {} par {} = {}".format(a, b, quotient))
