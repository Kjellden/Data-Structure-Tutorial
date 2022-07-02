# Python Data Structure Queues
## what is a Queue?
A Queue is a line of objects in order. Order is very important when it comes to queues because queues are a list of items waiting to be acted on in the order they are given. 

Queues are all around us in real life but one of the most common queue we see everyday is a line in a shopping center or at the water park. The first person in line is the first person to get picked and the last person goes last and when you want to join the queue you get in the back of the line. The same can go for programing. You can store information and have it wait in a queue to be used later.
## How and when do we use queues?
Queues are used in programing when you don't want something to be over loaded such as a web page or an online game. When to many users try and use one of these it could shut down and stop working properly to fix this they set a limit for how many people can be using it at one given moment and have everyone else wait. 

Using a queue is very simple you create a list with and when acting on the list you take from the head of the list (the front of the list) or the tail of the list (the back of the list).
![queue](Images\queue-image.png)

 When working with queues it is rare that you will act on anything in the middle of the list the only time this happens is when someone no longer wants to be in the queue and leaves without being acted on.

## commands and Big O
Operation | Description | Code    | Performance
-------- | -------- | --------|--------
enqueue(value) | Add a new value or object to the queue | queue.append(value) | O(1) - Adding a new object to the end of a list takes very little time.
dequeue() | Remove the first item from the list | value = queue[0] <br> del queue[0]|O(n) - once you take an object out of the list you must shift all spots behind it over 1.
size | check to see how many values are in the queue | length = len(queue) | O(1) - Checking the size of a dynamic array.
empty | check to see if the queue is empty or not | if len(queue) == 0| O(1) - this is the same as checking the size when it comes to performance

## example code
enqueue example
```python
# enqueue example
queue = [] # empty list
value_1 = "Nathan"
value_2 = "Ryan"

queue.append(value_1) # add an item to the back of the queue
queue..append(value_2) # add an item to the back of the queue
print(queue)

# dequeue example
removed = queue.pop(0) # get the first item in the queue and remove it.
print(removed)
print(queue)

# size example
print(len(queue))
```

## Problem
[Queues-project.py](Python-files\Queues-project.py) This project will will make a queue for a shopping line you will need to be able to add people to the line help people in line and print out the full line of people.
[Teachers answers](Python-files\Queues-project-answers.py)