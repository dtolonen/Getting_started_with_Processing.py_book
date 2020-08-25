
## Chapter 7 / Media


<details>
<summary markdown="span">Click here for notes and new functions found in this chapter</summary>

- PImage, PFont, String, and PShape.
- loadImage() three steps to follow before you can draw an image to the screen: 1. Add the image to the sketch’s data folder. 2. Create a variable to store the image. 3. Load the image into the variable with loadImage().
- image() you can then draw the image on the screen with this function. The parameters: The first parameter to image() specifies the image to draw; the second and third set the x and y coordinates. Optional fourth and fifth parameters to the image function set the width and height to draw the image. If the fourth and fifth parameters are not used, the image is drawn at the size at which it was created.
- The loadImage variable can't be called until after setup() is called, so you must/may have to initialise the img variable to None (img=None) as a special Python placeholder value allowing us to create a variable, but leave it 'empty'. Only in setup(), do we call the loadImage function and assign a real value to the img variable ( e.g. img = loadImage("lunar.jpg") ).
- The following websites are good places to find fonts with open licenses to use with Processing: http://www.google.com/fonts , http://openfontlibrary.org , http://www.theleagueofmoveabletype.com.
- Loading fonts and adding words to a sketch: add font to data folder, create variable to store the font, create the font and assign it to the variable with createFont(), use  textFont() to set the current font. 
- text() The first parameter to text() is the character(s) to draw to the screen. (Notice that the characters are enclosed within quotes.) The second and third parameters set the horizontal and vertical location. The location is relative to the baseline of the text. You can also set text to draw inside a box by adding fourth and fifth parameters that specify the width and height of the box.
- Creating a new shape: shape() , loadShape(), createShape() ,beginShape() , endShape() and shapeMode(CENTER) Vector shapes in the SVG format can be displayed in a different way, using loadShape(). Making a custom PShape with createShape() can make sketches more efficient when the same shape is drawn many times. Processing doesn't support all SVG features. See PShape documentation. 

</details>


<br/>

**Book examples**



Load an image

![example_7_1_load_an_image](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_7_Media/example_7_1_load_an_image/frames/SaveExample-0156.png)

Load more images

![example_7_2_load_more_images](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_7_Media/example_7_2_load_more_images/frames/SaveExample_7_2_tog.png)

Mousing around with an image

![example_7_3_mousing_around_with_an_image](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_7_Media/example_7_3_mousing_around_with_an_image/frames/SaveExample_7_3_tog.png)

Transparency with a GIF

![example_7_4_transparency_with_a_gif](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_7_Media/example_7_4_transparency_with_a_gif/frames/SaveExample_7_4_tog.png)

Transparency with a PNG

![example_7_5_transparency_with_a_png](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_7_Media/example_7_5_transparency_with_a_png/frames/SaveExample_7_5_tog.png)

Drawing with fonts

![example_7_6_drawing_with_fonts](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_7_Media/example_7_6_drawing_with_fonts/frames/SaveExample-0001.png)

Draw a box

![example_7_7_draw_a_box](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_7_Media/example_7_7_draw_a_box/frames/SaveExample-0001.png)

Store text in a string

![example_7_8_store_text_in_a_string](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_7_Media/example_7_8_store_text_in_a_string/frames/SaveExample-0001.png)

Draw with shapes

![example_7_9_draw_with_shapes](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_7_Media/example_7_9_draw_with_shapes/frames/SaveExample-0001.png)

Scaling shapes

![example_7_10_scaling_shapes](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_7_Media/example_7_10_scaling_shapes/frames/SaveExample_7_10_tog.png)

Creaing a new shape

![example_7_11_creating_a_new_shape](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_7_Media/example_7_11_creating_a_new_shape/frames/SaveExample-0138.png)

Robot 5: Media

![example_7_12_robot_5_media](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_7_Media/example_7_12_robot_5_media/frames/SaveExample_7_12_tog.png)


<br/>

**Experiments**

<br/>