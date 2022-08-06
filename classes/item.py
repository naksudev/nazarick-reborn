""" 
<- Rarity of items ->
- Legendary
- Super Rare
- Rare
- Uncommon
- Common
"""

class Item:
    def __init__(self, name, description, rarity, quantity = 1):
        self.name = name
        self.description = description
        self.rarity = rarity
        self.quantity = quantity

dragonTooth = Item( 'Dragon\'s Tooth', 
                    'A sharp tooth taken from a dragon.\n\n+20 ATK', 
                    'Super Rare' )