# python standard library: collection of modules

# import pizza
# from pizza import make_pizza, display_pizza_menu
# from pizza import *  # import all functions


# from pizza import make_pizza
# from pizza import display_pizza_menu as menu

# to avoid namespace conflict

import pizza as p

p.display_pizza_menu()
p.make_pizza("Large", "Tomato", "Olives", "Onion")

p.make_pizza("Small",
             "Mushroom",
             "Olives",
             "Onion")

# -------------
# general syntax
# import module_name as mn
#
# variables: lowercase underscore
# functions: lowercase, underscore
#

