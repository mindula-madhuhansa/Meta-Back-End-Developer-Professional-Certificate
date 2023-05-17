1. Which of the following is a Built-in Form Field class in Django? Select all that apply.
    - [x] **EmailField**
        > **EmailField** accepts input that follows an Email format.
    - [ ] StringField
    - [x] **URLField**
        > It accepts a string input as per the URL format.
    - [x] **IntegerField**
        > The **IntegerField** accepts inputs that are only integers.

2. When the Submit button is pressed on a form created from a template in Django, which of the following requests is triggered by default?
    - [ ] GET
    - [ ] PUT
    - [x] **POST**
        > On Submit, The POST method is triggered. The browser then bundles up the form data, encodes it for transmission, sends it to the server, and receives its response.

3. Which of the following code snippets is correct to import the form properties of a form created using the form class?
    - [x] `from django.forms import Form`
    - [ ] `from django.forms import forms`
    - [ ] `from django.forms import Forms`
        > This statement imports the Form class and subclass to define HTML form elements.

4. Suppose you create a model for a reservation system that contains fields for name, seats and notes.<br/>When using Model Forms, which of the following is an acceptable value for the field attribute inside the class Meta?
![model form](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/da924929-6ef8-449a-b35f-413a30412f08image1.png?expiry=1684454400000&hmac=4Vd0SMYkIyIs0060hdMVc7O9FrnV-QGFqMhGLKLgjzc)

    - [x] **"__ all__" as well as specific field names: **["name", "seats", "notes"]**
    - [ ] Only **"__ all__"**, field names cannot be specified.
    - [ ] Only specific field names can be specified, and no string value such as **"__ all__"**.
        > The string value of **"__ all__"** will include all the attributes inside the parent model, and the specific fields can also be passed inside a list object.

5. True or false. When creating a form using either of the classes, Form or **ModelForm**, will the argument passed inside the class be the same? For example:<br/>
`#Create Form`<br/>
`class SampleForm(forms.Form):`<br/><br/>
`#Create ModelForm`<br/>
`class SampleModelForm(forms.Form):`<br/>
    - [ ] Yes
    - [x] **No**
        > The Model Form is passed as an argument **ModelForm** which is imported from **django.forms**, while a standard web-based form is passed through the argument **forms.Form** and imported from the django module.
