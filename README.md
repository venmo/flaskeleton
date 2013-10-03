Venmo OAuth Flask Example
===========

An example server-side implementation of obtaining a long-lived access token for Venmo OAuth. 

Venmo API documentation available [here](http://venmo.com/api).

Setup
-----------

Install flask and requests 

    pip install flask
    pip install requests

Create a new Venmo Application by visiting https://venmo.com/

Login and go to: Account > Developers > [New Application](https://venmo.com/account/app/new).

![Create new application](https://dl.dropbox.com/u/800/Captured/GbalC.png)

You can find your app ID and secret here:
![Get app credentials](https://dl.dropboxusercontent.com/s/9gysjwne1u321fa/ExampleOAuthFlaskAppCredentials.png)


Clone this repo and cd into the venmo-flask directory.
Create a constants.py file with these definitions:

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
