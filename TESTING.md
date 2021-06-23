# Testing

# Contents
1. [Testing User Stories](testing-user-stories)
    - [First Time User](first-time-user)
    - [Returning User](returning-user)
    - [Frequent User](frequent-user)
    - [Admin Goals](admin-goals)
2. [Code Validation](code-validation)
3. [Functionality Testing](funcitonality-testing)
    - [Navigation](navigation)
    - [Registration & Log In](registration-and-log-in)
    - [Adding A Recipe](adding-a-recipe)
    - [Editing A Recipe](editing-a-recipe)
    - [Deleting A Recipe](deleting-a-recipe)
    - [User Profile](user-profile)
    - [Save Recipe to Profile](save-recipe-to-profile)
    - [Remove Recipe from Profile](remove-recipe-from-profile)
    - [Edit Profile Image](edit-profile-image)
    - [Recipes Search](recipes-search)
    - [Recipes Filter](recipes-filter)
    - [Log Out](log-out)
4. [Browser Compatibility](browser-compatibility)
5. [Responsive Design](responsive-design)
6. [Security Testing](security-testing)
7. [Solved Bugs](solved-bugs)
8. [Known Issues](known-issues)
9. [Lighthouse](lighthouse)

# Testing User Stories

## First Time User

1. As a first time visitor, I want to understand the purpose of the site at first 
glance, to establish whether I want to explore the site further.
    - The user is greeted with a carousel of image showing recipes with a view recipe 
    button clearly indicating this is some form of recipe website. 
    - Below the carousel is a brief introduction explaining what Fastara is and offers. I 
    have kept this introduction relatively short so the user does not lose interest. 


2. As a first time visitor, I want to be able to see recipes, to establish whether
I wish to register, to see full recipes. 
    - On the home page the user can see a carousel of recipes which autoplay, and further down 
    the page can see recipes from the different categories (breakfast, lunch and dinner). 
    - Before a user is registered / logged in, they can view all recipes on the recipes page. 
    - Before a user is registered / logged in, they can view individual recipes, which shows 
    some limited recipe information and an image of the recipe. 


3. As a first time visitor, I want to be able to click through different meal types
at the touch of a button.
    - On the home page, the user can view a few recipes from each category, and click 
    the link to take the user to view more recipes of the same category. 
    - On the recipes page, the user can click one of the category filter buttons to show them 
    all the recipes in that category. 


4. As a first time visitor, I want to be able to register an account easily, without
providing much personal information.
    - User's can register via the register link in the navbar, where they are taken to a 
    register form, and asked for firstname, username, and password. 


## Returning User 

1. As a returning visitor, I want to be able to login into my account, without re-registering.
    - A separate Log In link in the navbar allows the user to login into their account with their 
    username and password. 
    - If a user clicks on the register link they can see a message below the register button - 
    "Already Registered? Log In", with a link to take the user to the log in page. 


2. As a returning visitor, I want to be able to logout out of my account. 
    - When a user is logged in, a log out link in the navbar will open a modal confirming 
    whether the user wishes to log out of their account. 
    - A user can also log out from their profile, which will open the same modal confirming 
    whther the user wishes to log out of their account. 


3. As a returning visitor, I want to be able to view my profile. 
    - When a user logs in they are automatically redirected to their profile page, and 
    a welcome flash message greets the user.  
    - A profile link in the navbar allows the user to return to their profile from any page, once
    they are logged in. 


4. As a returning visitor, I want to be able to delete my account should I wish. 
    - From a user's prfofile page, the user can click the delete button, which will open a 
    modal confirming whether the user wishes to delete their account or not. A message is left 
    to confirm that any recipes the user has uploaded will not be removed from the site. 


5. As a returning visitor, I want to be able to save other user's recipes to my profile, 
for easy viewing on future visits to the site. 
    - Any recipe that is not uploaded by the current session user, will display a plus icon on 
    the recipe card, which allows the user to save the recipe to their profile. This will then 
    display on the user's profile, under any recipes that have been uploaded by the session user. 
    - When a user views an individual recipe that has not been uploaded by the session user, 
    a save recipe button will show at the bottom of the recipe allowing the user to save the recipe 
    to their profile. 


6. As a returning visitor, I want to be able to remove saved recipe's from my profile should
I no longer require them. 
    - When a user views the recipe cards in the saved recipes section on their profile, a 
    minus icon shows, which is tooltipped informing the user that this will remove the recipe 
    from their profile. A flash message displays indicating the recipe has been removed from their 
    profile. 

7. As a returning visitor, I want to to be able to access recipe information such as the ingedients 
and method.
    - Once a user has registered and logged in, when viewing individual recipes, rather than 
    a message asking whether they wish to log in or register to view the full recipe, the ingredients 
    and method are shown in two clear setions to the user, so they have all the information they need 
    to make the recipe. 


## Frequent User

1. As a frequent visitor, I want to be able to upload recipes to the website, and have access to 
any recipes I have uploaded on my profile. 
    - When a user is yet to upload any of their own recipes, a button on their profile will show 
    encouraging the user to upload their own recipes. 
    - A user can upload their own recipes using the add recipe link in the navbar, which will take 
    the user to a straightforward pre-defined form to fill in. 


2. As a frequent visitor, I want to be able to edit and recipe I have created. 
    - When viewing uploaded recipes on a user's profile then an edit icon will show on the recipe card, 
    which takes the user to the edit recipe form. This is pre-populated with all the recipe data, and is the same 
    format as the add recipe form. 
    - When viewing individual recipes, if the recipe has been uploaded by the user, then an edit 
    recipe button will show at the bottom of the page, which will take the user to the same 
    edit recipe form. 


3. As a frequent visitor, I want to be able to delete any recipe I have created.
    - When a user views a recipe that they have created a delete button will show at the bottom 
    of the recipe. This will trigger a modal to confirm whether they wish to delete the recipe or not. 
    - Note: A delete icon could have been added to the recipe card, but I decided against this, as I 
    feel this would have made the recipe cards to cluttered. 


4. As a frequent visitor, I want to be able to search recipes containing certain 
ingredients, or by a recipe name. 
    - On the recipes page there is a search function available to the user. Recipes will return 
    providing what the user searches for matches words in the Recipe Title, Description, or Ingredients. 


5. As a frequent visitor, I would like some information, showing which recipes contain 
the least calories and which recipes take the least amount of time. 
    - When a user is logged in a dashboard link is available in the navbar. The charts here 
    show the user which recipes have the lowest caloies, and which recipes are the quickest to 
    prepare and cook. 


## Admin Goals

1. As an admin user, I need to ensure some access control, to allow me to edit and delete recipes 
that are not deemed suitable for the website. 
    - When the user's username is "admin", then at the bottom of every recipe, the edit 
    and delete buttons will show. This is achieved using Jinja templating, and as there 
    can only be one "admin" username, this means only the admin user has access to this. 