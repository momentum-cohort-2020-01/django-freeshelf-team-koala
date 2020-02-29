Project CRC Model

1. Create project name = django-admin startproject bigfarma .
   a. Add data.py (book list)
2. Create project app = django-admin startapp store
3. Within bigfarma,
   a. Add app name to settings.py
   b. Add urls to urls.py
4. Within appname,
   a. Migrations folder
   i. Perform python manage.py makemigrations (after models.py created/updated)
   ii. Perform python manage.py migrate (after models.py created/updated)
   b. Static/base folder
   i. Create css folder
5. Create style.css
   ii. Create img folder
6. Create placeholder jpg for out-of-stock item

7. Get main page header jpg for main page
8. Get jpg for mobile phone

c. Templates folder
i. registration folder

1. activate.html
2. activation_complete.html
3. activation_email.txt
4. activation_email_subject.txt
5. login.html
6. logout.html
7. registration_complete.html
8. registration_form.html
   ii. store folder
9. cart.html
10. detail.html
    iii. base.html
    iv. template.html
    d. Add models.py
    e. Add urls.py
    f. Add views.py
