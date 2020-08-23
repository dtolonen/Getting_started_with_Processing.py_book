
## Chapter 8 / Motion


<details>
<summary markdown="span">Click here for notes and new functions found in this chapter</summary>

- frameRate() Processing uses float values to create fluid motion
- variable: direction
- Tweening: With a few lines of code, you can set up the start position and the stop position, then calculate the in- between (tween) positions at each frame. 
- random() We can simulate the unpredictable qualities of the world by generating random numbers. The random() func- tion calculates these values; we can set a range to tune the amount of disarray in a program. Note: behaves differently from the random module included in the Python standard library.
- constrain() constrain() func- tion limits a value to a specific range, which can be used to keep x and y within the boundaries of the Display Window.
- randomSeed() function can be used to force random() to produce the same sequence of numbers each time a program is run. 
- millis() Every Processing program counts the amount of time in milliseconds that has passed since it was started. We can use this counter to trigger animations at specific times. The millis() function returns this counter value.
- sin() and cos() functions in Processing return values between −1 and 1 for the sine or cosine of the specified angle. Like arc(), the angles must be given in radian values. To be useful for drawing, the float values returned by sin() and cos() are usually multiplied by a larger value. 
- variable: sinval With the map() function, the sinval variable is converted from this range to values from 0 and 255. 
- sin() and cos() are used together, they can produce cir- cular motion. The cos() values provide the x coordinates, and the sin() values provide the y coordinates. Both are multiplied by a variable named scalar to change the radius of the move- ment and summed with an offset value to set the center of the circular motion. A slight change made to increase the scalar value at each frame produces a spiral, rather than a circle.

</details>


<br/>

**Book examples**



See the framerate

![example_8_1_see_the_framerate](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_8_Motion/example_8_1_see_the_framerate/frames/example_8_1_see_the_framerate.png)

Set the framerate

![example_8_2_set_the_framerate](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_8_Motion/example_8_2_set_the_framerate/frames/example_8_2_set_the_framerate.png)

Move a shape

![example_8_3_move_a_shape](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_8_Motion/example_8_3_move_a_shape/frames/SaveExample-0231.png)

Wrap around

![example_8_4_wrap_around](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_8_Motion/example_8_4_wrap_around/frames/SaveExample_8_4_tog.png)

Bounce off the wall

![example_8_5_bounce_off_the_wall](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_8_Motion/example_8_5_bounce_off_the_wall/frames/example_8_5_bounce_off_the_wall.png)

Calculate tween positions

![example_8_6_calculate_tween_positions](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_8_Motion/example_8_6_calculate_tween_positions/frames/example_8_6_calculate_tween_positions.png)

Generate random values

![example_8_7_generate_random_values](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_8_Motion/example_8_7_generate_random_values/frames/example_8_7_generate_random_values.png)

Draw randomly

![example_8_8_draw_randomly](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_8_Motion/example_8_8_draw_randomly/frames/example_8_8_draw_randomly.png)

Move shapes randomly

![example_8_9_move_shapes_randomly](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_8_Motion/example_8_9_move_shapes_randomly/frames/example_8_9_move_shapes_randomly.png)

Time passes

![example_8_10_time_passes](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_8_Motion/example_8_10_time_passes/frames/example_8_10_time_passes.png)

Triggering timed events

![example_8_11_triggering_timed_events](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_8_Motion/example_8_11_triggering_timed_events/frames/example_8_11_triggering_timed_events.png)

Sine wave values

![example_8_12_sine_wave_values](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_8_Motion/example_8_12_sine_wave_values/frames/SaveExample_8_12_tog.png)

Sine wave values

![example_8_13_sine_value_movement](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_8_Motion/example_8_13_sine_value_movement/frames/SaveExample_8_13_tog.png)

Circular motion

![example_8_14_circular_motion](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_8_Motion/example_8_14_circular_motion/frames/SaveExample_8_14_tog.png)

Spirals

![example_8_15_spirals](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_8_Motion/example_8_15_spirals/frames/SaveExample_8_15_tog.png)

Robot 6: Motion

![example_8_16_robot_6_motion](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_8_Motion/example_8_16_robot_6_motion/frames/example_8_16_robot_6_motion.png)



<br/>

**Experiments**

<br/>