# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. 
# Think of five simple foods, and store them in a tuple.
foods = ('dim sums', 'hot and sour soup', 'quick noodles', 
         'szechwan chilli chicken', 'spring rolls')

# Use a for loop to print each food the restaurant offers.
for food in foods:
    print(food.title())

# Try to modify one of the items, and make sure that Python rejects the 
# change.
#foods[0] = 'stir fried tofu with rice'

# The restaurant changes its menu, replacing two of the items with 
# different foods. Add a block of code that rewrites the tuple, and 
# then use a for loop to print each of the items on the revised menu.
foods = ('dim sums', 'hot and sour soup', 'quick noodles', 
         'stir fried tofu with rice', 
         'shitake fried rice with water chestnuts')
for food in foods:
    print(food.title())