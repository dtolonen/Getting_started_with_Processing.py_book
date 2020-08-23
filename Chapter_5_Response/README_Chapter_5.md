## Chapter 5 / Response

<details>
<summary markdown="span">Click here for notes and new functions found in this chapter</summary>

- The code within the draw() block runs from top to bottom, then repeats until you quit the program by clicking the Stop button or closing the window. Each trip through draw() is called a frame. (The default frame rate is 60 frames per second, but this can be changed.)
- the code inside setup() is used to define the starting values. The first line is always the size() function, often followed by code to set the starting fill and stroke colors, or perhaps to load images and fonts. (If you don’t include the size() function, the Display Window will be 100×100 pixels.)
- There’s one more location to put code—you can also place variables outside of setup() and draw(). If you create a variable inside of setup(), you can’t use it inside of draw(), so you need to place those variables somewhere else. Such vari- ables are called global variables, because they can be used any- where (“globally”) in the program. 


- draw()
- setup()
- background() this function clears the entire window, so be sure to always place it before other functions inside draw(); other- wise, the shapes drawn before it will be erased.
- variables: mouseX, mouseY, pmouseX, pmouseY. The mouseX variable stores the x coordinate, and the mouseY variable stores the y coordinate. The pmouseX and pmouseY variables store the position of the mouse at the previous frame. These are updated each time draw() runs. 
- dist() The pmouseX and pmouseY variables can also be used to calculate the speed of the mouse. This is done by measuring the distance between the current and most recent mouse location. dist() simplifies this calculation. 
- With easing, there are two values: the current value and the value to move toward (see Figure 5-1). At each step in the program, the current value moves a little closer to the target value (targetX variable). See the line(s) beginning with x +=.
- usually can't change global variables from within a function - if you want to, you must include the keyword 'global' as the first line in your function with the name of the variable you want to change e.g. 'global x, y, px, py.' The keyword prevents you from absentmindedly creating a new variable in your draw() function (or any other function) that has the same name as a global variable, and overwriting the value in that global variable as a result.
- boolean variable: mousePressed (don't necessarily need if mousePressed == True: comparison operator e.g. if mousePressed: is enough)
- variable: mouseButton (has three values, LEFT, CENTER, RIGHT) 
- To write programs that have graphical user interfaces (buttons, checkboxes, scrollbars, etc.), we need to write code that knows when the cursor is within an enclosed area of the screen. 
- relational expressions
- variables: key, keyPressed. The key variable stores the most recent key that has been pressed. The key variable holds a string value whose length is 1. Unlike the boolean variable keyPressed, which reverts to False each time a key is released, the key variable keeps its value until the next key is pressed. Each time a new key is pressed, the value updates and a new character draws.
- textSize() 
- textAlign()
- text()
- map() the numbers that are created by the mouse and keyboard often need to be modified to be useful - or in a useful range - within a program. This transformation can be done with an equation or with the map() function. The first parameter is the variable to be converted, the second and third parameters are the low and high values of that variable, and the fourth and fifth parameters are the desired low and high values. The map() function hides the math behind the conversion. Processing’s map() function is different from Python’s built-in map() function. 

</details>


## Book examples


### Draw function
![example_5_1_draw_function ]()

### The setup() function
![example_5_2_the_setup___function]()

### Global variables
![example_5_3_global_variables ]()

### Track the mouse
![example_5_4_track_the_mouse]()

### The dot follows you
![example_5_5_the_dot_follows_you]()

### Draw continuously 
![example_5_6_draw_continuosly]()

### Set the thickness on the fly
![example_5_7_set_thickness_on_the_fly]()

### Easing does it
![example_5_8_easing_does_it]()

### Smooth lines with easing
![example_5_9_smooth_lines_with_easing]()

### Click the mouse
![example_5_10_click_the_mouse]()

### Detect when not clicked
![example_5_11_detect_when_not_clicked]()

### Multiple mouse buttons
![example_5_12_multiple_mouse_buttons]()

### Find the cursor
![example_5_13_find_the_cursor]()

### The bounds of a circle
![example_5_14_the_bounds_of_a_circle]()

### The bounds of a rectangle 
![example_5_15_the_bounds_of_a_rectangle]()

### Tap a key
![example_5_16_tap_a_key]()

### Draw some letters 
![example_5_17_draw_some_letters]()

### Check for specific keys
![example_5_18_check_for_specific_keys]()

### Move with arrow keys
![example_5_19_move_with_arrow_keys]()

### Map values to a range
![example_5_20_map_values_to_a_range]()

### Map with the map() function
![example_5_21_map_with_the_map___function]()

### Robot 3: response
![example_5_22_robot_3_response]()










## Experiments
