import pizza
import pizza as p
from pizza import make_pizza as mp
from pizza import *

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'pepper', 'cheese')

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'pepper', 'cheese')

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'pepper', 'cheese')

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'pepper', 'cheese')
