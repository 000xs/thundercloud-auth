from flask import Flask, render_template, request, jsonify,make_response
from database import Database
from utils import generate_token, verify_token

app = Flask(__name__)
database = Database()

@app.route("/")
def index():
    return render_template("index.html")  # your homepage

@app.route("/signup")
def signup():
    return render_template("signup.html")  # your signup form

@app.route("/login")
def login():
    return render_template("login.html")  # your login form

@app.route("/auth/signup", methods=["POST"])
def api_signup():
    username = request.form.get("username")
    password = request.form.get("storm_sequence")  # already converted :name: format from frontend

    if not username or not password:
        return jsonify({"error": "Missing username or storm sequence"}), 400

    user_id = database.adduser(username, password)
    if not user_id:
        return jsonify({"error": "Username already exists"}), 409

    return jsonify({"message": f"Welcome to the Storm Kingdom, {username}!", "user_id": user_id})

@app.route("/auth/login", methods=["POST"])
def api_login():
    username = request.form.get("username")
    password = request.form.get("password")  # already converted :name: format from frontend

    if not username or not password:
        return render_template('auth/error.html', message="Invalid username or password")
         

    user = database.verify_user(username, password)
     

    if user:
        resp =  make_response(render_template('auth/success.html', message=f"Welcome back, {username}!"))
        resp.set_cookie('token', generate_token(user[0],username))
        return resp
         
    else:
        return render_template('auth/error.html', message="Invalid username or password")
        
        # return jsonify({"error": "Invalid username or password"}), 401


@app.route('/account')
def account():
    token = request.cookies.get('token')
    
    userdata = verify_token(token)
    
    user = database.validate_user(userdata)
    
    
    return render_template('account.html', username=userdata['user_name'], storm_sequence=userdata['user_id'])
    # return jsonify(user)
