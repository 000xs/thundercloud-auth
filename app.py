from flask import Flask, render_template, request, jsonify, make_response,redirect,url_for
from database import Database
from utils import generate_token, verify_token, password_hash, valid_hashed_password

app = Flask(__name__)
database = Database()


@app.route("/")
def index():
    return render_template("index.html")   


@app.route("/signup")
def signup():
    return render_template("signup.html")  


@app.route("/login")
def login():
    return render_template("login.html") 


@app.route("/auth/signup", methods=["POST"])
def api_signup():
    username = request.form.get("username")
    password = request.form.get(
        "storm_sequence"
    )  # already converted :name: format from frontend

    if not username or not password:
        return render_template("auth/signup/error.html", message="Missing username or storm sequence")
       
        # return jsonify({"error": "Missing username or storm sequence"}), 400
    # turn password to hashed varible
    hash_password = password_hash(password)

    user_id = database.adduser(username, hash_password)
    if not user_id:
        return render_template("auth/signup/error.html", message="Username already exists")
        # return jsonify({"error": "Username already exists"}), 409

    
    
    return render_template(
            "auth/signup/success.html",  
            message=username
        )


@app.route("/auth/login", methods=["POST"])
def api_login():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    user = database.verify_user(username)

    if user and valid_hashed_password(
        password, user[2]
    ):  # user[2] is stored hashed password
        resp = make_response(
            render_template("auth/login/success.html", message=f"Welcome back, {username}!")
        )
        resp.set_cookie("token", generate_token(user[0],user[1]))
        return resp
    else:
        return (
            render_template("auth/login/error.html", message="Invalid username or password"),
            401,
        )


@app.route("/account")
def account():
    token = request.cookies.get("token")

    userdata = verify_token(token)

    user = database.validate_user(userdata)

    return render_template(
        "account.html",
        username=userdata["user_name"],
        storm_sequence=userdata["user_id"],
    )
    # return jsonify(user)
@app.route("/logout")
def logout():
    """Delete the cookie and redirect to root."""
    resp = make_response(redirect(url_for("index")))
    
    resp.delete_cookie("token")
    return resp
   
