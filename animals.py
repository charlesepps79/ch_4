# 4-2. Animals: Think of at least three different animals that have a 
# common characteristic. Store the names of these animals in a list, 
# and then use a for loop to print out the name of each animal.
animals = ['bats', 'birds', 'bugs']
for animal in animals:
    print(animal)

# Modify your program to print a statement about each animal, such as 
# A dog would make a great pet.
for animal in animals:
    print(animal.title() + " can fly.\n")

# Add a line at the end of your program stating what these animals have 
# in common. You could print a sentence such as Any of these animals 
# would make a great pet!
print("Because they all have wings.")