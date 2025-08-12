from flask import Flask, render_template, request, jsonify, make_response,redirect,url_for
from database import Database
from utils import generate_token, verify_token, password_hash, valid_hashed_password

app = Flask(__name__)
database = Database()

# midelware 
@app.before_request
def check_authentication():
    protected_paths = ['/account']  

    if request.path in protected_paths:
         
        token = request.cookies.get('token')
        if not token or not verify_token(token):
            return render_template("unauthorized.html") # Unauthorized
            
@app.route("/")
def index():
    """Displays the homepage."""
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
    )  
    if not username or not password:
        return render_template("auth/signup/error.html", message="Missing username or storm sequence")
       

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
    ):  
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

    if not userdata:
        return render_template('unauthorized.html')
    
    user = database.validate_user(userdata)

    if not user:
        return render_template('unauthorized.html')

    users_progress = database.get_all_users_progress()

    return render_template(
        "account.html",
        username=userdata["user_name"],
        scores=user[3],
        storm_sequence=userdata["user_id"],
        users=users_progress
    )

@app.route("/logout")
def logout():
    """Delete the cookie and redirect to root."""
    resp = make_response(redirect(url_for("index")))
    
    resp.delete_cookie("token")
    return resp

@app.route("/update_score", methods=["POST"])
def update_score():
    token = request.cookies.get("token")
    userdata = verify_token(token)
    if not userdata:
        return jsonify({"error": "Unauthorized"}), 401

    score = request.json.get("score")
    if score is None:
        return jsonify({"error": "Missing score"}), 400

    database.update_user_score(userdata["user_id"], score)
    return jsonify({"success": True})
