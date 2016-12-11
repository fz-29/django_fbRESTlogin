#Facebook REST Login API - Django

This repository contains Boilerplate code for REST API Facebook login in Django using django-rest-auth.

-> Authenticate via. Facebook Login <br>
-> Token Based Approach ( Not session based ) <br>

How it takes place : 

1. Front End Side


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