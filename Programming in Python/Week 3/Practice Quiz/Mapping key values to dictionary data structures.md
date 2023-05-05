1. What will be the output of the following code:
<br/>a = [[96], [69]]<br/>print(''.join(list(map(str, a))))
    - [x] **"[96][69]"**
    - [ ] "[96],[69]"
    - [ ] [96][69]
    - [ ] "9669"
        > It will initially be a list of strings such as ['[96]', '[69]'] which is then converted into a conjoined string. 

2. Which of the following is **TRUE** about the map() and filter() functions?
    - [ ] The map() function is built-in, but the filter() function needs to be defined first.
    - [ ] The map() function needs to be defined first, but the filter() function is built-in.
    - [ ] Both the map() and filter() functions need to be defined before we use them.
    - [x] **Both the map() and filter() functions are built-in.**
        > Function you pass to filter() and map() function may need definition, but they both are built-in.

3. What will be the output of the following code:
<br/>&emsp;z = ["alpha","bravo","charlie"]<br/>&emsp;new_z = [i[0]*2for i in z]<br/>&emsp;print(new_z)
    - [ ] ['aa'], ['bb'], ['cc']
    - [x] **['aa', 'bb', 'cc']**
    - [ ] ['a', 'b', 'c']
    - [ ] ['alphaalpha', 'bravobravo', 'charliecharlie']
        > The output will be a list of strings.