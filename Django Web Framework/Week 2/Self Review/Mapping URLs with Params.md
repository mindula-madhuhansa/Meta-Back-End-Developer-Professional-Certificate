1. True or false. The URL parameter present in the **urls.py** file such as **<int:drink>** has to match the object passed to the view such as **drink** inside **views.py** file.
    - [x] **True**
    - [ ] False
        > The matching enables Django to map the URL parameter to the correct view and appropriate data type.

2. True or false. In the lab you created, you defined a URL with a parameter inside the path() function in the **urls.py** file of **myapp**. When defining a view function in the **views.py** file, you must pass an additional argument along with the request object.
    - [x] **True**
    - [ ] False
        > Django expects to receive more than the request object after mapping the URL path. If not, it will throw an error. The number of arguments inside a view other than the **request** object must match the parameters passed inside the **path()** function.

3. In the lab you completed, what would be the effect on the code if you had not included the the string **drinks/** in the app-level path function inside **urls.py** file? For example:
<br/>`urlpatterns = [`<br/>
&emsp;`path('<str:drink_name>', views.drinks, name="drink_name"),`<br/>
`]`<br/>
    - [ ] Both the view and URL path will change.
    - [ ] The view and URL will remain unchanged.
    - [ ] The view will change but URL remains unchanged.
    - [x] **The view remains unchanged but URL path will change.**
        > The view is independent of the path set except for URL parameters and will remain unchanged. The URL will change in line and will be accessible at for example: http://127.0.0.1:8000/mocha
