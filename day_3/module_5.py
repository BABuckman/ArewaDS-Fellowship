# Level 1
list1 = list()    # empty list 
list2 = ['Kwame', 200, 'Computer science', 3.4, 3.81,'Physical Science', 'UCC']
print(len(list2))       # get lenght of the list
print(len(list1)-1)     # last item 
print(list2[int(len(list2)/2)])        # middle item
print(list2[0])                         # first item 

mixed_data_types = ['Bernard', 19, 'Single', 'Amanfrom Rd., Accra, Ghana']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']

print(mixed_data_types)
print(it_companies)

print('First item: ' + mixed_data_types[0])
print('Middle item: ' + mixed_data_types[int(len(mixed_data_types)/2)])
print('Last item: ' + mixed_data_types[len(mixed_data_types)-1])

# Modify the company list
it_companies[0] = 'Telegram'
print(it_companies)

# Adding an IT company
it_companies.append('Facebook')
print(it_companies)

# Insert an item in the middle 
it_companies.insert(int(len(it_companies)/2),'Meta')
print(it_companies)

n = 0
# Change the names to uppercase
while n < len(it_companies):
    it_companies[n] = it_companies[n].upper()
    n = n + 1

print(it_companies)

# Check if a certain company exists
item = 'Facebook'
txt1 = '{} exists in the list.'
txt2 = '{} does not exist in the list.'

if item in it_companies:
    print(txt1.format(item))
else:
    print(txt2.format(item))

# Sort the list
print(it_companies.sort())

# Reverse list items 
print(it_companies.sort(reverse=True))
print(it_companies.reverse())

# Slice out the first 3 companies from the list
print(it_companies[0:3])

# Slice out the last 3 companies from the list 
print(it_companies[-4:-1])

# Slice out the middle IT company or companies from the list
print(it_companies[int(len(it_companies)/2)])

# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

print(front_end.extend(back_end))


