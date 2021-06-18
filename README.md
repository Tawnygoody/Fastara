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
    - Below the title of the recipe is a card with an image of the recipe with some information 
    relating to the recipe (calories, cook time, prep time, servings and whether it is vegetarian/
    vegan). Image of the recipe is crucial - saying goes "people eat with their eyes" - this is definately
    relevant when coming to recipe websites. The images are styled so they do not stretch, and should 
    look appealing on all device sizes. 
    - Below the recipe card is section to encourage the user to register / log in. If the ingredients / methods
    fields were shown to an un-registered user, there may be no incentive for a user to register. Un-regisered users
    have the basic information they need to determine whether recipes appeal to them. 
    - At the bottom of the page is a button to take the user back to the recipes page. 
- View Recipe Page (When user is logged in)
    - Title and image card remain the same when the user is logged in. 
    - Below the recipe card, shows who created the recipe and shows the recipe description
    in italics, with a yellow background. This is to further engage the user. 
    - The ingredients and method columns are split unevenly, with the method column being wider 
    on larger devices, as this tends to have more content than the ingredients column. The dark 
    background of the ingredients column provides a nice contrast and clearly separates the 
    ingredients from the method. 
    - At the bottom of the page is a variety of buttons. Which buttons are shown varies according 
    to the user and which user uploaded the recipe:
        - A user who uploaded the recipe, will be shown a recipes button to take the user back to 
        the recipes page, an edit button to enable the user to edit the recipe and a delete button 
        to allow the user to delete the recipe if they wish. The delete button triggers a modal to
        confirm the user wishes to delete the recipe, to reduce the chance of unwanted deletions. 
        - A user who did not upload the recipe will be shown the recipes button to take the user back 
        to the recipes page and a save button to save the recipe to their profile. 
        - The admin user will be shown, the recipe button, edit button, and delete button, as this user 
        has authority to edit and delete any recipe. The save button will only show on recipes not 
        uploaded by admin. 
- Profile Page
    - The profile page will only be displayed to users that are logged in. 
    - The card at the top of the page is similar in appearance to the card on the view recipes page, with the 
    main difference in appearance that the profile image is a smaller on larger devices. Profile information 
    such as username, recipes created and recipes saved can be viewed here. Below this the user can choose to
    edit their profile image, log out, and delete their profile. The log out button and delete profile 
    buttons will trigger modals, to reduce the chance of unwanted deletion / logging out. 
    - When a user has not uploaded any recipes an upload recipe button will be shown to encourage the user
    to upload their own recipes. 
    - When a user has uploaded there own recipes, the upload recipe button will be removed, and the recipe card
    will be displayed here. These will appear as they do on the recipes page. Again the plus icon will not show 
    as the recipe has been uploaded by the user and already appears on the users profile, therefore there is no 
    requirement to save the recipe to their profile. 
    - If a user has saved no recipes to there profile then no section will display below the created recipes section. 
    Once a user has saved a recipe, the saved recipes title will show, with the recipe cards shown in this section. 
    Next to the eye icon to view the recipe, a tooltipped minus icon will display should the user wish to remove the 
    recipe from the saved recipes section. 
- Dashboard 
    - By utilising MongoDB Charts this provides a visualization of the data stored in MongoDB. This can provide, useful
    information to the user and actionable insight. 
    - Whilst I could choose to do a whole variety of charts, this could be deemed tedious to a user. I have therefore chosen 
    4 charts which provides the most relevant information to the user: 
        - A heat map showing where the recipes come from around the globe. 
        - A chart showing which user has uploaded the most recipes. 
        - A chart showing which recipes take the least amount of time to prep and cook. 
        - A chart showing which recipes have the lowest amount of calories. 
    - The first 2 charts are just for the general interest of the user. The second 2 charts 
    provide the user with actionable insight. Most people after a full days work want dinner to 
    be full of flavour and take the least amount of time. The chart showing recipes with the least 
    calories is especially helpful to users who are on an intermittent fasting diet plan, as they have 
    a restrictive amount of calories they can consume on fast days. 
    - Charts are set to refresh every 30mins. 
