
## Chapter 3 / Draw


<details>
<summary markdown="span">Click here for notes and new functions found in this chapter</summary>

  
- size()
- arc()
- line()
- point()
- ellipse()
- rect()
- radians()
- special names for Pi values: PI, QUARTER_PI, HALF_PI, and TWO_PI can be used to replace the radian values for 180°, 45°, 90°, and 360°
- strokeWeight()
- strokeCap()
- strokeJoin() default: pointed (mitered) corners
- ellipseMode()
- rectMode()
- ellipseMode(CORNER) makes the ellipse() function behave more like rect()
- ellipseMode(RADIUS)
- background(), fill(), and stroke() 
- The values of the parameters are in the range of 0 to 255, where 255 is white, 128 is medium gray, and 0 is black. To move beyond grayscale values, you use three parameters to specify the red, green, and blue components of a color e.g. fill(255, 0, 0). Alternatively, use the Processing app colour picker. Optional fourth parameter to fill() or stroke() is the alpha value, which uses the range 0 to 255 e.g. fill(255, 0, 0, 160)
- fill()
- noStroke()
- noFill()
- beginShape(), vertex(), endShape()  not limited to using these  basic geometric shapes — you can also define new shapes by connecting a series of points. Use the word CLOSE to connect the last point: endShape(CLOSE)

- As you work with Processing sketches, you’ll find yourself creating dozens of iterations of ideas; using comments to make notes or to disable code can help you keep track of multiple options. Use Ctrl-/ (Cmd-/ on OS X) to add or remove comments

</details>


<br/>

**Book examples**



Draw a point

![example_3_2_draw_a_point](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_3_Draw/example_3_2_draw_a_point/frames/SaveExample-0000.png)

Draw a line

![example_3_3_draw_a_line](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_3_Draw/example_3_3_draw_a_line/frames/SaveExample-0000.png)

Draw basic shapes

![example_3_4_draw_basic_shapes](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_3_Draw/example_3_4_draw_basic_shapes/frames/SaveExample-0000.png)

Draw a rectangle

![example_3_5_draw_rectangle](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_3_Draw/example_3_5_draw_rectangle/frames/SaveExample-0000.png)

Draw an ellipse

![example_3_6_draw_ellipse](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_3_Draw/example_3_6_draw_ellipse/frames/SaveExample-0000.png)

Draw part of an ellipse

![example_3_7_draw_part_of_ellipse](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_3_Draw/example_3_7_draw_part_of_ellipse/frames/SaveExample-0000.png)

Draw with degrees

![example_3_8_draw_with_degrees](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_3_Draw/example_3_8_draw_with_degrees/frames/SaveExample-0000.png)

Control the drawing order

![example_3_9_control_drawing_order](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_3_Draw/example_3_9_control_drawing_order/frames/SaveExample-0000.png)

Control the drawing order in reverse

![example_3_10_contol_drawing_order_reverse](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_3_Draw/example_3_10_contol_drawing_order_reverse/frames/SaveExample-0000.png)

Set the stroke weight 

![example_3_11_set_stroke_weight](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_3_Draw/example_3_11_set_stroke_weight/frames/SaveExample-0000.png)

Set the stroke caps

![example_3_12_set_stroke_caps](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_3_Draw/example_3_12_set_stroke_caps/frames/SaveExample-0000.png)

Set the stroke joins

![example_3_13_set_stroke_joins](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_3_Draw/example_3_13_set_stroke_joins/frames/SaveExample-0000.png)

On the corner

![example_3_14_on_the_corner](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_3_Draw/example_3_14_on_the_corner/frames/SaveExample-0000.png)

Paint with grays

![example_3_15_paint_with_grays](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_3_Draw/example_3_15_paint_with_grays/frames/SaveExample-0000.png)

Control the fill and stroke

![example_3_16_control_fill_and_stroke](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_3_Draw/example_3_16_control_fill_and_stroke/frames/SaveExample-0000.png)

Draw with colour

![example_3_17_draw_with_colour](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_3_Draw/example_3_17_draw_with_colour/frames/SaveExample-0000.png)

Set transparency

![example_3_18_set_transparency](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_3_Draw/example_3_18_set_transparency/frames/SaveExample-0000.png)

Draw an arrow

![example_3_19_draw_an_arrow](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_3_Draw/example_3_19_draw_an_arrow/frames/SaveExample-0000.png)

Close the gap

![example_3_20_close_the_gap](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_3_Draw/example_3_20_close_the_gap/frames/SaveExample-0000.png)

Create some creatures

![example_3_21_create_some_creatures](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_3_Draw/example_3_21_create_some_creatures/frames/SaveExample-0000.png)

Comments

![example_3_22_comments](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_3_Draw/example_3_22_comments/frames/SaveExample-0000.png)

Robot 1: Draw

![example_3_23_robot1_draw](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_3_Draw/example_3_23_robot1_draw/frames/SaveExample-0000.png)


<br/>

**Experiments**

<br/>
