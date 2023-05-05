1. **<br/>def sum(n):<br/>&emsp;if n == 1:<br/>&emsp;&emsp;return 0<br/>&emsp;return n + sum(n-1)<br/><br/>a = sum(5)<br/>print(a)**<br/><br/>What will be the output of the recursive code above?
    - [ ] 0
    - [ ] RecursionError: maximum recursion depth exceeded
    - [x] **14**
    - [ ] 15
        > The output will be the sum of values from 2 to 5.

2. Statement A: A function in Python only executes when called.<br/>Statement B: Functions in Python always returns a value.
    - [ ] Both A and B are True
    - [ ] B is True but A is False
    - [x] **A is True but B is False**
    - [ ] Both A and B are False
        > Functions need to be called and don't always have to return a value. 

3. **some = ["aaa", "bbb"]<br/>#1<br/>def aa(some):<br/>&emsp;return<br/><br/>#2<br/>def aa(some, 5):<br/>&emsp;return<br/><br/>#3<br/>def aa():<br/>&emsp;return<br/><br/>#4<br/>def aa():<br/>&emsp;return "aaa"**<br/><br/>Which of the above are valid functions in Python? (Select all that apply)
   - [x] **1**
      > The function can return even if the argument passed is unused
   - [ ] 2
   - [x] **3**
      > An empty function can exist even if it has no functionality. 
   - [x] **4**
      > You can return a string such as “aaa” from a function.

4. For the following code:<br/>&emsp;**numbers = [15, 30, 47, 82, 95]<br/>&emsp;def lesser(numbers):<br/>&emsp;&emsp;return numbers < 50<br/><br/>&emsp;small = list(filter(lesser, numbers))<br/>&emsp;print(small)**<br/><br/>If you modify the code above and change filter() function to map() function, what will be the list elements in the output that were not there earlier?
   - [ ] 82, 65
   - [ ] 15, 30, 47, 82, 95
   - [x] **None of the other options**
   - [ ] 15, 37, 47
      > The values returned by the map() function in this case are boolean values from the comparison done in the lesser() function. So the right answer is: True, False. 