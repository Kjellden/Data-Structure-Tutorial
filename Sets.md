# Python Data Structure Queues
## what is a Set
Unlike other storage type data structures such as lists, stacks, and queues a set is a data structure where order is not important to the end goal.

1. #### specialties with sets
Along with not needing to worry about order when working with sets you also don't have to worry about having duplicate information because the way sets store information don't allow for duplicates. This ability of not needing order or not being able to store duplicate information allows us to find if information is in the set or not. We find an item where an item and store items in a set using a technique called hashing.

2. #### Hashing
To be able to get O(1) time with sets we must use hashing. Assume we wanted to store crayons we could store each color as a value or index in the set. The function would look like this index(color) = color so in simple terms we could see it like this.

blue -> hash -> 0
green -> hash -> 1
red -> hash -> 3
purple -> hash -> 2
[blue, green, red, purple]

check if something is in the set
 
green -> hash -> 0 set[0] == green so true
orange -> hash -> 5 set[5] == none so false

so if we wanted to find if purple was in the set we could check to see if there was an item in that hash location because hash index's are made for each item. This way of encoding index allows you to perform O(1) because you no longer have to search the full list you only need to check the hash index for the item your looking for.

## commands and Big O
Operation | Description | Code | Performance
-------- | -------- | --------|--------|
add(value)| Add a value to the set | my_set.add(value)| O(1)|
remove(value)| Removes value from the set | my_set.remove(value)| O(1)|
member(value)| checks to see if value is in the set | if value in set | O(1)
size()| check the size of the set | len(my_set) }| O(1)

## example code
```python
# make an empty set
my_set = set()

# add an item to the set
my_set.add(5)
my_set.add(6)
my_set.add(5)

# print out the set
print(my_set)  # {5, 6}

# remove from set 
my_set.remove(5)

# check to see if an item is in the set
value = 5
if value in my_set:
    print("yes")
else:
    print("no")

value = 6
if value in my_set:
    print("yes")
else:
    print("no")

# hwo big is the set
print(len(my_set))
```

## Problem