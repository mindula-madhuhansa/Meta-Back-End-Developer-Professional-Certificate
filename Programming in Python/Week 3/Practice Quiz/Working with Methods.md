1. True or False: A class can serve as a base class for many derived classes. 
   - [x] **True**
   - [ ] False
        > Theoretically it can be superclass for infinite subclasses.  

2. In case of multiple inheritance where C is a derived class inheriting from both class A and B, and where a and b are the respective objects for these classes, which of the following code will inherit the classes A and B correctly? (Select all that apply)
    - [x] **class C(B, A)**
        > Code works irrespective of the order the classes are passed. 
    - [ ] class (a, b)
    - [x] **class C(A, B)**
        > Code works irrespective of the order the classes are passed. 
    - [ ] class(a, B)

3. In Example 3 of the previous exercise, if we had modified the code to include a global variable ‘a = 5’ as follows:
<br/><br/>&emsp;a = 5<br/>&emsp;class A;<br/>&emsp;&emsp;a = 7<br/>&emsp;&emsp;pass<br/><br/>&emsp;class B(A):<br/>&emsp;&emsp;pass<br/><br/>&emsp;class C(B):<br/>&emsp;&emsp;pass<br/><br/>&emsp;c = C()<br/>&emsp;print(c.a())<br/><br/>Will the code work and what will be the output if it does?
   - [ ] Yes and it will print the value 7
   - [x] **No**
   - [ ] Yes and it will print the value 5
       > As the print statement is over the object c. 

4. What function can be used other than mro() to see the way classes are inherited in a given piece of code?
   - [ ] class()
   - [ ] dir()
   - [x] **help()**
   - [ ] info()
       > help() can be used other than mro() to see the way classes are inherited in a given piece of code.

5. help() can be used other than mro() to see the way classes are inherited in a given piece of code.
   - [x] **call child class __init__()**
       > It is called over child class __init__() and refers parent class __init__()
   - [ ] call different parent class method
   - [x] **called over the __init__() method of the class it is called from**
       > That will refer the __init__() of parent class. 

6. What is the type of inheritance in the code below:
<br/><br/>&emsp;class A():<br/>&emsp;&emsp;pass<br/><br/>&emsp;class B(A):<br/>&emsp;&emsp;pass<br/><br/>&emsp;class C(B):<br/>&emsp;&emsp;pass<br/><br/>
   - [ ] Hierarchical
   - [ ] Multiple
   - [ ] Single
   - [x] **Multi-level**
       > Multi-level is the type of inheritance in the code
      

