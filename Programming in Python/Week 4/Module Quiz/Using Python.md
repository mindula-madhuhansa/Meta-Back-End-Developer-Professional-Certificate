1. Python is an interpreted language. Which of the following statements correctly describes an interpreted language?
     - [ ] The source code is pre-built and compiled before running.
     - [x] **The source code is converted into bytecode that is then executed by the Python virtual machine.**
     - [ ] Python needs to be built prior to it being run.
     - [ ] Python will save all code first prior to running.
         > Unlink other programming languages Python does not need to be built or linked for the code to run.

2. Why is indentation important in Python?
     - [ ] The code will compile faster with indentation. 
     - [x] **Python used indentation to determine which code block starts and ends.** 
     - [ ] It makes the code more readable.
     - [ ] The code will be read in a sequential manner
         > Python does not use curly braces like other languages, so it leverages off indentation to determine where the code blocks start and end.

3. What will be the output of the following code?
<br/><br/>&emsp;names = ["Anna", "Natasha", "Mike"]<br/>&emsp;names.insert(2, "Xi")<br/>&emsp;print(names)<br/><br/>
    - [ ] ["Anna", "Natasha", Xi]
    - [ ] ["Anna", "Xi", "Mike"]
    - [x] **["Anna", "Natasha", "Xi", "Mike"]**
    - [ ] ["Anna", "Natasha", 2, "Xi", "Mike"]
        > The insert() function displaces the remaining list after inserting the element passed. 

4. What will be the output of the code below?
<br/><br/>&emsp;for x in range(1, 4):<br/>&emsp;&emsp;print(int((str((float(x))))))<br/><br/>
    - [x] **Will give an error**
    - [ ] 1 , 2
    - [ ] 1.0, 2.0
    - [ ] "one", "two"
        > The float will first convert into string and output such as <class 'float'> which cannot be converted into int. 

5. What will be the output of the following code:
<br/><br/>&emsp;sample_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}<br/>&emsp;for x in sample_dict:<br/>&emsp;&emsp;print(x)<br/><br/>
    - [ ] {1 2 3}
    - [ ] (1, 'Coffee')<br/>(2, 'Tea')<br/>(3, 'Juice')
    - [x] **1 2 3**
    - [ ] 'Coffee', 'Tea', 'Juice'
        > The default values printed from a dictionary are keys.

6. What will be the output of the recursive code below?
<br/><br/>&emsp;def recursion(num):<br/>&emsp;&emsp;print(num)<br/>&emsp;&emsp;next = num - 3<br/>&emsp;&emsp;if next > 1:<br/>&emsp;&emsp;&emsp;recursion(next)<br/><br/>&emsp;recursion(11)<br/><br/>
    - [ ] 8 5 2
    - [x] **11 8 5 2**
    - [ ] 2 5 8
    - [ ] 2 5 8 11
        > The values printed have difference of 3, but printed in opposite order. 
     
7. What will be the type of time complexity for the following piece of code:
<br/><br/>&emsp;def bigo(numbers):<br/>&emsp;&emsp;for i in numbers:<br/>&emsp;&emsp;&emsp;print(numbers)<br/><br/>&emsp;big([1, 7, 13, 19])<br/><br/>
    - [ ] Logarithmic Time
    - [x] **Linear Time**
    - [ ] Quadratic Time
    - [ ] Constant Time
        > The single for loop will have linear time depending on the size of the input sequence. 

8. What will be the output of the code below:
<br/><br/>&emsp;str = 'Pomodoro'<br/>&emsp;for l in str:<br/>&emsp;if l == "o":<br/>&emsp;&emsp;str = str.split()<br/>&emsp;&emsp;print(str, end=",")<br/><br/>
    - [ ] ['P', 'm', 'd', 'o']
    - [ ] ['Pomodoro']
    - [x] **Will throw an error**
    - [ ] ['Pomodoro', 'modoro', 'doro', 'ro']
        > The first time split() function is used, the str variable will convert into a list over which split() cannot be used and will give an error. 

9. Find the output of the code below:
<br/><br/>&emsp;def d():<br/>&emsp;&emsp;color = "green"<br/>&emsp;&emsp;def e():<br/>&emsp;&emsp;&emsp;nonlocal color<br/>&emsp;&emsp;&emsp;color = "yellow"<br/>&emsp;&emsp;e()<br/>&emsp;&emsp;print("Color: " + color)<br/>&emsp;&emsp;color = "red"<br/>&emsp;color = "blue"<br/>&emsp;d()<br/><br/>
    - [x] **yellow**
    - [ ] red
    - [ ] blue
    - [ ] green
        > The color variable will retain the value from the nonlocal variable from e()

10. Find the output of the code below:<br/><br/>
&emsp;num = 9 <br/>&emsp;class Car:<br/>&emsp;&emsp;num = 5<br/>&emsp;&emsp;bathrooms = 2<br/><br/>&emsp;def cost_evaluation(num):<br/>&emsp;&emsp;num = 10<br/>&emsp;&emsp;return num<br/><br/>&emsp;class Bike():<br/>&emsp;&emsp;num = 11<br/><br/>&emsp;cost_evaluation(num)<br/>&emsp;car = Car()<br/>&emsp;bike = Bike()<br/>&emsp;car.num = 7<br/>&emsp;Car.num = 2<br/>&emsp;print(num)<br/><br/>
    - [x] **9**
    - [ ] 5
    - [ ] 2
    - [ ] 10
        > The value of the global variable will remain unchanged.
   
11. Which of the following is the correct implementation that will return **True** if there is a parent class P, with an object p and a subclass called C, with an object c?
    - [x] **print(issubclass(C,P))**
    - [ ] print(issubclass(C,c))
    - [ ] print(issubclass(p,C))
    - [ ] print(issubclass(P,C))
        > It can be read as C is subclass of P.

12. Django is a type of:
    - [ ] Asynchronous framework
    - [ ] Micro-framework
    - [x] **Full-stack framework**
        > Django is a Full-stack framework.

13. Which of the following is not true about Integration testing:
    - [ ] Tests the flow of data from one component to another.
    - [ ] Primarily dealt by the tester.
    - [x] **It is where the application is tested as a whole.**
    - [ ] It combines unit tests.
        > This is the case with system testing.

14. While using pytest for testing, it is necessary to run the file containing the main code before we can run the testing file containing our unit tests.
    - [x] **False**
    - [ ] True 
        > The main file must be saved to keep it updated but, it is not required to be executed. We have to import it into our testing file.
      
15. What will be the output of the code below:<br/><br/>&emsp;class A:<br/>&emsp;&emsp;def a(self):<br/>&emsp;&emsp;return "Function inside A"<br/><br/>&emsp;class B:<br/>&emsp;&emsp;def a(self):<br/>&emsp;&emsp;return "Function inside B"<br/><br/>&emsp;class C:<br/>&emsp;&emsp;pass<br/>&emsp;<br/>&emsp;class D(C, A, B):<br/>&emsp;&emsp;pass<br/><br/>&emsp;d = D()<br/>&emsp;print(d.a())<br/><br/>
    - [ ] Function inside B 
    - [ ] No output
    - [x] **Function inside A**
    - [ ] None of the above
        > The class A comes before class B in terms of the parent classes of class D.