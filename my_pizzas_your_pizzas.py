# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 
# 4-1 (page 60). Make a copy of the list of pizzas, and call it 
# friend_pizzas. Then, do the following:
pizzas = ['neopolitan style pizza', 'new haven style apizza', 
          'grandma style pizza', 'new york style pizza', 'pan style pizza']
for pizza in pizzas:
    print(pizza.title())

for pizza in pizzas:
    print("I like " + pizza.title() + "!\n")

print("I LOVE PIZZA!")

friend_pizzas = pizzas[:]

# Add a new pizza to the original list.
pizzas.append('montanara style pizza')

# Add a different pizza to the list friend_pizzas.
friend_pizzas.append('sicilian style pizza')

# Prove that you have two separate lists. Print the message, My 
# favorite pizzas are:, and then use a for loop to print the first 
# list. Print the message, My friend’s favorite pizzas are:, and then 
# use a for loop to print the second list. Make sure each new pizza is 
# stored in the appropriate list.
print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())