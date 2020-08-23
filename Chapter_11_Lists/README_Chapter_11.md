
## Chapter 11 / Lists


<details>
<summary markdown="span">Click here for notes and new functions found in this chapter</summary>

- A list is a group of variables that share a common name - useful because they make it possible to work with more variables without creating a new name for each one. 
- When a program has many elements (for example, a field of stars in a space game or multiple data points in a visualization), lists make the code easier to write.
- Each item in a list is called an element, and each has an index value to mark its position within the list. Just like coordinates on the screen, index values for a list start counting from 0. 
- Lists in Python can contain values of varying data types. 
- list(), append() You can also use the built-in Python function list() to create a list value. Python list values are objects, and support a number of useful methods. The list method we’ll use most is append(), which adds an item to a list.
- After the list has been created, you can overwrite the value of an item at a particular index in a list by writing an expression with the square bracket syntax, followed by an equal sign (=) and the new value for that item e.g. x[2] = 789
- len() Python's built-in function to determine the length of a list (how many elements)
- Avoid creating lists within draw(), because creating a new list on every frame will slow down your frame rate.
- The way we use for loops to operate on lists is different depend- ing on exactly what we want to do with the list.
- A for loop can be used to fill a list with values or to read the values back out. 
- insert() list object method - Two lists can be used to store the position of the mouse—one for the x coordinate and one for the y coordinate. These lists store the location of the mouse for every frame. With each new frame, the newest coordinate is inserted at the beginning of the list. E.g. the code x.insert(0, mouseX) inserts the value in the variable mouseX at index 0 of the list (i.e., the beginning of the list). 
- The technique for storing coordinates in a list is inef- ficient. Because there’s no built-in limit to the num- ber of coordinates the list will store, the list in this program can quickly grow very large in memory, causing your sketch to slow down or even crash. For a more efficient technique that only stores the last n numbers, see the Examples → Basics → Input → StoringInput example included with Python Mode.
- Making a list of objects is nearly the same as making the lists however since each list element is an object, it must first be instanti- ated before it can be appended to the list. (For a built-in Pro- cessing class such as PImage, you need to use the loadImage() function to create the object before it’s assigned.)
- Because iterating over every item in a list is a very common task when writing computer programs, Python has a shorthand syn- tax for making it easier. Instead of creating a new counter vari- able, such as an i variable and iterating over the result of the range() function, it’s possible to iterate over the elements of a list directly using the for loop form e.g. 
```
# From: 
def draw():
    for i in range(len(bugs)):
        bugs[i].move() 
        bugs[i].display()

# To:
def draw():
    for b in bugs: 
        b.move 
        b.display
```

- nf() formats numbers so that nf(1, 4) returns the string “0001” and nf(11, 4) returns “0011”. These values are concatenated with the beginning of the filename (“frame-”) and the end (“.png”) to create the complete filename as a string.
  

</details>


<br/>

**Book examples**



Many variables

![example_11_1_many_variables]()

Too many variables

![example_11_2_too_many_variables]()

Lists, not variables

![example_11_3_lists_not_variables]()

Declare and append to a list

![example_11_4_declare_and_append_to_a_list]()

Compact list initialization

![example_11_5_compact_list_initialization]()

Revisiting the first exmaple

![example_11_6_revisiting_the_first_example]()

Filling a list in for a loop

![example_11_7_filling_a_list_in_for_a_loop]()

Example 11_8 (no such example in book)


Track mouse movements 

![example_11_9_track_mouse_movements]()

Managing many objects

![example_11_10_managing_many_objects]()

A new way to manage objects

![example_11_11_a_new_way_to_manage_objects]()

Sequence of images

![example_11_12_sequence_of_images]()

Robot 9: Lists

![example_11_13_robot_9_lists]()


<br/>

**Experiments**

<br/>