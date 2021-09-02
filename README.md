# Todolist API

## 💻 Project

This project is a simple API for register a task.
- It has a token authentication system.
- Only authenticated users can use the API.
- The user must be able to register new tasks, and edit or delete only his own.
- It has a registration screen (optional, if you don't want to use the admin or shell to create a user)

Below Screenshot from the browsable API:
![image](/readme_img/main_screen.png?raw=true "Main_Screen")

## 🚀 Technologies

This project was developed with the following tecnologies:
- Python 3.9.6
- Django 3.2.6
- Django Rest Framework 3.12.4

The reason for choosing Django and Django Rest Framework was the practicality and productivity for the creation of REST API's, besides particularly liking these tools. 🥰

The database used for this application was `sqlite3`. Because it is already installed and configured with Django, it makes the development a lot easier.

## ℹ️ How to use

**1. Preparing the environment**

I recommend using a [virtualenv](https://virtualenv.pypa.io/en/latest/) to run the application locally. 

Virtualenv is already included in standard library of the Python3. You can create a virtual environment using the command below:
```
python3 -m venv venv
```
Activate your virtual environment
```
(Unix or MacOS) $ source venv/bin/activate
(Windows) ...\> env\Scripts\activate.bat
```
With the virtual environment activated, install the dependencies that are in the requirements.txt file, using the command below:
```
pip install -r requirements.txt
```
Migrate the models to the database
```
./manage.py makemigrations
./manage.py migrate
```
Run the application
```
./manage.py runserver
```
**2. Registration and Authorization**

The application has authentication by token and session, so it's necessary to create a user and then access the API with the token or using login and password (browsable API)

- Creating user

You can create a user via the `/api/signup` route. Or if you prefer, create a superuser using the terminal, with the command.
```
(venv) $ ./manage.py createsuperuser
```
- Accessing the application using the token

After user created, you need to request a token. Send a post request to the address /api-token which will return a Json response with the token, if the user is authenticated correctly.

Example with Postman
![image](/readme_img/postman_post_api-token.png?raw=true "postman_post_api-token")

You can also make this request using python's requests library.
```
import requests

url = "http://localhost:8000/api-token/"
payload={'username': 'USERNAME', 'password': 'PASSWORD'}
response = requests.request("POST", url, data=payload)
print(response.text)

out: {"token":"ae63b18092790b29cc7a58eb573be05ad5954b2d"}
```

With the token you can normally use the API, remembering to pass the token in the header with the Authorization key and value 'Token <token>' For more details on how to use the token you can check the [DRF documentation](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication)

- If you want to use the browsable API (which is much more interesting) you can authenticate by entering the username and password created earlier
![image](/readme_img/drf_api_login_screen.png?raw=true "drf_api_login_screen")
![image](/readme_img/drf_login_screen.png?raw=true "drf_login_screen")

**3. In operation**
  
Example of creating a task (with Postman):
  
![image](/readme_img/postman_post_api-todolist.png?raw=true "postman_post_api-todolist")

Update a task (with browsable API)
![image](/readme_img/drf_put_api_todolist_id.png?raw=true "drf_put_api-todolist_id")

If the user tries to update or delete a task that he did not create himself, it will not succeed and will display an error message.
![image](/readme_img/drf_put_api_todolist_id_response_error.png?raw=true "drf_put_api-todolist_response_error_id")
![image](/readme_img/drf_delete_api_todolist_id_response_error.png?raw=true "drf_delete_api-todolist_response_error_id")

The API has ordering by delivery date and searching by username. To access this resource, pass this information by parameter.
```
/api/todolist/?ordering=date&search=marco
```

## Endpoints and Features

- Register:
  - `(POST)/signup`
- Get token for API access
  - `(POST)/api/token`
- List all task
  - `(GET) /api/todolist/`
- Create new task
  - `(POST) /api/todolist/`
- Show an specific task
  - `(GET) /api/todolist/{id}/`
- Update a specific task
  - `(PUT) /api/todolist/{id}/`
  - `(PATCH) /api/todolist/{id}/`
- Delete an specific task
  - `(DELETE) /api/todolist/{id}/`

👀 For more information about endpoints, see the documentation on endpoint `(GET)/api/doc/`

## 🗄️ Deploy
Deploy was made using Heroku. For mor details see the [documentation](https://devcenter.heroku.com/categories/python-support)

Link to App:
https://todolist-api-evoe.herokuapp.com/api/

**OBS:** To login you can use **username: evoe** and **password: todolistevoe**
  
## 📎 Versioning

1.0.0.0

## 🧔 Authors

* **Marco Capozzoli**: @marcocapozzoli (https://github.com/marcocapozzoli)

## 📚 Referências
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Django](https://www.djangoproject.com/)
- [Swagger](https://drf-yasg.readthedocs.io/en/stable/)
