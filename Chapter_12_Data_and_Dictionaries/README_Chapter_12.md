
## Chapter 12 / Data and Dictionaries


<details>
<summary markdown="span">Click here for notes and new functions found in this chapter</summary>

- Data visualization is one of the most active areas at the intersection of code and graphics and is also one of the most popular uses of Processing. 
- Writing code to create visualization from scratch provides more control over the output and encourages users to imagine, explore, and create more unique representations of data - far more interesting than being limited by prepack- aged methods or tools that are available.
- Simple data types (int, float for numbers and decimals) vs compound data type (objects, lists), which track multiple values. The values in a list are accessed by their numerical index, whereas the values in an object are accessed by name as data attributes. 
- The examples in this chapter introduce a new compound data type: the dictionary. Dictionaries are data structures that are conceptually similar to lists, except instead of accessing values by numerical index, you access them by name. This makes dic- tionaries a data type especially suited for storing, transmitting, and processing structured data. There are several built-in Python tools that read data in various formats (e.g., from the data folder for a sketch) and return dictionaries.
- You can think of a dictionary as being sort of like a list, except you index its values not with a number but with a key. Dictionary keys are usually strings that identify the values they point to in an easy-to-remember way.
- dictionary values can be any data type: strings, integers, floating-point numbers, booleans—even objects, lists, and other dictionaries can be stored as dictionary values.
- check to see whether or not a key is present in a dictio- nary by using the special operator in e.g. 'if 'eqRadiusKm' in planetInfo'. 
- In other computer languages (such as Java and C++), the analo- gous data structure is called a map. Sometimes when talking about dictionaries, we’ll say that keys “map” to values. 
- we can create lists of dictionaries
- We can access any value for a par- ticular key for one of the dictionaries in this list like so: print planetList[2]['name'] # prints 'Earth'.
- We can loop over a list of dictionaries the same way we loop over a regular list, with a for loop.
- Instead of creating a variable for each dictionary first and then putting the variable names into the list declaration, we can simply write the dictionaries straight into a list.
- Python csv library - Spreadsheets are made out of rows and columns, with each row usually repre- senting one item and each cell in the row representing some aspect of that item. Spreadsheet data is often stored in plain-text files with columns using commas or the tab character. Python includes a library to make it easy to work with data stored in this format. The csv library provides functions and classes that make it easy to work with data in CSV format. There’s one tricky thing about using CSV files, which is that they don’t contain any information about what kind of data they’re storing. the csv library always gives you data from a CSV file as a string, even if the underlying data looks like a number. If you want to use that string as a number, you have to explicitly convert it your- self, using one of Python’s built-in conversion functions like int().
- The import statement at the beginning of the program is what signals to Python that we want to use the built-in csv library in our program. E.g. 'import csv'.
- open() function, csv.reader() object -  We also need to use the built-in Python function open() to gain access to the file in the sketch’s data folder. Once we’ve created a CSV reader object, we use a for loop to operate on each row of data in sequence. A CSV reader object works a lot like a list, in that we can iterate over it with a for loop. 
-  setXY() If your table data has headers, your data is easier to read. E.g. setXY() converts the latitude and longitude data from the file's headers (zip,state,city,lat,lng) into a point on the screen.
-  csv.DictReader object - a little different from the csv.reader object that we used in the previous example. When we used the csv.reader object, we had to access each cell in a row of data by its numerical index. The csv.DictReader object, on the other hand, gives us a dictionary for each row. This dictio- nary uses the strings in the header line of the CSV file as its keys, and each key maps to the corresponding value for the row in question. Because each row is a dictionary, we can use (for example) the expression row["lat"] to access the latitude column, which is much easier to remember than if we needed to reference the column by its numerical index. csv.DictReader objects, unlike regular lists, can only be iterated over once, so we use the list() function to read all of the rows from one of these objects at once and store them in a separate variable.
-  JSON The JavaScript Object Notation (JSON) format is another com- mon system for storing data. Like HTML and XML formats, the elements have labels associated with them. Notice that the CSV notation has fewer characters than JSON, which can be important when working with massive data sets. On the other hand, the JSON version is often easier to read because each piece of data is labeled.
-  json library you may also have noticed that JSON looks very similar to how Python data structures look when included directly to a program. There are subtle differences and you can't just paste a JSON structure into your Python program and expect it to work. (for example, the data structure of a json file can be a list of dictionaries, instead of a single dictionary in Python). As a result, a call to json.load() in setup() returns a list.  Here, you can use the JSON library to convert JSON into a format that we can use in a program. 
-  json library you may also have noticed that JSON looks very similar to how Python data structures look when included directly to a program. There are subtle differences and you can't just paste a JSON structure into your Python program and expect it to work. For example, the data structure of a json file can be a list of dictionaries, instead of a single dictionary in Python. As a result, the call to json.load() in setup() returns a list.  Here, you can use the JSON library to convert JSON into a format that we can use in a program. 
-  json.load() function loads data in JSON format from a given file handle. (Just as with the CSV examples, we need to create the file handle first with the built-in open() function.) The json.load() function returns a value of a compound data type  that corresponds to the data in the JSON file. We can then use square bracket syntax to access values for particular keys in that dictionary. After we’ve converted the JSON into Python, the types of the values retrieved will reflect their types from the original JSON data structure (i.e., JSON integers will become Python integers, JSON strings will become Python strings, etc.).
-  APIs: Public access to massive quantities of data collected by govern- ments, corporations, organizations, and individuals is changing our culture. This data is most often accessed through software structures called APIs (application programming interfaces). Essentially, they are requests for data made to a service. When data sets are huge, it’s not practical or desired to copy the entirety of the data; an API allows a pro- grammer to request only the trickle of data that is relevant from a massive sea. Some APIs are entirely public, but many require authentication, which is typically a unique user ID or key so the data service can keep track of its users. Many APIs also require you to reg- ister as a developer on their site to obtain an “API key,” a special identifying string that must be included with the API request. Processing can request data over the Internet when the com- puter that is running the program is online. CSV, TSV, JSON, and XML files can be loaded using the corresponding load function with a URL as the parameter. you’ll find that the data returned by many APIs shares a similar format.

</details> 


<br/>

**Book examples**



Keyboard keys as dictionary keys

![example_12_1_keyboard_keys_as_dictionary_keys]()

The planets

![example_12_2_the_planets]()

Read the data

![example_12_3_read_the_data]()

Draw the table

![example_12_4_draw_the_table]()

29,740 cities

![example_12_5_29_740_cities]()

Read a JSON file

![example_12_6_read_a_JSON_file]()

Visualize data from a JSON file

![example_12_7_visualize_data_from_a_JSON_file]()

Parsing the weather data

![example_12_8_parsing_the_weather_data]()

Chaining square brackets

![example_12_9_chaining_square_brackets]()

Robot 10: Data, pt.1 

![example_12_10_robot_10_data_pt1]()

Robot 10: Data, pt.2 

![example_12_10_robot_10_data_pt2]()


<br/>

**Experiments**

<br/>