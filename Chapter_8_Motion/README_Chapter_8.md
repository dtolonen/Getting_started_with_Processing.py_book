
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

![example_8_1_see_the_framerate]()

Set the framerate

![example_8_2_set_the_framerate]()

Move a shape

![example_8_3_move_a_shape]()

Wrap around

![example_8_4_wrap_around]()

Bounce off the wall

![example_8_5_bounce_off_the_wall]()

Calculate tween positions

![example_8_6_calculate_tween_positions]()

Generate random values

![example_8_7_generate_random_values]()

Draw randomly

![example_8_8_draw_randomly]()

Move shapes randomly

![example_8_9_move_shapes_randomly]()

Time passes

![example_8_10_time_passes]()

Triggering timed events

![example_8_11_triggering_timed_events]()

Sine wave values

![example_8_12_sine_wave_values]()

Sine wave values

![example_8_13_sine_value_movement]()

Circular motion

![example_8_14_circular_motion]()

Spirals

![example_8_15_spirals]()

Robot 6: Motion

![example_8_16_robot_6_motion]()



<br/>

**Experiments**

<br/>