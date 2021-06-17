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

### Existing Features

- Base Page:
    - Navbar (Desktop) - The navbar has a centralised Fastara Logo. Links to the 
    pages are then aligned either side of the logo. I feel this gives the site a 
    contemporary feel, and works well having even number of links either side when 
    a user is either logged in or logged out. The dark background contrasts well with 
    the logo color. Links have been given an off-white color, as to not detract from
    the logo.
    - Navbar (Mobile) - A simple collapsible side nav replaces the links either side 
    of the logo when viewing the site on smaller screen sizes. This is triggered by the 
    hamburger icon, and has the the same dark background as the navbar. An additional logo
    can be seen at the top of the collapsible navbar. 
    - Flash Messages - Imported from Flask, the "flash" feature provides helpful user feedback
    after interaction with the site. 
    - Footer - Footer contains social media links and a github link which open in seperate
    tabs allowing the user to remain on Fastara. Email information for the company is also available
    should a user have any query. 

- Home Page: 
    - A carousel image display with autoplay featuring recipes which have been uploaded by admin. 
    Images are randomised and will show 6 recipes all of which have buttons to take them to that 
    recipe page. 
    - A section briefly explaining what Fastara offers, what intermittent fasting
    involves and its relevance to the site. These fade in on scrolling providing a nice
    user interaction to keep the user's attention. 
    - A book promotion section providing a deeper insight into intermittent fasting, which opens
    in a separate link. 
    - A category section displaying a few recipes for each of the different meal types, with links 
    to take the user to view more of the same category. These recipes are randonmised so the 
    same recipes do not appear on the home page every time it is refreshed/visited. The recipe cards 
    scale in on scroll, which is particularly satisfying on smaller devices. 
- Log In Page
    - A striking yet simple background image can be seen to keep the user interested. 
    - A simple dark background form, which is partially opaque, allows the background
    image to be seen whilst the content is still clearly visible. 
    - Fontawesome icons have been used to provide futher user engagement, with a large 
    login button. 
    - If a user does not already have an account, a link below the login button will take
    them to the register page. 
- Register Page
    - This has mostly the same features as the login page with some minor differences:
        - First name field rather than email or fullname, gives a informal tone, 
        - If a user already has an account, a link below the register button will take them 
        to the login page. 
- Recipes Page
    - At the top of the page there is a search bar, allowing the user to search for recipes using 
    keywords of their choice. This will filter results from the Recipe Title, Description & ingredients,
    and display only recipes matching that criteria. If no results are returned then a message stating
    No results found displays. The reset button allows the user to display a list of all the recipes. 
    - Filter buttons below the search bar allows the user to filter the recipes they see 
    by meal type. 
    - Recipe cards display an image of the recipe, which when hovered over, or clicked on smaller devices, 
    scale in and show an overlay with the name of the recipe. This is a subtle interaction to entice the user. 
    A calorie count a brief description is also provided on the cards. The orange eye allows the user to view
    the entire recipe. This has been tooltipped to provide helpful guidance to the user. 
    - When a user is logged in a tooltipped plus icon will be visible on the cards, which allows the user 
    to save the recipe to their profile. This icon does not appear when the recipe was uploaded by the session
    user as this will already appear on their profile under uploaded recipes. 
    - The recipe cards have been paginated so that only 6 results display per page, so a user does not need to 
    do large amounts of scrolling to get to the bottom / top of the page. 
- View Recipe Page (When not logged in / registered)
    - 

