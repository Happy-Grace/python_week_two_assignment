# Create an empty list called my_list.
# Append the following elements to my_list: 10, 20, 30, 40.
# Insert the value 15 at the second position in the list.
# Extend my_list with another list: [50, 60, 70].
# Remove the last element from my_list.
# Sort my_list in ascending order.
# Find and print the index of the value 30 in my_list.


# 1) An empty list
my_list = list()
# Verify the list is created and empty
print(f'\nThe empty list: {my_list}.')
print(f"List created successfully: {type(my_list)}.\n")



# 2) Appending elements to the list.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Items added to the list.
print(f"List with added items: {my_list}.\n")

# 3) Insert the value 15 at the second position(index of 1) in the list.
my_list.insert(1, 15)

print(f"The value 15 inserted successfully: {my_list}.\n")


# 4) Extend my_list with another list: [50, 60, 70].
# Created a new list  to be extended.
new_list = [50, 60, 70]
my_list.extend(new_list)

print(f"New list extended successfully: {my_list}.\n")


# 5) Remove the last element from my_list.
my_list.pop()

print(f"Last element removed successfully: {my_list}.\n")


# 6) Sort my_list in ascending order.
# I'd reverse my list, to show the sort() method works.
my_list.reverse()
print(f"Reversed List: {my_list}.\n")

my_list.sort()
print(f"Sorted List: {my_list}.\n")


# 7) Find and print the index of the value 30 in my_list.

print(f"Index of the value 30: {my_list.index(30)}.\n")
