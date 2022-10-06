from audioop import reverse
from pyexpat import model


guitars = [
    {'model':'sdr13','price':300},
    {'model':'ss13','price':4000},
    {'model':'sop13','price':9008},
    {'model':'ssssss13','price':204}
]
print(sorted(guitars ,key = lambda i:i['price'],reverse=True))