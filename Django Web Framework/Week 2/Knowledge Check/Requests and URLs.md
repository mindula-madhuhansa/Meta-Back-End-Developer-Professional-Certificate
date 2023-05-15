1. Complete the following sentence. A view function returns an object of the HttpResponse class. It is imported from________.
    - [ ] The django.urls module
    - [ ] The django.db module
    - [ ] The django.http module
    - [x] **The django.contrib module**
        > This module defines **HttpRequest** and **HttpResponse** classes, their attributes and methods.

2. True or False. More than one URL pattern may be mapped to a single view function.
    - [x] **True**
    - [ ] False
        > In the **urlpatterns** list of the **urls.py** file, it is possible to add a path that has more than one endpoint pointing to the same view function.

3. Complete the following sentence. The view function obtains the body parameters in the client’s request with its ______________ attribute.
    - [ ] request.GET
    - [x] request.POST
    - [ ] request.FILES
    - [ ] request.method
        > When an HTML form submits data with the POST method, it is added to the body of the HTTP request. Inside the view function, the **request.POST** attribute fetches the form data for further processing.

4. Assuming that the client URL endpoint is http://127.0.0.1:8000/product/keyboard/500/, which of the following statements will correctly parse the path parameters? Select all that apply.
    - [ ] `path('product/<name>/<float:price>', views.addproduct)`
    - [x] `path('product/<name>/<price>', views.addproduct)`
        > Django captures the values from the URL into the variables in angular brackets. The variable is of str type by default, if any converter is not used. Hence name= **keyboard** and price = **500** sting variables passed to the **addproduct** view function.
    - [x] `path('product/<str:name>/<int:price>', views.addproduct)`
        > Both the variables are using path converters explicitly. Hence, name is a string and price is an integer.
    - [x] `path('product/<name>/<int:price>', views.addproduct)`
        > The use of **int** path converter stores integer 500 in price. Name stores the **str** value by default.

5. What are the types of parameters that a view receives in a client request? Select all that apply.
    - [x] **Query parameters**
        > The URL may have a query string appended to the endpoint. The parameters are available to the view in **request.GET** attribute.
    - [ ] URL parameters
    - [x] **Body parameters**
        > The data items sent by the client with POST method are the body parameters of the request. The **request.POST** attribute contains this data.
    - [x] **Path parameters**
        > If the client URL endpoint contains one or more parameters separated by the **/** symbol, the path converter in **path()** function’s URL pattern string parses the parameters in appropriate variables. Then, it passes them to the view function.
