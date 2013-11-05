Flaskeleton - plug-and-play so you can get to the fun stuff, fast.
===============================================================================

A Flask app that has everything you need to interact with an OAuth API baked in. Build your own app off of it by cloning and modifying it to your heart's desire!

Currently uses the Venmo OAuth API as example. Also includes examples for making POST requests using html forms and AJAX. Uses Bootstrap, Jinja2 and jQuery.

Venmo API documentation available [here](http://venmo.com/api).

Flask documentation available [here](http://flask.pocoo.org/).

Bootstrap documentation available [here](http://getbootstrapcom/).

Jinja2 documentation available [here](http://jinja.pocoo.org/docs/).

jQuery documentation available [here](http://jquery.com/).

Setup
-----------
Clone this repo to a local directory on your computer. Navigate to the directory.

Install flask and requests

    pip install flask
    pip install requests

Run a setup script to create a couple of useful constants for your app, include a key to encrypt your sessions
and placeholders for Venmo app credentials. These are used in "Venmo API Integration Example" below.
`python setup.py`

How to run
-----------
Go into the app main directory and
run `python main.py`
That's all (make sure you have that constants file, constants.py, and you have installed those libraries mentioned above)!

Venmo API Integration Example
-----------------------------
This app includes an example implemention of Venmo's OAuth server-side authentication. Follow these steps to get that example working!

###Creating your Venmo app

First, if you are not signed up for Venmo, sign up for an account [here](https://venmo.com/signup).

Next, login and go to: Account > Developers > [New Application](https://venmo.com/account/app/new).

**Note: When doing local development, you must set `Web Redirect URL` to http://localhost:5000/oauth-authorized so that Venmo properly redirects back to your app once a user has authenticated. When deploying to a cloud platform like Heroku, change the web redirect URL to the location of your Heroku app.**

![Create new application](https://dl.dropboxusercontent.com/s/ffo01uzr65y9kzw/GbalC.png)

Now, fill in the constants.py file with this information:
<table>
    <tr>
    <td> CONSUMER_ID </td>
    <td> Your Venmo app ID e.g. 1349 (do not include the quotes) </td>
    </tr>
    <tr>
    <td> CONSUMER_SECRET </td>
    <td> Your Venmo app secret as a string e.g. 'E4jWCktKjvnDoIjdFwXaQuGBKPhxTDXR' </td>
    </tr>
    <tr>
    <td> APP_SECRET </td>
    <td> A random string used to encrypt your session cookies e.g. 'thisappisnice' </td>
</table>

Then run

    python main.py

Go to localhost:5000 in your browser and follow the instructions there!

That's it!
----------
We hope you use this app as a starting off point.
