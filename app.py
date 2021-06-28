import os
import random
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from flask_paginate import Pagination, get_page_args
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


def get_recipes_paginate(offset=0, per_page=10):
    recipes = list(mongo.db.recipes.find())
    return recipes[offset: offset + per_page]


def filter_recipes_paginate(category, offset=0, per_page=10):
    if category == "Breakfast":
        recipes = list(mongo.db.recipes.find({"category_name": "Breakfast"}))
    elif category == "Lunch":
        recipes = list(mongo.db.recipes.find({"category_name": "Lunch"}))
    else:
        recipes = list(mongo.db.recipes.find({"category_name": "Dinner"}))
    return recipes[offset: offset + per_page]


# ---------- Home Page ----------
@app.route("/")
def home():
    admin_recipes = list(
        mongo.db.recipes.find({"created_by": "admin"}))
    random.shuffle(admin_recipes)
    breakfast_recipes = list(
        mongo.db.recipes.find({"category_name": "Breakfast"}))
    random.shuffle(breakfast_recipes)
    lunch_recipes = list(
        mongo.db.recipes.find({"category_name": "Lunch"}))
    random.shuffle(lunch_recipes)
    dinner_recipes = list(
        mongo.db.recipes.find({"category_name": "Dinner"}))
    random.shuffle(dinner_recipes)
    return render_template(
        "home.html",
        admin_recipes=admin_recipes,
        breakfast_recipes=breakfast_recipes,
        lunch_recipes=lunch_recipes,
        dinner_recipes=dinner_recipes
        )


# ---------- Register Page ----------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        
        # check if the username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "firstname": request.form.get("firstname").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "saved_recipes": [],
            "profile_image": 
            "https://images.unsplash.com/photo-1528216142275-f64d7a59d8d5"
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


# ---------- Login Page ----------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        # Check if username exists in the db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # Invalid Password Match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# ---------- Profile Page ----------
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})
    recipes = list(mongo.db.recipes.find({"created_by": session['user']}))
    saved = username["saved_recipes"]
    saved_recipe = []

    for recipe_id in saved:
        recipe_id = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        saved_recipe.append(recipe_id)

    if session["user"]:
        return render_template(
            "profile.html",
            username=username,
            recipes=recipes,
            saved_recipe=saved_recipe)

    return redirect(url_for("login"))


# ---------- Delete Profile ----------
@app.route("/remove_profile")
def remove_profile():
    mongo.db.users.remove({"username": session["user"]})
    session.pop("user")
    flash("Your profile has been succesfully deleted")
    return redirect(url_for("register"))


# ---------- Log Out ----------
@app.route("/logout")
def logout():
    # Remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# ---------- Get all Recipes ----------
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    per_page = 6
    total = len(recipes)
    pagination_recipes = get_recipes_paginate(
        offset=page*per_page-per_page, per_page=per_page)
    random.shuffle(pagination_recipes)
    pagination = Pagination(page=page, per_page=per_page, total=total)
    return render_template(
        "recipes.html",
        recipes=pagination_recipes,
        page=page,
        per_page=per_page,
        pagination=pagination,
        )


# ---------- Filter Buttons ----------
@app.route("/get_recipes/<category>")
def categories(category):
    if category == "Breakfast":
        recipes = list(mongo.db.recipes.find({"category_name": "Breakfast"}))
    elif category == "Lunch":
        recipes = list(mongo.db.recipes.find({"category_name": "Lunch"}))
    else:
        recipes = list(mongo.db.recipes.find({"category_name": "Dinner"}))

    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    per_page = 6
    total = len(recipes)
    pagination_recipes = filter_recipes_paginate(
        category, offset=page*per_page-per_page, per_page=per_page)
    random.shuffle(pagination_recipes)
    pagination = Pagination(page=page, per_page=per_page, total=total)
    return render_template(
        "recipes.html",
        recipes=pagination_recipes,
        page=page,
        per_page=per_page,
        pagination=pagination,
        )


# ---------- Recipes Text Search ----------
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template(
        "search.html",
        recipes=recipes)


# ---------- Add a new Recipe ----------
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        vegetarian = "on" if request.form.get("vegetarian") else "off"
        vegan = "on" if request.form.get("vegan") else "off"
        recipe = {
            "title": request.form.get("title"),
            "description": request.form.get("description"),
            "category_name": request.form.get("category_name"),
            "cuisine": request.form.get("cuisine"),
            "vegetarian": vegetarian,
            "vegan": vegan,
            "servings": request.form.get("servings"),
            "calories": request.form.get("calories"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "recipe_image": request.form.get("recipe_image"),
            "ingredients": request.form.getlist("ingredients"),
            "recipe_method": request.form.getlist("recipe_method"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories)


# ---------- Edit an existing recipe ----------
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        vegetarian = "on" if request.form.get("vegetarian") else "off"
        vegan = "on" if request.form.get("vegan") else "off"
        edit = {
            "title": request.form.get("title"),
            "description": request.form.get("description"),
            "category_name": request.form.get("category_name"),
            "cuisine": request.form.get("cuisine"),
            "vegetarian": vegetarian,
            "vegan": vegan,
            "servings": request.form.get("servings"),
            "calories": request.form.get("calories"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "recipe_image": request.form.get("recipe_image"),
            "ingredients": request.form.getlist("ingredients"),
            "recipe_method": request.form.getlist("recipe_method"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, edit)
        flash("Recipe Successfully Updated")
        return redirect(url_for("get_recipes"))
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories)


# ---------- Delete an Existing Recipe ----------
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))


# ---------- View individual Recipes ----------
@app.route("/view_recipe/<recipe_id>")
def view_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        "view_recipe.html",
        recipe=recipe)


# ---------- Save a recipe to profile ----------
@app.route("/save/<recipe_id>", methods=["POST"])
def save_recipe(recipe_id):
    username = mongo.db.users.find_one({"username": session["user"]})
    saved = username["saved_recipes"]

    if ObjectId(recipe_id) in saved:
        flash("Recipe Already Saved to Profile")
        return redirect(request.referrer)
    mongo.db.users.update_one(
        username, {"$push": {"saved_recipes": ObjectId(recipe_id)}})
    flash("Recipe Saved to Profile")
    return redirect(request.referrer)


# ---------- Remove a saved recipe from profile ----------
@app.route("/remove/<recipe_id>", methods=["POST"])
def delete_saved_recipe(recipe_id):
    username = mongo.db.users.find_one({"username": session["user"]})
    mongo.db.users.update_one(
        username, {"$pull": {"saved_recipes": ObjectId(recipe_id)}})
    flash("Recipe Removed from Profile")
    return redirect(request.referrer)


@app.route("/profile_image", methods=["POST"])
def profile_image():
    username = mongo.db.users.find_one({"username": session["user"]})
    mongo.db.users.update_one(
        username, {"$set": {
            "profile_image": request.form.get("profile_image")}})
    flash("Profile picture sucessfully updated")
    return redirect(request.referrer)


# ---------- Dashboard Page ----------
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ---------- Error Handing Pages ----------
@app.errorhandler(404)
def resource_not_found(error):
    '''
    thanks to https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/
    '''
    return render_template("404.html")


@app.errorhandler(500)
def internal_server_error(error):
    '''
    thanks to https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/
    '''
    return render_template("500.html")


# The correct running of the app file
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)
