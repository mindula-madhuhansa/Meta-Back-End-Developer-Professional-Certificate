1. How do you accept a GET, POST and PUT call to a function-based view using an API decorator?

   - [x] `@api_view(['GET','POST','PUT'])`
   - [ ] `api_view(['GET','POST','PUT'])`
   - [ ] `@api_view('GET','POST','PUT')`
   - [ ] An API endpoint cannot accept multiple HTTP methods
     > An API view decorator function needs an @ in front of it and you can pass all the necessary HTTP method names as a list inside it.

2. What are the benefits of using a serializer? Choose all that apply.

   - [ ] It can save data to a database
   - [ ] It can automatically convert data to JSON or XML
   - [ ] It helps to authenticate API calls
   - [x] **It can convert model instances to native Python data types**
     > You can quickly convert model instances to native Python data types using serializers. These native Python data types can later be displayed as JSON and XML using renderers.
   - [x] It can validate data
     > Before saving data in the database, a serializer can validate the data according to the validation rules specified in the serializers.py file to ensure the data is proper and sufficient.
   - [x] It can convert user input and map it to models
     > This is a built-in functionality of the serializers in DRF, and it’s called Deserialization.

3. Which of the following are valid serializer classes in DRF? Choose all that apply.

   - [x] **HyperLinkModelSerializer**
     > You can use this serializer class to quickly create hyperlinked relationships between related models and display them as hyperlinks.
   - [ ] RelationshipSerializer
   - [ ] PrimaryKeySerializer
   - [x] **ModelSerializer**
     > Model serializers are used to quickly serialize models and their relationships.
   - [x] **Serializer**
     > This is the base Serializer class in DRF which can be used to serialize model instances and standalone objects.

4. You can access the data attribute of a serializer class at any time.

   - [ ] True
   - [x] **False**
     > The data attribute of a serializer class can only be accessed after the validation is done in the serializer.

5. Which of the following renderers comes with DRF by default? Choose all that apply.

   - [x] **HTML Renderer**
     > DRF comes with a few HTML renderers to help you render static and dynamic HTML content.
   - [ ] YAML Renderer
   - [x] **JSON Renderer**
     > The JSON renderer comes as a built-in package in the Django REST Framework.
   - [ ] XML Renderer

6. Which of the following statement is true about DRF?

   - [ ] Learning DRF is tough
   - [ ] DRF doesn’t work with different database engines
   - [x] DRF is built for API development
   - [ ] DRF is a standalone framework
     > Though you can use DRF to create standard HTML content, DRF is specifically built for developers to create API projects very quickly. It comes with all the necessary classes and modules like ViewSets, generic views, serializers, authentication and permissions classes and many more which API developers require frequently in their projects. DRF also has excellent documentation and a huge community of developers so getting help or support is easier.

7. Which of the following panels are available in the DDT or Django debug toolbar? Choose all that apply.

   - [x] **Profiling**
     > This panel displays the full call stack for the current request.
   - [ ] Throttle
   - [x] **Headers**
     > The headers panel lists all the headers for the current request and response.
   - [ ] Network
   - [x] **SQL**
     > This panel displays all the SQL queries executed for the current request.

8. To serialize a queryset that returns more than one item, which of the following arguments is necessary for the serializer class?

   - [ ] `related=True`
   - [x] **`many=True`**
   - [ ] `multiple_items=True`

9. Which of the following statements are true about using renderers? Choose all that apply.

   - [ ] You cannot use multiple renderers in a project
   - [ ] You cannot forcefully use a single renderer
   - [x] **If no **Accept** header is present, DRF uses JSON renderer by default.**
     > If there is no accept header present, DRF displays the output in JSON using the built-in JSONRenderer class.
   - [x] **Renderers can automatically convert the output**
     > When you load these renderer classes in the settings.py file, they will work automatically based on the Accept header that an API client sent. You don’t need to write extra code for that.
   - [x] **Renderers need an **Accept** header to work properly**
     > Based on these Accept headers DRF invokes the appropriate renderer to display the output properly.

10. How do you display related model fields as hyperlinks? Choose all that apply.
    - [ ] A ModelSerializer can do it automatically
    - [x] **Using HyperlinkedRelatedField**
      > A HyperlinkedRelatedField serializer field can display related models as hyperlinks.
    - [x] **Using HyperlinkedModelSerializer**
      > There is a special serializer class called HyperlinkedModelSerializer which can also display related models as a hyperlink.
    - [ ] Using RelationshipSerializer
