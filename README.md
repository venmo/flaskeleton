BLAH! Flaskeleton - a plug-and-play Flask app so you can get to the fun stuff, fast.
===============================================================================

Uses Bootstrap, Jinja2 and jQuery.

Includes examples for making POST requests using html forms and AJAX.

Also includes an information on how to make a Venmo app and implement server-side OAuth!

Venmo API documentation available [here](http://venmo.com/api).

Flask documentation available [here](http://flask.pocoo.org/)

Bootstrap documentation available [here](http://getbootstrap.com/)

Jinja2 documentation available [here](http://jinja.pocoo.org/docs/)

jQuery documentation available [here](http://jquery.com/)

Setup
-----------

Install flask and requests

    pip install flask
    pip install requests

Run a setup script to create a couple of useful constants for your app, include a key to encrypt your sessions
and placeholders for Venmo app credentials.
`python setup.py`

How to run
-----------
Go into the app main directory.
run `python main.py`
That's all (make sure you have that constants file and you installed those libraries mentioned above)!

Venmo API Integration Example
-----------------------------
This app includes an example implemention of Venmo's OAuth server-side authentication. Follow these steps to get that example working!

###Creating your Venmo app

First, if you are not signed up for Venmo, sign up for an account [here](https://venmo.com/signup).

Next, login and go to: Account > Developers > [New Application](https://venmo.com/account/app/new).

**Note: You must set the `Web Redirect URL` to http://localhost:5000/oauth-authorized so that Venmo properly redirects back to your app once a user has authenticated.**

![Create new application](https://dl.dropbox.com/u/800/Captured/GbalC.png)

You can find your app ID and secret here:
![Get app credentials](https://dl.dropboxusercontent.com/s/9gysjwne1u321fa/ExampleOAuthFlaskAppCredentials.png)

Run `python setup.py` to automatically create a constants.py file with dummy info.

If you choose to make a Venmo app later, fill in the constants.py file with this information:
<table>
    <tr>
    <td> CONSUMER_ID </td>
    <td> Your Venmo app ID e.g. 1349 **NO QUOTATION MARKS** </td>
    </tr>
    <tr>
    <td> CONSUMER_SECRET </td>
    <td> Your Venmo app secret e.g. 'E4jWCktKjvnDoIjdFwXaQuGBKPhxTDXR' </td>
    </tr>
    <tr>
    <td> APP_SECRET </td>
    <td> a random string used to encrypt your session cookies e.g. 'thisappisnice' </td>
</table>

Then run

    python main.py

Go to localhost:5000 in your browser, and log in with your Venmo credentials.

That's it
----------
We hope you use this app as a starting off point.
