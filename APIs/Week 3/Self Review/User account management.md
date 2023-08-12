1. Inside the **Meta** class for **RatingSerializer**, you defined a variable such as: **queryset = User.objects.all()**. Inside which of the following configuration options did you define this?

   - [ ] model
   - [x] **validators**
   - [ ] extra_kwargs
   - [ ] fields
     > validators is a messages argument that is used to enforce **unique_together** constraints on model instances.

2. Which of the following options should you add to the **urlpatterns** inside the **path()** function to configure the **RatingsView()** class?

   - [x] `views.RatingsView.as_view()`
   - [ ] `RatingsView.as_view()`
   - [ ] `RatingsView.views.as_view()`
   - [ ] `views.RatingsView`
     > The **RatingsView** class is inside the **views.py** file and uses the **as_view()** function to return a callable view.

3. Which of the following configuration options do you need to add as strings inside the **INSTALLED_APPS** list in the **settings.py** file? Select all that apply.
   - [x] **`djoser`**
     > **djoser** is a library that you imported to performs REST implementation of the Django authentication system and therefore must be added to the **INSTALLED_APPS** list.
   - [ ] `LittleLemon`
   - [x] **`rest_framework`**
     > **rest_framework** needs to be added as a configuration to utilize functionalities inside the Django rest framework module.
   - [x] **`rest_framework.authtoken`**
     > **rest_framework.authtoken** will access the subpackage **authtoken** and it needs to be added inside the **INSTALLED_APPS** option.
