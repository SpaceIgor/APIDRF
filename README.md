For run this project you need use following steps:

1.Open your terminal, go to Desktop or another folder by 'cd' command;

2.Paste in terminal:'https://github.com/SpaceIgor/APIDRF.git'

3.Creating and activate your virtualenv - for windows:
python -m venv <name_of_virtualenv>    =>   <name_of_virtualenv>/Script/activate

4.Back to previos folder wich includes manage.py and run: 
"pip install --upgrade pip"     =>    "pip install -r requirements.txt";

5.Download XAMPP for Windows with MySQL:
https://www.apachefriends.org/blog/news-article-61070.html

6.Activate modules in XAMPP:    Apache and MySQL
You can see how to connect it with django in the next video, if something didn’t work out for you:
https://www.youtube.com/watch?v=yWD0yDMouVY
To see your databases you can view them at:    http://localhost/phpmyadmin

7.Run this command for adding tables in your database: 
"python manage.py makemigrations"   =>    "python manage.py migrate"

8.Create superuser:
python manage.py createsuperuser

9.After all dependencies will install run this command:
python manage.py runserver

We have access to urls:
    http://127.0.0.1:8000/ - home page
    http://127.0.0.1:8000/admin/ - admin page

API PAGE
    http://127.0.0.1:8000/api/v1/ - main API page
    
There you will see page with this urls:

DirectionList:
    http://127.0.0.1:8000/api/v1/direction_list/

    In direction page you can only create a direction; for looking how use url filters click on filters button then press needed filters or sort and after just check url it will be change for your filters

DoctorList:
    http://127.0.0.1:8000/api/v1/doctor_list/
    
    In doctor page you can add new doctors, and ordering, searching, filtering by filter button, and also you can do same thing by using url;