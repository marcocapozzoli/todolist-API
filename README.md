# Todolist API

## 💻 Project

Below Screenshot from the browsable API:
![image](/readme_img/main_screen.png?raw=true "Main_Screen")

## 🚀 Technologies

This project was developed with the following tecnologies:
- Python 3.9.6
- Django 3.2.6
- Django Rest Framework 3.12.4

The reason for choosing Django and Django Rest Framework was the practicality and productivity for the creation of REST API's, besides particularly liking these tools. 🥰

The database used for this application was `sqlite3`. Because it is already installed and configured with Django, it makes development a lot easier.

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

The application has authentication by token and session, so it is necessary to create a user and then access the api with the token or using login and password

- Creating user

You can create a user via the `/api/signup` route. Or simply create a superuser directly in the terminal using the command:
```
(venv) $ ./manage.py createsuperuser
```
- Accessing the application using the token

After user created, you need to request a token, making a post request to the address `/api-token` which will return Json with the token, if the user is authenticated correctly

Example with Postman
![image](/readme_img/postman_POST_api-token.png?raw=true "Postman Post_api-token")

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

Example with Postman:
![image](/readme_img/Postman_GET_api-buy.png?raw=true "Postman Get_api/buy")

- If you want to use the navigable API (which is much more interesting) you can authenticate by entering the username and password created earlier
![image](/readme_img/drfweb_noauthentication.png?raw=true "drfweb noauthentication")
![image](/readme_img/drfweb_login_screen.png?raw=true "drfweb login_screen")

**3. In operation**
  
Example of creating a purchase (with Postman):
![image](/readme_img/Postman_Post_api-buy.png?raw=true "Postman Post api/buy")

If the data is correct they will be saved and a request to the external API, which will generate the cashback. *Reply from the post request made by the retailer's customer will be the reply from the external API.*
```Json
```
 

## Endpoints and Features

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

## 📎 Versioning

1.0.0.0

## 🧔 Authors

* **Marco Capozzoli**: @marcocapozzoli (https://github.com/marcocapozzoli)

## 📚 Referências
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Django](https://www.djangoproject.com/)
- [Swagger](https://drf-yasg.readthedocs.io/en/stable/)
