# customuser
Author Chris Wilson
Worked with Koren and Sean. 
Used reference-https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html

Project name Custom Users:
There are two ways to extend users in Django: the "profile" method and a custom user. We've already used the profile method for our first project, so now we'll cover the custom user.

This project is simply about implementing a custom user from the ground up so that you can use it in the next assignment.

Your Task
Implement your own login and signup page (don't use the defaults) for the server that leads to a locked-down "homepage". The homepage should show:

the username & display name of the person who is logged in
output the value of `settings.AUTH_USER_MODEL`
NOTE: DO NOT name any part of your app "user" -- it will have conflict with the built-in user model and give you all sorts of errors that are really difficult to debug if you don't know what you're looking for. Use "custom_user", "myuser", "dudewheresmyuser"... literally anything but "user" will work.

Extra Credit (2 points)

Extend your custom user field so that it has the following nullable fields:

Homepage (URLField)
Age (IntegerField)
Extra Credit (1 point)

(this is the hard part) Make the custom fields appear on the admin panel and available for editing. 1 additional bonus point if you make the superuser command ask for their age.