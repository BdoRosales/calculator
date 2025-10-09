"""Functions to keep track of and alter an inventory."""

def create_inventory(items):
    """Create an inventory dictionary from a list of items."""
    inventory = {}
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


def add_items(inventory, items):
    """Add a list of items to the existing inventory."""
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


def decrement_items(inventory, items):
    """Decrement items in the inventory, but not below zero."""
    for item in items:
        if item in inventory:
            inventory[item] = max(0, inventory[item] - 1)
    return inventory


def remove_item(inventory, item):
    """Remove an item entirely from the inventory if it exists."""
    inventory.pop(item, None)  # No error if item doesn't exist
    return inventory


def list_inventory(inventory):
    """Return a list of (item, quantity) tuples for items with quantity > 0."""
    return [(item, inventory[item]) for item in inventory if inventory[item] > 0]

    
