1. In the lab you completed, the file for adding the URL configuration called **urls.py** was created inside which directory?
    - [ ] The initial working directory called **myproject**.
    - [ ] myproject
    - [x] **myapp**
        > The **myapp** directory hosts the additional **urls.py** file you create and is separate from the **urls.py** file created by default inside the project directory.

2. To enable using URL configurations in the **urls.py** file at the app-level, you have to import the **include()** and **path()** functions inside which file?
    - [ ] Functions don't need to be imported at either app-level or project-level **urls.py** file
    - [ ] the app-level urls.py file.
    - [x] **the project-level urls.py file.**
    - [ ] Both app-level and project-level **urls.py** file.
        > The app-level **urls.py** file gets updated with URL configuration that can be referenced using the **include()** function by passing the location of the app-level **urls.py** file to it as an argument. The path function has to be imported in both the files.

3. Among the path configurations you added inside the app-level **urls.py** file, one of them is for the view function called **Menu**. What was the string added as the first parameter inside the path function associated with it?
    - [ ] “/menu”
    - [ ] “menu”
    - [ ] “Menu/”
    - [x] **“menu/”**
        > This is ideally how we pass the string argument for the URL path associated with the view for the menu page.
