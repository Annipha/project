'''
Python Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''

'''
BASIC LEVEL
PART 1: Read in the file with csv.reader() and store it in an object called 'file_nested_list'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
      https://docs.python.org/2/library/csv.html
'''

import csv

file_nested_list = []

with open('chipotle.tsv', 'rb') as tsvfile:
    tsvfile = csv.reader(tsvfile, delimiter ='\t')
    for row in tsvfile:
        file_nested_list.append(row)

    
       

    

# specify that the delimiter is a tab character
# make 'file_nested_list' = list of rows



'''
BASIC LEVEL
PART 2: Separate 'file_nested_list' into the 'header' and the 'data'.
'''

header = []
header.append(file_nested_list[0])

data = [] 
for row in file_nested_list[1:]:
    data.append(row)

                     


'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!
'''
lastseen_order = []
for orders in data:
    if (orders[0] in lastseen_order)==False:
        lastseen_order.append(orders[0])
        

#lastseen_order = 0
#for orders in data: 
#    if orders[0] != lastseen_order: 
#        lastseen_order = orders[0]

list_price = []
for price in data: 
    list_price.append(price[4])

sum = 0
for price in list_price:
    new_price = price[1:4]
    sum = sum + float(new_price)

answer = sum/float(len(lastseen_order))
new_answer = str(round(answer, 2))
print new_answer

# count the number of unique order_id's
# note: you could assume this is 1834 since that's the maximum order_id, but it's best to check

# create a list of prices
# note: ignore the 'quantity' column because the 'item_price' takes quantity into account
# strip the dollar sign and trailing space

# calculate the average price of an order and round to 2 digits
# $18.81


'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''

# if 'item_name' includes 'Canned', append 'choice_description' to 'sodas' list
sodas = []
for soda in data: 
    if 'Canned' in soda[2] and ((soda[3] in sodas)==False):
        sodas.append(soda[3])

# equivalent list comprehension (using an 'if' condition)

sodas_list = [soda[3] for soda in data if 'Canned' in soda[2]]



# create a set of unique sodas



'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''

# keep a running total of burritos and toppings
burritos = 0
for burrito in data:
    if 'Burrito' in burrito[2]:
        burritos = burritos+1

print burritos

    

# calculate number of toppings by counting the commas and adding 1
# note: x += 1 is equivalent to x = x + 1
sum_toppings = 0
for topping in data:
    if 'Burrito' in topping[2]:
        sum_toppings += int(topping[3].count(','))+1
print sum_toppings
    
                                      

# calculate the average topping count and round to 2 digits
# 5.40

avr_topping = float(sum_toppings)/float(burritos)
print round(avr_topping,2)


                                      
'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''

# start with an empty dictionary
chips = {}

# if chip order is not in dictionary, then add a new key/value pair
for chip in data:
    if 'Chips' in chip[2] and ((chip[2] in chips) == false):
        chips[chip[2]] = int(chip[1])
        
# if chip order is already in dictionary, then update the value for that key
    if chip[2] in chips:
        chips[chip[2]] += int(chip[1])

       
        

# defaultdict saves you the trouble of checking whether a key already exists



'''
BONUS: Think of a question about this data that interests you, and then answer it!
'''
