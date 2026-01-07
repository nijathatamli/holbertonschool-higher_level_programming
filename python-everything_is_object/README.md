Everything is an Object in Python

In Python, the phrase "Everything is an object" isn't just a catchy slogan—it is a fundamental truth of the language's architecture. Unlike languages like Java or C++, where there is a distinction between primitive types (like int) and objects, Python treats every piece of data, every function, and even every module as an object.
1. Objects, Identity, and Type

Every object in Python has three distinct characteristics:

    Identity (id): The object's address in memory.

    Type (type): The class the object belongs to (e.g., int, list, function).

    Value: The actual data stored in the object.

Python

x = 42
print(id(x))    # Unique memory address
print(type(x))  # <class 'int'>

2. Mutable vs. Immutable Objects

The way Python handles objects depends largely on whether the object can be changed after it is created.
Category	Types	Behavior
Immutable	int, float, str, tuple, bool	Cannot be changed. Modifying them creates a new object.
Mutable	list, dict, set, bytearray	Can be changed in-place without changing the identity.

    Pro Tip: Be careful when passing mutable objects (like lists) as default arguments in functions; they persist across multiple function calls!

3. Functions and Classes as First-Class Objects

In Python, functions and classes are First-Class Objects. This means they can be:

    Assigned to a variable.

    Passed as an argument to another function.

    Returned from a function.

    Stored in data structures (like lists or dictionaries).

Python

def shout(text):
    return text.upper()

# Assigning a function to a variable
yell = shout 
print(yell("hello")) # HELLO

4. Why This Matters: Variable Assignment

In Python, variables are labels (references) pointing to objects, not boxes containing values.

When you write a = [1, 2, 3] and b = a, both a and b point to the same object in memory. If you modify the list via a, the change is reflected in b.
5. Introspection and the object Base Class

Almost everything in Python inherits from the base object class. You can use introspection to see what an object is made of:

    dir(obj): Lists all attributes and methods of an object.

    getattr(obj, 'name'): Gets a named attribute from an object.

    isinstance(obj, class): Checks if an object is an instance of a specific class.
