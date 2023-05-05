1. Which of the following is not a sequence data-type in Python?
    - [ ] Tuples
    - [x] **Dictionary**
    - [ ] String
    - [ ] List
        > Dictionaries have key-value object structure and are not sequences. 

2. For a given list called new_list, which of the following options will work:
<br/>new_list = [1,2,3,4]
<br/>Select all that apply.
    - [ ] new_list[4] = 10
    - [x] **new_list.extend(new_list)**
        > This will extend the list to give [1,2,3,4,1,2,3,4]
    - [x] **new_list.insert(0, 0)**
        > his will insert 0 at the 0th index giving: [0,1,2,3,4]
    - [x] **new_list.append(5)**
        > This will append the value 5 to the list giving: [1,2,3,4,5]

3. Which of the following is not a type of variable scope in Python? 
    - [ ] Local
    - [ ] Global
    - [ ] Enclosing
    - [x] **Package**
        > Packages do not define a scope, they are external installations that we bring to extend code functionality.

4. Which of the following is a built-in data structure in Python?
    - [ ] Tree
    - [ ] Queue
    - [ ] LinkedList
    - [x] **Set**
        > Set is a built-in data structure such as list, tuple, etc.

5. For a given file called ‘names.txt’, which of the following is NOT a valid syntax for opening a file:
    - [ ] with open('names.txt', 'r') as file:<br/>print(type(file))
    - [ ] with open('names.txt', 'w') as file:<br/>print(type(file))
    - [ ] with open('names.txt', 'rb') as file:<br/>print(type(file))
    - [x] **with open('names.txt', 'rw') as file:<br/>print(type(file))**
        >  It should either be ‘r’ mode for reading or ‘w’ mode for writing.

6. Which among the following is not a valid Exception in Python?
    - [ ] ZeroDivisionException
    - [ ] FileNotFoundError
    - [ ] IndexError
    - [x] **LoopError**
        > There is no such Exception defined in Python.

7. For a file called **name.txt** containing the lines below:
<br/>&emsp;First line<br/>&emsp;Second line<br/>&emsp;And another !<br/>What will be the output of the following code:<br/>&emsp;with open('names.txt', 'r') as file:<br/>&emsp;&emsp;lines = file.readlines()<br/>&emsp;print(lines)<br/>
    - [ ] 'First line'
    - [x] **['First line\n',<br/>'Second line\n',<br/>'And another !']**
    - [ ] ['First line']
    - [ ] 'First line'<br/>'Second line'<br/>'And another !'
        > readlines() returns an ordered list with lines in the text file as items in the list. 
    
8. State TRUE or FALSE:<br/>*args passed to the functions can accept the key-value pair.
    - [ ] True
    - [x] **False**