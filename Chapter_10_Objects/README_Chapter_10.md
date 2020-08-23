
## Chapter 10 / Objects


<details>
<summary markdown="span">Click here for notes and new functions found in this chapter</summary>

- Object-oriented programming (OOP)
- Unlike the primitive data types boolean, int, and float, which can store only one value, an object can store many. But that’s only a part of the story. Objects are also a way to group variables with related functions.
- Objects are important, because they break up ideas into smaller building blocks. 
- It’s easier to write and maintain smaller, under- standable pieces of code that work together than it is to write one large piece of code that does everything at once.
- A software object is a collection of related variables and func- tions. In the context of objects, a variable is called a field (some- times known as an instance variable or data attribute in Python) and a function is called a method. 
- Fields and methods work in a manner similar to the variables and functions covered in earlier chapters, but we’ll use the new terms to emphasize that they are a part of an object. To say it another way, an object com- bines related data (fields) with related actions and behaviors (methods). The idea is to group together related data with related methods that act on that data.
- Before you can create an object, you must define a class. A class is the specification for an object - a class is like a blueprint for a house. 
- the class defines the data types and behaviors, but each object (house) made from a single class (blueprint) has variables (color, fireplace) that are set to differ- ent values. To use a more technical term, each object is an instance of a class and each instance has its own set of fields and methods.
- Before you write a class, we recommend a little planning. Think about what fields and methods your class should have. Do a lit- tle brainstorming to imagine all the possible options and then prioritize and make your best guess about what will work. You’ll make changes during the programming process, but it’s impor- tant to have a good start.
- The fields inside a class can be any type of data. A class can simultaneously hold many booleans, floats, images, strings, and so on. Keep in mind that one reason to make a class is to group together related data elements. 
- Writing a class based on our brainstormed fields and methods, we follow three steps: 1. Write the class definition. 2. Write an __init__ method (explained shortly) to initialize the object and assign values to the fields. Python automatically calls this method whenever an object (an instance of the class) is created. The purpose of the __init__ method is to assign the initial values to the object’s fields. 3. Add the methods.
- The first parameter to any method in Python, including the __init__ method, is the word self. This is a special parame- ter that Python automatically passes to methods. Its value is the object that the method is being called on. The self parameter is what allows you to set the value for a field (e.g., the expression self.x = tempX in the preceding example) or to use the value of that field in an expression.
- Now that you have defined a class, to use it in a program you must define an object from that class. There are two steps to create an object: 1. Create a variable to store the object. 2. Create (initialize) the object by “calling” the name of the class as though it were a function.
- The Processing software has tabs to allow you to spread your code across more than one file - makes your code more manageable and easier to edit. Reinforce modularity and create a new tab for each new class. 

</details>


<br/>

**Book examples**



Make an object
![example_10_1_make_an_object](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_10_Objects/example_10_1_make_an_object/frames/SaveExample_10_1_tog.png)

Make multiple objects
![example_10_2_make_multiple_objects](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_10_Objects/example_10_2_make_multiple_objects/frames/SaveExample_10_2_tog.png)

Robot 8: Objects
![example_10_3_robot_8_objects](https://github.com/dtolonen/Getting_started_with_Processing.py_book/blob/master/Chapter_10_Objects/example_10_3_robot_8_objects/frames/example_10_3_robot_8_objects_1.png)


<br/>

**Experiments**

<br/>
