1. What function allows reading and writing files in Python?
    - [ ] read_write()
    - [ ] input()
    - [x] **open()**
    - [ ] output()
        > open() both reading and writing of files.

2. Which method allows reading of only a single line of a file containing multiple lines?
    - [ ] readall()
    - [ ] readlines()
    - [ ] read()
    - [x] **readline()**
        > Readline allows the reading of a single line of a file.

3. What is the default mode for opening a file in python?
    - [ ] write mode
    - [x] **read mode**
    - [ ] copy mode
    - [ ] read and write
        > By default, the file is opened in read mode.

4. What is the difference between write and append mode?
    - [ ] Nothing, they are both the same.
    - [x] **Write mode overwrites the existing data. Append mode adds new data to the existing file.**
    - [ ] Write mode will append data to the existing file. Append will overwrite the data.
    - [ ] Write mode will not allow edits if content already exists. Append mode will add new data to the file.
        > Both write and append mode serve different use-cases!

5. What error is returned if a file does not exist?
    - [ ] Exception
    - [x] **FileNotFoundError**
    - [ ] AssertionError 
    - [ ] LookupError
        > The FileNotFoundError is returned when a file cannot be found.