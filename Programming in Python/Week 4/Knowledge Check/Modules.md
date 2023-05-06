1. Assuming there exists a module called ‘numpy’ with a function called ‘shape’ inside it, which of the following is NOT a valid syntax for writing an import statement? (Select all that apply)
    - [x] **import * from numpy**
        > This is an incorrect format.
    - [x] **import shape from numpy**
        > This is an incorrect format.
    - [ ] import numpy as dn
    - [ ] from numpy import *
    - [ ] from numpy import shape as s

2. Which of the following locations does the Python interpreter search for modules by default?
    - [ ] The current working directory
    - [x] **Any user-specified location added to the System path using sys package**
    - [ ] Installation-dependent default directory
    - [ ] PYTHONPATH or simply the environment variable that contains list of directories 
        > The location is accessible, but not by default.

3. We can import a text file using the import statement in Python:
   - [ ] True
   - [x] **False**
       >  Import statement can only be used for importing Python filetypes and packages.

4. Which of the following statements is NOT true about the reload() function?
   - [ ] You can use the reload() function multiple times for the same module in the given code.
   - [ ] The reload() function can be used for making dynamic changes within code.
   - [ ] You need to import a module before the reload() function can be used over it.
   - [x] **The reload() function can be used to import modules in Python.**
       > The module has to be imported separately. The reload() function cannot import module.

5. Which of the following is NOT to be considered as an advantage of modular programming while using Python?
   - [ ] Reusability
   - [ ] Scope
   - [ ] Simplicity
   - [x] **Security**
       > While some modules may supply security features, modular programming is not designed by default for security.

6. Which of the following module types are directly available for import without any additional installation when you begin writing our code in Python? (Select all that apply)
   - [ ] Third-party packages from Python Package Index not present on the device
   - [x] **Modules in the current working directory of the Project**
       > Modules in the current working directory of the project are directly available for import without any additional installation when you begin writing our code in Python.
   - [x] **Built-in modules**
       > Built-in modules are directly available for import without any additional installation when you begin writing our code in Python.
   - [ ] User-defined modules in Home directory of the device