from flask import Flask, request, session, render_template, jsonify, redirect, url_for
from constants import CONSUMER_ID, CONSUMER_SECRET, APP_SECRET
import requests

app = Flask(__name__)
# comment out when you're done testing
app.debug = True
app.secret_key = APP_SECRET

@app.route('/')
def index():
    if session.get('venmo_token'):
        data = {'name': session['venmo_username'],
            'access_token': session['venmo_token'],
            'signed_in': True}
        return render_template('index.html', data=data)
    else:
        data = {'signed_in': False,
        'consumer_id': CONSUMER_ID}
        return render_template('/index.html', data=data)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/make_post', methods=["POST"])
def make_post():
    message = request.form['message']
    return render_template('/make_post.html', message=message)

@app.route('/ajax_post', methods=["POST"])
def ajax_post():
    message = request.form['message']
    print request.form
    if not message:
        return jsonify({"message":"Please include a message!"}), 400
    response_message = "Hey, your message was %s" % message
    return jsonify({"message": response_message})

@app.route('/make_payment', methods=["POST"])
def make_payment():
    access_token = request.form['access_token']
    note = request.form['note']
    payload = {"access_token":access_token,
            "note":note,
            "amount":.10,
            "user_id":153136}
    url = "https://sandbox-api.venmo.com/payments"
    response = requests.post(url, payload)
    data = response.json()
    return jsonify(data)

@app.route('/get_payments', methods=["GET"])
def get_payments():
    access_token = request.args.get('access_token')
    url = "https://sandbox-api.venmo.com/payments?access_token=" + access_token
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

@app.route('/oauth-authorized')
def oauth_authorized():
    AUTHORIZATION_CODE = request.args.get('code')
    data = {
        "client_id":CONSUMER_ID,
        "client_secret":CONSUMER_SECRET,
        "code":AUTHORIZATION_CODE
        }
    url = "https://api.venmo.com/oauth/access_token"
    response = requests.post(url, data)
    response_dict = response.json()
    access_token = response_dict.get('access_token')
    user = response_dict.get('user')

    session['venmo_token'] = access_token
    session['venmo_username'] = user['username']

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
