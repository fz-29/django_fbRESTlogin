#Facebook REST Login API - Django

This repository contains Boilerplate code for REST API Facebook login in Django using django-rest-auth.

-> Authenticate via. Facebook Login <br>
-> Token Based Approach ( Not session based ) <br>

### How it takes place : 

POST 127.0.0.1:8000/rest-auth/facebook/

1. Front End Side
	* use JS SDK, to receive access_token associated with the user and the corressponding app.

2. send the access_token to our Django REST API server
	
3. Our API server	
	* our server sends this access_token to FB server, and authenticats access_token.
	* on success
		* if new user it fetches info about the user which presents the access_token, and inserts user to 'Social Accounts'
		* insert the access_token and update key(token like entity for our server verifcation, to avoid repeated FB calls)
	* sends back	


### Procedure for Code: 

1. pip install django-rest-auth
2. Initialize Django Project
3. Create super user and then migrate
4. Check and run admin page
5. Follow steps at [django-rest-auth : Documentation](http://django-rest-auth.readthedocs.io/en/latest/installation.html#social-authentication-optional)
	* Add new apps to settings.py
	* Migrate
	* Now, add Add Social Application in django admin panel. (Add App Name, Client ID and Key)
	* Create new view as a subclass of rest_auth.registration.views.SocialLoginView with FacebookOAuth2Adapter adapter as an attribute
	* Create url for FacebookLogin view.

### Procedure for Gaining Token: 
	* Send a POST REQUEST with access_token. (POST[URL] & BODY->x-www-form-urlencode & access_token : <access_token received from Facebook>)
	* Django Server Receieves and authenticates from FB server.
	* Django server genarates its own key for that user and return it as response.