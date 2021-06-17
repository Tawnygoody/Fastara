<h1 align="center">Fastara</h1>

View the repository in GitHub [here](https://github.com/Tawnygoody/Fastara)

View the live project [here](https://fastara.herokuapp.com/)

# Contents

1. [User Experience (UX)](#user-experience-(ux))
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
    - [Surface](#surface)
2. [Database Schema](#database-schema)
3. [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks, Libraries & Programmes used](#frameworks-libraries-and-programmes-used)
4. [Testing](#testing)
5. [Database Creation](#database-creation)
6. [Deployment](#deployment)
    - [Forking the GitHub Repository](#forking-the-github-repository)
    - [Making a Local Clone](#making-a-local-clone)
    - [Heroku app](#heroku-app)
7. [Credits](#credits)
    - [Code](#code)
    - [Media](#media)
8. [Acknowledgments](#acknowledgments)

# User Experience (UX)

## Strategy

Healthy Doesn't Mean Boring!!

Fastara is a recipe website aimed at user's looking for low calorie recipes or who are on
or looking to explore an intermittent fasting diet such as "5:2" diet. Visitors are 
encouraged to upload and share their own creations with the community. 

### User Stories

- First Time Visitor Goals
    1. As a first time visitor, I want to understand the purpose of the site at first 
    glance, to establish whether I want to explore the site further. 
    2. As a first time visitor, I want to be able to see recipes, to establish whether
    I wish to register, to see full recipes. 
    3. As a first time visitor, I want to be able to click through different meal types
    at the touch of a button.
    4. As a returning visitor, I want to be able to register an account easily, without
    providing much personal information. 

- Returning Visitor Goals
    1. As a returning visitor, I want to be able to login into my account, without re-registering.
    2. As a returning visitor, I want to be able to logout out of my account. 
    3. As a returning visitor, I want to be able to view my profile. 
    4. As a returning visitor, I want to be able to delete my account should I wish. 
    5. As a returning visitor, I want to be able to save other user's recipes to my profile, 
    for easy viewing on future visits to the site. 
    6. As a returning visitor, I want to be able to remove saved recipe's from my profile should
    I no longer require them. 
    7. As a returning visitor, I want to to be able to access recipe information such as 
    calories, prep time and cook time to see whether the recipe is suitable for my needs.

- Frequent User Goals
    1. As a frequent visitor, I want to be able to upload recipes to the website, and have access to 
    any recipes I have uploaded on my profile. 
    2. As a frequent visitor, I want to be able to edit and recipe I have created. 
    3. As a frequent visitor, I want to be able to delete any recipe I have created. 
    4. As a frequent visitor, I want to be able to search recipes containing certain 
    ingredients, or by a recipe name. 
    5. As a frequent visitor, I would like some information, showing which recipes contain 
    the least calories and which recipes take the least amount of time. 

- Admin Goals
    1. As an admin user, I need to ensure some access control, to allow me to edit and delete recipes 
    that are not deemed suitable for the website. 

## Scope

Fastara is centered around CRUD (Create, Read, Update Delete) functionality and interacts 
with a MongoDB Atlas cloud database managements system. This is the key feature to allow the 
app to function. 
- Create - Recipes can be saved to the database, using a form on the site. 
- Read - View all of the recipes saved in the database:
    - Recipes can be filtered by meal type. 
    - Search bar functionality allows the user to search for recipes using keywords. 
- Update - Users can edit their own recipes, which changes the stored content within the 
database (provided they are allowed to do so).
- Delete - Users can delete any recipes they have uploaded, or can delete their profile 
should they wish. 

To prevent unwanted editing or deletions, the website has been designed in a way that these 
functions are only available to the uploader of the specific recipe or to the admin user. 
Full CRUD functionality is only authorised to registered users. 

For any site user: 
- Home Page, with attractive imagery, and some information about the site. 
- Recipes Page, showing all the recipes that have been uploaded to the site. 
- Recipe Page, showing limited information about an individual recipe. 
- Login Page
- Register Page
- Information to contact company. 

For registered users:
- Log Out functionality. 
- Clear profile page displaying any recipes the user has uploaded or saved, and 
some basic user information. 
- Recipe Page, shows all information about an individual recipe. 
- Add a recipe page, allowing users to upload there own recipes. 
- Dashboard page, allowing users to allow users to compare recipes. 

For site admin: 
- CRUD functionality for all recipes, regardless of who uploaded them. 

## Structure


