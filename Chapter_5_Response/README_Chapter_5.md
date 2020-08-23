
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


<br/>

**Book examples**



Draw function

![example_5_1_draw_function ](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_5_Response/example_5_1_draw_function/frames/example_5_1_draw_function.png)

The setup() function

![example_5_2_the_setup___function](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_5_Response/example_5_2_the_setup___function/frames/example_5-2_the_setup___function.png)

Global variables

![example_5_3_global_variables ](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_5_Response/example_5_3_global_variables/frames/SaveExample-0001.png)

Track the mouse

![example_5_4_track_the_mouse](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_5_Response/example_5_4_track_the_mouse/frames/SaveExample-0277.png)

The dot follows you

![example_5_5_the_dot_follows_you](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_5_Response/example_5_5_the_dot_follows_you/frames/SaveExample-0365.png)

Draw continuously 

![example_5_6_draw_continuosly](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_5_Response/example_5_6_draw_continuosly/frames/SaveExample-0195.png)

Set the thickness on the fly

![example_5_7_set_thickness_on_the_fly](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_5_Response/example_5_7_set_thickness_on_the_fly/frames/SaveExample-0331.png)

Easing does it

![example_5_8_easing_does_it](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_5_Response/example_5_8_easing_does_it/frames/SaveExample_5_8_tog.png)

Smooth lines with easing

![example_5_9_smooth_lines_with_easing](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_5_Response/example_5_9_smooth_lines_with_easing/frames/SaveExample-0925.png)

Click the mouse

![example_5_10_click_the_mouse](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_5_Response/example_5_10_click_the_mouse/frames/SaveExample-0336.png)

Detect when not clicked

![example_5_11_detect_when_not_clicked](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_5_Response/example_5_11_detect_when_not_clicked/frames/SaveExample-0001.png)

Multiple mouse buttons

![example_5_12_multiple_mouse_buttons](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_5_Response/example_5_12_multiple_mouse_buttons/frames/SaveExample_5_12_tog.png)

Find the cursor

![example_5_13_find_the_cursor](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_5_Response/example_5_13_find_the_cursor/frames/SaveExample_5_13_tog.png)

The bounds of a circle

![example_5_14_the_bounds_of_a_circle](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_5_Response/example_5_14_the_bounds_of_a_circle/frames/SaveExample_5_14_tog.png)

The bounds of a rectangle 

![example_5_15_the_bounds_of_a_rectangle](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_5_Response/example_5_15_the_bounds_of_a_rectangle/frames/SaveExample_5_15_tog.png)

Tap a key

![example_5_16_tap_a_key](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_5_Response/example_5_16_tap_a_key/frames/SaveExample_5_16_tog.png)

Draw some letters 

![example_5_17_draw_some_letters](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_5_Response/example_5_17_draw_some_letters/frames/SaveExample-0289.png)

Check for specific keys

![example_5_18_check_for_specific_keys](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_5_Response/example_5_18_check_for_specific_keys/frames/SaveExample_5_18_tog.png)

Move with arrow keys

![example_5_19_move_with_arrow_keys](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_5_Response/example_5_19_move_with_arrow_keys/frames/SaveExample_5_19_tog.png)

Map values to a range

![example_5_20_map_values_to_a_range](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_5_Response/example_5_20_map_values_to_a_range/frames/SaveExample_5_20_tog.png)

Map with the map() function

![example_5_21_map_with_the_map___function](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_5_Response/example_5_21_map_with_the_map___function/frames/SaveExample_5_21_tog.png)

Robot 3: response

![example_5_22_robot_3_response](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_5_Response/example_5_22_robot_3_response/frames/SaveExample_5_22_tog.gif)


<br/>


**Experiments**

<br/>