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


def get_recipes_paginate(offset=0, per_page=6):
    recipes = list(mongo.db.recipes.find())
    return recipes[offset: offset + per_page]


def filter_recipes_paginate(category, offset=0, per_page=6):
    if category == "Breakfast":
        recipes = list(mongo.db.recipes.find({"category_name": "Breakfast"}))
    elif category == "Lunch":
        recipes = list(mongo.db.recipes.find({"category_name": "Lunch"}))
    else:
        recipes = list(mongo.db.recipes.find({"category_name": "Dinner"}))
    return recipes[offset: offset + per_page]


@app.route("/")
def home():
    """
    Renders the home page and lists recipes for
    admin, breakfast, lunch & dinner
    """
    # lists recipes created by admin and shuffles
    admin_recipes = list(
        mongo.db.recipes.find({"created_by": "admin"}))
    random.shuffle(admin_recipes)

    # lists recipes in breakfast category and shuffles
    breakfast_recipes = list(
        mongo.db.recipes.find({"category_name": "Breakfast"}))
    random.shuffle(breakfast_recipes)

    #lists recipes in lunch category and shuffles
    lunch_recipes = list(
        mongo.db.recipes.find({"category_name": "Lunch"}))
    random.shuffle(lunch_recipes)

    #lists recipes in dinner category and shuffles
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


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Registers a new user and adds them to the
    database if the username is valid and NOT
    a duplicate
    """
    if request.method == "POST":

        # check if the username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # if username already exists: flash message
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # update mongoDB users collection
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


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Logs the user in if the username and password
    match what is held in the database
    """

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


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Renders the user profile template and displays
    user information, recipes created by the user
    and users saved recipes
    """

    # stores the user's username in variable
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    # stores the user's profile image in variable
    profile_image = mongo.db.users.find_one(
        {"username": session["user"]})["profile_image"]

    # stores the user's profile image in variable
    firstname = mongo.db.users.find_one(
        {"username": session["user"]})["firstname"]

    # stores the recipes crated by the user in variable
    recipes = list(mongo.db.recipes.find({"created_by": session['user']}))

    # stores the recipes saved by the user in variable
    saved = mongo.db.users.find_one(
        {"username": session["user"]})["saved_recipes"]

    # creates an empty array
    saved_recipe = []

    # Each of the users saved recipes is appended to the empty array
    for recipe_id in saved:
        recipe_id = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        saved_recipe.append(recipe_id)

    # Profile template rendered when there's a session user
    if session["user"]:
        return render_template(
            "profile.html",
            username=username,
            profile_image=profile_image,
            firstname=firstname,
            recipes=recipes,
            saved_recipe=saved_recipe)

    # if no user in session redirects to login page
    return redirect(url_for("login"))


@app.route("/remove_profile")
def remove_profile():
    """
    Deletes the user's account from the database
    """

    # removes the session user from the database
    mongo.db.users.remove({"username": session["user"]})

    # removes the user from the session
    session.pop("user")
    flash("Your profile has been succesfully deleted")
    return redirect(url_for("register"))


@app.route("/logout")
def logout():
    """
    Removes the user from the session and redirects
    the user to the login page
    """
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/get_recipes")
def get_recipes():
    """
    Returns a list of all the recipes in the database,
    returns the recipes.html & pagination is applied
    """

    # lists all recipes in the database
    recipes = list(mongo.db.recipes.find())

    # pagination adapted from mozillazg (credited in README)
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


@app.route("/get_recipes/<category>")
def categories(category):
    """
    Filters the recipes by breakfast, lunch & dinner
    and renders them to the recipes.html template
    """

    # returns a list of all recipes in breakfast category
    if category == "Breakfast":
        recipes = list(mongo.db.recipes.find({"category_name": "Breakfast"}))

    # returns a list of all recipes in lunch category
    elif category == "Lunch":
        recipes = list(mongo.db.recipes.find({"category_name": "Lunch"}))

    # returns a list of all recipes in dinner category
    else:
        recipes = list(mongo.db.recipes.find({"category_name": "Dinner"}))

    # pagination adapted from mozillazg (credited in README)
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


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Searches the recipes collection and returns results
    matching Recipe name, description and ingredients
    """

    # stores user input in variable
    query = request.form.get("query")

    # list all recipes matching user query
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template(
        "search.html",
        recipes=recipes)


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    """
    Adds a new recipe to the database if all the fields
    are valid
    """

    if request.method == "POST":
        # Updates the database with all the recipes fields
        # from user input
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
        # Inserts a new recipe to the database
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))

    # sorts all categories and sorts alphabetically
    categories = mongo.db.categories.find().sort("category_name", 1)

    # if there is a session user add_recipe template renders
    if session["user"]:
        return render_template("add_recipe.html", categories=categories)
    # if no session user redirects to login page
    else:
        return redirect(url_for("login"))


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """
    Edits and updates an existing recipe in the database
    """

    if request.method == "POST":
        # Updates the database with all the recipes fields
        # from user input
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

        # updates an existing recipe in the database
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, edit)
        flash("Recipe Successfully Updated")
        return redirect(url_for("get_recipes"))

    # finds the recipe by id
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    # sorts all categories and sorts alphabetically
    categories = mongo.db.categories.find().sort("category_name", 1)

    # if there is a session user add_recipe template renders
    if session["user"]:
        return render_template(
            "edit_recipe.html", recipe=recipe, categories=categories)
    # if no session user redirects to login page
    else:
        return redirect(url_for("login"))


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """
    Deletes a recipe from the database. Loops through
    all the users saved recipes, and removes the deleted
    recipe from each of the users saved_recipes arrays.
    """

    # stores the recipe id in recipe variable
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    # Lists all the users with the recipe_id
    saved_recipes = list(mongo.db.users.find(
        {"saved_recipes": ObjectId(recipe_id)}))

    # loops through all users saved recipes
    for recipes in saved_recipes:
        # Removes the deleted recipe from all users saved recipes array
        mongo.db.users.update_many(
            recipes, {"$pull": {recipe}})

    # Deletes recipe from the database
    mongo.db.recipes.remove(recipe)
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))


