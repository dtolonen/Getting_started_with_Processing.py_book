
## Chapter 6 / Translate, Rotate, Scale


<details>
<summary markdown="span">Click here for notes and new functions found in this chapter</summary>

- An alternative technique for positioning and moving things on screen is to change the screen coordinate system. By modifying the default coordinate system, we can create different transformations including translation, rotation, and scaling.

- translate() sets the (0,0) coordinate of the screen to the mouse location (mouseX and mouseY). Each time the draw() block repeats, the rect() is drawn at the new ori- gin, derived from the current mouse location.
- rotate() rotates the coordinate system. It has one parameter, which is the angle (in radians) to rotate. It always rotates relative to (0,0), known as rotating around the origin.
- To rotate a shape around its own center, it must be drawn with coordinate (0,0) in the middle.
- the order in which the functions appear affects the result.
- Another option is to use the rectMode(), ellipse Mode(), imageMode(), and shapeMode() functions, which make it easier to draw shapes from their center.
- variable: angleDirection
- scale() stretches the coordinates on the screen.
- To maintain a consistent stroke weight as a shape scales, divide the desired stroke weight by the scalar value.
- pushMatrix() and popMatrix() always used in pairs. To isolate the effects of a transformation so they don’t affect later commands. When pushMatrix() is run, it saves a copy of the current coordinate system and then restores that system after pop Matrix(). This is useful when transformations are needed for one shape but not wanted for another.

</details>


<br/>

**Book examples**



Translating location

![example_6_1_translating_location](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_6_Translate_Rotate_Scale/example_6_1_translating_location/frames/SaveExample-0113.png)

Multiple translations

![example_6_2_multiple_translations](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_6_Translate_Rotate_Scale/example_6_2_multiple_translations/frames/SaveExample-0063.png)

Corner rotation

![example_6_3_corner_rotation](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_6_Translate_Rotate_Scale/example_6_3_corner_rotation/frames/SaveExample_6_3_tog.png)

Center rotation

![example_6_4_center_rotation](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_6_Translate_Rotate_Scale/example_6_4_center_rotation/frames/SaveExample_6_4_tog.png)

Translation, then rotation 

![example_6_5_translation_then_rotation](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_6_Translate_Rotate_Scale/example_6_5_translation_then_rotation/frames/SaveExample-0095.png)

Rotation, then translation

![example_6_6_rotation_then_translation](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_6_Translate_Rotate_Scale/example_6_6_rotation_then_translation/frames/SaveExample_6_6_tog.png)

An articulating arm

![example_6_7_an_articulating_arm](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_6_Translate_Rotate_Scale/example_6_7_an_articulating_arm/frames/SaveExample-0158.png)

Scaling

![example_6_8_scaling](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_6_Translate_Rotate_Scale/example_6_8_scaling/frames/SaveExample-0109.png)

Keeping strokes consistent

![example_6_9_keeping_strokes_consistent](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_6_Translate_Rotate_Scale/example_6_9_keeping_strokes_consistent/frames/SaveExample_6_9_tog.png)

Isolating transformations

![example_6_10_isolating_transformations](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_6_Translate_Rotate_Scale/example_6_10_isolating_transformations/frames/SaveExample_6_10_tog.png)

Robot 4: Translate, rotate, scale

![example_6_11_robot_4_translate_rotate_scale](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_6_Translate_Rotate_Scale/example_6_11_robot_4_translate_rotate_scale/frames/SaveExample-0040.png)


<br/>

**Experiments**

<br/>