- Add Recipe Page
    - The same background image as the log in page and register page has been used. 
    - There are various fields for the use to fill in. Relevant fields have been tooltipped 
    to provide users with the requirements they need in order to create the recipe. A dropdown 
    field has been used to select the recipe category, and switches have been used to indicate 
    whether a recipe is vegan or vegetarian. 
    - Ingredients and method fields have an add ingredient/method button, allowing the user to 
    seperate each ingredient / method. When each new step is added, a red bin appears allowing the user 
    to delete an ingredient / method. 
    - The add recipe button at the bottom will add the recipe to the database and display the recipe 
    card on recipes and the users profile. Only when the required fields have been completed, and meet the 
    stated criteria will this be achievable. 
- Edit Recipe Page 
    - The edit recipe page can be accessed from the "View Recipe" page, which are available on the recipes 
    page and the users profile page. 
    - The edit recipe is much the same as the add recipe page, however the page is pre-populated 
    with the recipe data. 
    - At the bottom of the page there is cancel button which will cancel any changes made and take the user 
    back to the recipes page and an edit button which update the changes in the database and take the user 
    back to the recipes page. 

### Future Features

- An option for a user to build a meal plan for a day. For those who are on the 5:2 diet plan, 
as they have a limited number of calories for the day, it would be useful to the user, to be able 
to build a meal plan, that keeps all the 3 meal types (Breakfast, Lunch & Dinner) under their 
daily allowance. 


## Skeleton 

Below you can find links for my wireframes, showing how I would like the pages to be strcutured, 
and how the site would appear on different device sizes. 

### Wireframes 

The wireframes have been created using Balsamiq, and show for desktop, iPad and iPhone. 

- Home Page
    - [Desktop](documentation/wireframes/home-desktop.png)
    - [iPad](documentation/wireframes/home-ipad.png)
    - [iPhone](documentation/wireframes/home-iphone.png)
- Recipes Page
    - [Desktop](documentation/wireframes/recipes-desktop.png)
    - [iPad](documentation/wireframes/recipes-ipad.png)
    - [iPhone](documentation/wireframes/recipes-iphone.png)
- Log In Page
    - [Desktop](documentation/wireframes/login-desktop.png)
    - [iPad](documentation/wireframes/login-ipad.png)
    - [iPhone](documentation/wireframes/login-iphone.png)
- Register Page
    - [Desktop](documentation/wireframes/register-desktop.png)
    - [iPad](documentation/wireframes/register-ipad.png)
    - [iPhone](documentation/wireframes/register-iphone.png)
- Profile Page 
    - [Desktop](documentation/wireframes/profile-desktop.png)
    - [iPad](documentation/wireframes/profile-ipad.png)
    - [iPhone](documentation/wireframes/profile-iphone.png)
- Add / Edit Recipe 
    - [Desktop](documentation/wireframes/add-desktop.png)
    - [iPad](documentation/wireframes/add-ipad.png)
    - [iPhone](documentation/wireframes/add-iphone.png)
- View Recipe Page 
    - [Desktop]()
    - [iPad]()
    - [iPhone]()
- Dashboard Page 
    - [Desktop]()
    - [iPad]()
    - [iPhone]()

## Surface 

### Design 

- Colour Scheme
    - I have taken inspiration from [Canva's](https://www.canva.com/learn/website-color-schemes/)
    professional and modern colour scheme and [Assiko's Fireworks](https://www.awwwards.com/sites/assiko), described
    by [Visme](https://visme.co/blog/website-color-schemes/) as Innovative and audacious, seen below. Both 
    color schemes have dark greys, yellows, and lighter grays which were the main colorsI have chosen to include 
    in my site. 

    #### Assiko Colour Scheme

    ![Assiko Color Scheme](documentation/color-schemes/color-scheme-idea1.png)

    #### Canva Professional & Modern Colour scheme

    ![Canva Colour Scheme](documentation/color-schemes/color-scheme-idea2.png)

    #### Chosen Colour scheme

    ![Chosen Colour Scheme](documentation/color-schemes/color-scheme.png)

    - Very dark Grey (#101010) has been used for the navbar and the footer, and dark text. 
    - Bright Yellow (#ffe400) has been used for headings underlines, in the logo, and to provide 
    text contrast against dark buttons / links. 
    - Ligher yellow (#ffee58), has been used to highlight nav links, and on buttons to take the user 
    to different pages on the site. 
    - Very light grey (#eae7dc) has been used for the nav links, so they do not detract from the Logo 
    text, as this is White, and light text on dark backgrounds.
    - Off white (#f1f1f1) has been used for overlay text to provide more contrast with the images behind 
    than the very light grey would offer. 

- Additional colors have been used to signify, saving recipes, editing recipes, and any deletion's/
Log out. 