@app.route("/view_recipe/<recipe_id>")
def view_recipe(recipe_id):
    """
    Returns the recipe page for a specific recipe id
    """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        "view_recipe.html",
        recipe=recipe)


@app.route("/save/<recipe_id>", methods=["POST"])
def save_recipe(recipe_id):
    """
    Saves a recipe to the user saved_recipes array
    which can then be viewed on the users profile
    """
    username = mongo.db.users.find_one({"username": session["user"]})
    saved = username["saved_recipes"]

    # checks if the recipe is already in the users
    # saved_recipes array
    if ObjectId(recipe_id) in saved:
        flash("Recipe Already Saved to Profile")
        return redirect(request.referrer)

    # adds the recipe to the users saved_recipes array
    mongo.db.users.update_one(
        username, {"$push": {"saved_recipes": ObjectId(recipe_id)}})
    flash("Recipe Saved to Profile")
    return redirect(request.referrer)


@app.route("/remove/<recipe_id>", methods=["POST"])
def delete_saved_recipe(recipe_id):
    """
    Removes a saved recipe from the users saved_recipes array
    """

    # sets the session user to username variable
    username = mongo.db.users.find_one({"username": session["user"]})

    # removes recipes from users saved_recipes array
    mongo.db.users.update_one(
        username, {"$pull": {"saved_recipes": ObjectId(recipe_id)}})
    flash("Recipe Removed from Profile")
    return redirect(request.referrer)


@app.route("/profile_image", methods=["POST"])
def profile_image():
    """
    Allows the user to update there profile picture.
    """

    # sets the session user to username variable
    username = mongo.db.users.find_one({"username": session["user"]})

    # updates the session users profile_image
    mongo.db.users.update_one(
        username, {"$set": {
            "profile_image": request.form.get("profile_image")}})
    flash("Profile picture sucessfully updated")
    return redirect(request.referrer)


@app.route("/dashboard")
def dashboard():
    """
    Renders the dashboard is there is a session user
    """
    if session["user"]:
        return render_template("dashboard.html")
    else:
        return redirect(url_for("login"))



@app.errorhandler(404)
def resource_not_found(e):
    '''
    404 error handling page
    thanks to https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/
    '''
    return (render_template("404.html"), 404)


@app.errorhandler(500)
def internal_server_error(e):
    '''
    500 error handling page
    thanks to https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/
    '''
    return render_template("500.html"), 500


# The correct running of the app file
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=False)
