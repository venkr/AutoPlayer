Syntax Comparison
=====

Hello World
-----
Java:
```Java
public class HelloWorld {
    public static void main (String[] args){
        System.out.println("Hello World!");
    }
}
```

Python:
```Python
print("Hello World!")
```

Single line comments
------

Java:
```Java
//This is a comment
```
Python:
```Python
#This is a comment
```

Defining variables
------
Java:
```Java
int x = 10;
String y = "Hello";
```
Python:
```Python
x = 10
y = "Hello"
x = "Hello"
```

(Note the last line which isn't possible in Java)

Boolean expressions
-----

Java:
```Java
!(x>0 && y>0) || z > 0
```

Python:
```Python
not(x > 0 and y > 0) or z > 0
```

Conditionals 
-----

Java:
```Java
if (a){
  doA();
} else if (b){
  doB();
} else {
  doC();
  doD();
}
doE();
```

Python:
```Python
if a:
  doA()
elif b:
  doB()
else:
  doC()
  doD()
doE()
```

Note: While the indentation in the Java code is for readability, in Python, incorrect indentation will cause the program to run incorrectly.

Looping
-----

Java:
```Java
while (a){
  doA();
}
```

Python:
```Python
while a:
  doA()
```

Java:
```Java
for (int number: listOfNumbers){
  doThing(number);
}
```

Python:
```Python
for number in listOfNumbers:
  doThing(number)
```

Java:
```Java
for (int i = 0; i < 100; i++){
  doThing(i);
}
```

Python:
```Python
for i in range(0,100):
  doThing(i)
```

Functions
-----
Java:
```Java
public int increment(int i){
  return i + 1;
}
```

Python:
```
def increment(i):
  return i + 1
```
Lists:
-----

Lists are the equivalent of Arrays or ArrayLists in Java.
However, they can hold different types, and have many inbuilt functions.

An empty list:
```Python
myList = []
```
A prepopulated list:
```Python
myList = [1, 2.0, "Hello World!"]
```

(Note: `>>>` is used to denote output.)

Getting an item:
```Python
myList = [1, 2.0, "Hello World!"]
print(myList[0])
>>> 1
```

Negative indexes count from the end:
```Python
myList = [1, 2.0, "Hello World!"]
print(myList[-1])
>>> "Hello World!"
```

(You can use both positive and negative indexes on Strings too, to treat them as char arrays!)

Changing an item:
```Python
myList = [1, 2.0, "Hello World!"]
print(myList)
>>> [1, 2.0, 'Hello World!']
myList[0] = 5
print(myList)
>>> [5, 2.0, 'Hello World!']
```

Appending an item:
```Python
myList = [1, 2.0, "Hello World!"]
myList.append(1)
print(myList)
>>> [1, 2.0, 'Hello World!', 1]
```

Helpful links
=====
Lists a lot of Python syntax, starting from most common to least common: https://learnxinyminutes.com/docs/python3/

Comparison between C++ and Python syntax, might be useful: http://jasonpark.me/DuoCoder/public/learn.html?lang_from=cpp&lang_to=py
