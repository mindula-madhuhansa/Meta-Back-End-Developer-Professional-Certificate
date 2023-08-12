1. In the model **MenuItem** that you created, you used the **ForeignKey()** class to create a many-to-one relationship with the model **Category**. Which of the options below was the value set for the attribute **on_delete** that preserves the referenced object?

   - [ ] `models.SET_NULL`
   - [ ] `models.SET_DEFAULT`
   - [ ] `models.CASCADE`
   - [x] **`models.PROTECT`**
     > **models.PROTECT** prevents deletion of the referenced object. The value for **on_delete** is set to this value because you don’t want the entries inside the **Category** class deleted on deletion of some menu item.

2. The setup for the **PageNumberPagination** style that you configured inside the **DEFAULT_PAGINATION_CLASS** configuration settings is part of the sub-package **rest_framework.filters**

   - [ ] True
   - [x] **False**
     > **rest_framework.pagination** is the subpackage containing the style options **PageNumberPagination**

3. The **generics.ListCreateAPIView** is passed as an argument inside which of the following views?

   - [x] Both **MenuItemsView** and **CategoriesView**
   - [ ] Only **CategoriesView**
   - [ ] Neither **MenuItemsView** or **CategoriesView**
   - [ ] Only **MenuItemsView**
     > Both classes will use the **generics.ListCreateAPIView** to create read-write endpoints that will represent collection of model instances.
