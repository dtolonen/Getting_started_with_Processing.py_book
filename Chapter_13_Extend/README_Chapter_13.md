
## Chapter 13 / Extend


<details>
<summary markdown="span">Click here for notes and new functions found in this chapter</summary>

- Over the last decade, Processing has been used to make music videos for Radiohead and R.E.M., to make illustrations for publications such as Nature and the New York Times, to output sculptures for gallery exhibitions, to control huge video walls, to knit sweaters, and much more. Processing has this flexibility because of its system of libraries.
- Processing libraries: As smaller, self-contained projects, libraries are easier to manage than if these features were integrated into the main software.
- To use a library, select Import Library from the Sketch menu. Before a contributed library can be imported through the Sketch menu, it must be added through the Library Manager. Select the Import Library option from the Sketchbook menu and then select Add Library to open the Library Manager interface.
- In addition to the libraries included with Processing (these are called the core libraries), there are over 100 contributed libraries that are linked from the Processing website. All libraries are listed online at http://processing.org/reference/libraries/.
- The most common use of the Sound library is to play a sound as background music or when an event happens on screen. 
- The SoundFile object. The SoundFile class has many methods to control how a sound is played. The most essential are play() to play the sample a single time, loop() to play it from beginning to end over and over, stop() to halt the playback, and jump() to move to a specific moment within the file.
- AudioIn and Amplitude classes + objects, input() and analyze() methods.
- The fundamentals of sound synthesis are waveforms that include the sine wave, triangle wave, and square wave.
A sine wave sounds smooth, a square wave is harsh, and a triangle wave is somewhere between. Each wave has a number of properties. The frequency, measured in hertz, determines the pitch—the highness or lowness of the tone. The amplitude of the wave determines the volume—the degree of loudness.
- The sine object, created from the SinOsc class, frew() method.
- saveFrame() The animated images created by a Processing program can be turned into a file sequence with the saveFrame() function. When saveFrame() appears at the end of draw(), it saves a numbered sequence of TIFF-format images of the program’s output named screen-0001.tif, screen-0002.tif, and so on to the sketch’s folder. These files can be imported into a video or animation program and saved as a movie file. You can also specify your own filename and image file format. Use the # (hash mark) symbol to show where the numbers will appear in the filename. They are replaced with the actual frame numbers when the files are saved. You can also specify a subfolder to save the images into, which is helpful when working with many image frames. When using saveFrame() inside draw(), a new file is saved each frame—so watch out, as this can quickly fill your sketch folder with thousands of files.
- If your desired output is vector graphics, you can write the output to PDF files for higher resolution. The PDF Export library makes it possible to write PDF files directly from a sketch. 
</details>


<br/>

**Book examples**



Draw to a PDF

![example_13_5_draw_to_a_pdf]()

Play a sample

![example_13_1_play_a_sample]()

Listen to a microphone

![example_13_2_listen_to_a_microphone]()

Create a sine wave

![example_13_3_create_a_sine_wave]()

Saving images

![example_13_4_saving_images]()


<br/>

**Experiments**

<br/>