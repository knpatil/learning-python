"""
This is a python module
    It is just a collection of related functions
"""

def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested"""
    print(f"Creating pizza of size: {size}")
    print(f"\t with toppings: {toppings}")

def display_pizza_menu():
    print("We make Large, Medium, Small size pizzas.")
    print("Menu: ")
    print("-----")
    print("\t\tVeggie Delight")
    print("\t\tPaneer Pizza")
    print("\t\tCombo Pizza")
    print("-" * 40)

