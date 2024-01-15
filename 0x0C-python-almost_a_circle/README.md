# 0x0C. Python - Almost a circle

In this project, I learned how to convert a Python data structure to a JSON string,
 convert a JSON string to a Python data structure, what is __*args__ and how to use it
what is __**kwargs__ and how to use it, how to handle named arguments in a function.

## Function Prototypes : 

Prototypes for functions written in this project:

| File                     	| Prototype                             	|
| -----------------------  	| -------------------------------------------	|
| `models/base.py '        	| `def __init__(self, id=None)`                 |
| `models/rectangle.py`    	| 'Class Rectangle`   				|

* **0. If it's not tested it doesn't work**
  

* **1. Base class**
  * [__init__.py](__init__.py): class constructor: def __init__(self, id=None):
  * [base.py](./models/base.py):  Class Base to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)
  
* **2. First Rectangle**
  * [rectangle.py](./models/rectangle.py): Write the class Rectangle that inherits from Base
  
* **3. Validate attributes**
 * [rectangle.py](./models/rectangle.py): Write the class Rectangle that inherits from Base. Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded)

* **4. Area first**
  * [rectangle.py](./models/rectangle.py):Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.
  
* **5. Display #0**
  * [rectangle.py](./models/rectangle.py): Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character
  
* **6. __str__**
  * [rectangle.py](./models/rectangle.py): Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
  

* **7. Display #1**
  * [rectangle.py](./models/rectangle.py): Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y
  

* **8. Update #0**
  * [rectangle.py](./models/rectangle.py): Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute

* **9. Update #1**
   * [rectangle.py](./models/rectangle.py): Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes

* **9. Update #1**
   * [rectangle.py](./models/rectangle.py): Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes
   
* **9. Update #1**
   * [rectangle.py](./models/rectangle.py): Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes
 
* **10. And now, the Square!**
   * [square.py](./models/square.py): Write the class Square that inherits from Rectangle:

* **11. Square size**
   * [square.py](./models/square.py): Update the class Square by adding the public getter and setter size

* **12. Square update**
   * [square.py](./models/square.py): Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes:

* **13. Rectangle instance to dictionary representation**
   * [square.py](./models/square.py): Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle
 
* **14. Square instance to dictionary representation**
   * [square.py](./models/square.py): Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square

* **15. Dictionary to JSON string**
   * [square.py](./models/square.py): Update the class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries
 
* **16. JSON string to file**
   * [square.py](./models/square.py): Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file

* **17. JSON string to dictionary mandatory**
   * [square.py](./models/square.py): Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle
 
* **18. Dictionary to Instance**
   * [square.py](./models/square.py): Update the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set

* **19. File to instances**
   * [square.py](./models/square.py):Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances
 
* **20. JSON ok, but CSV?**
   * [square.py](./models/square.py): Update the class Base by adding the class methods def save_to_file_csv(cls, list_objs): and def load_from_file_csv(cls): that serializes and deserializes in CSV.
