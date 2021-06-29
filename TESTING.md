# Testing

# Contents
1. [Testing User Stories](testing-user-stories)
    - [First Time User](first-time-user)
    - [Returning User](returning-user)
    - [Frequent User](frequent-user)
    - [Admin Goals](admin-goals)
2. [Code Validation](code-validation)
3. [Browser Compatibility](browser-compatibility)
4. [Functionality Testing](funcitonality-testing)
    - [Navigation](navigation)
    - [Home Page](home-page)
    - [Registration & Log In](registration-and-log-in)
    - [Adding A Recipe](adding-a-recipe)
    - [Editing A Recipe](editing-a-recipe)
    - [Deleting A Recipe](deleting-a-recipe)
    - [User Profile](user-profile)
    - [Save Recipe to Profile](save-recipe-to-profile)
    - [Recipes Search & View](recipes-search-and-view)
    - [Recipe Page](recipe-page)
    - [Dashboard](dashboard)
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


# Code Validation 

# Browser Compatibility

# Functionality Testing

Functionality testing has been carried out on all browsers listed in the browser 
compatibility section. 

## Navigation 

|  Test  |  Purpose  |  Expected Result  |  Pass / Fail  |
|:---:|-----------------| ---------------- |:-----:|
| 01 | Home link in navbar | Takes the user to the home page | Pass |
| 02 | Logo in navbar | When clicked takes the user to the home page| Pass |
| 03 | Recipes link in navbar | Takes user to the recipes page | Pass |
| 04 | Log In link in navbar | Takes user to the log in page form | Pass |
| 05 | Register link in navbar | Takes user to the register page form | Pass |
| 06 | Add Recipe link in navbar (when user logged in) | Takes user to the add recipe page form | Pass |
| 07 | Profile link in navbar (when user logged in) | Takes user to their profile page | Pass |
| 08 | Dashboard link in navbar (when user logged in) | Takes user to the dashboard page | Pass |
| 09 | Log out link in navbar (when user logged in) | Opens a modal confirming whether the user wishes to log out - confirming logs user out, and redirects them to the login page  | Pass |
| 10 | GitHub icon in footer | Opens github repository in a new tab | Pass |
| 11 | LinkedIn icon in footer | Opens developers linkedIn pafe in a new tab | Pass |
| 12 | Pinterest icon in footer | Open pinterest in a new tab | Pass |
| 13 | Twitter icon in footer | Opens twitter in a new tab | Pass |

## Home Page

|  Test  |  Purpose  |  Expected Result  |  Pass / Fail  |
|:---:|-----------------| ---------------- |:-----:|
| 01 | Carousel Autoplay | Carousel should display six random recipes uploaded by admin and should automatically move to the next recipe after five seconds | Pass |
| 02 | Carousel Recipe link | View recipe button takes the user to the recipe page of the image shown | Pass |
| 03 | Animations on scroll | When a user scrolls down a page different sections fade in / flip up | Pass |
| 04 | Find out more button | The find out more button opens a link in a seperate tab, offering the user the option to purchase the book feature | Pass |
| 05 | More Breakfast Button | Takes the user to the recipes page and filters the recipes for breakfast recipes | Pass |
| 06 | More Lunch Button | Takes the user to the recipes page and filters the recipes for lunch recipes | Pass |
| 07 | More Dinner Button | Takes the user to the recipes page and filters the recipes for dinner recipes | Pass |
| 08 | Recipe Cards | Clicking the recipe image or the eye icon takes the user to that recipe page | Pass |
| 09 | Recipe Cards (when logged in) | Clicking the plus icon (when not uploaded by the session user) saves the recipe to their profile | Pass |

## Registration and Log In 

|  Test  |  Purpose  |  Expected Result  |  Pass / Fail  |
|:---:|-----------------| ---------------- |:-----:|
| 01 | Log In link | Yellow log in link under the register button redirects the user to the log in page | Pass |
| 02 | First Name validation | First name (a-z, A-Z, between 2-20 characters). Input field tooltipped to provide user feedback. If invalid input turns red and feedback provided | Pass |
| 03 | User Name validation | User name (a-z, A-Z, 0-9 between 5-20 characters). Input field tooltipped to provide user feedback. If invalid input turns red and feedback provided | Pass |
| 04 | Password validation | Password (a-z, A-Z, 0-9 between 5-20 characters). Input field tooltipped to provide user feedback. If invalid input turns red and feedback provided | Pass |
| 05 | Username Duplicates | Flash message indicates to the user than the username already exists, and redirects them to the register page | Pass |
| 06 | Sucessful Registration | Flash message indicates to the user that their registration has been sucessful and redirects them to the user's profile page | Pass |
| 07 | Incorrect Username / Password | Flash message indicates to the user that their username or password is incorrect and redirects them to the log in page | Pass |
| 08 | Sucessful Log In | Flash message welcomes the user and the user is redirected to their profile page | Pass |

## Adding a recipe 

|  Test  |  Purpose  |  Expected Result  |  Pass / Fail  |
|:---:|-----------------| ---------------- |:-----:|
| 01 | Recipe Name Field | Recipe name must be between 5-50 characters. Feedback provided if criteria not met | Pass |
| 02 | Recipe Description Field | Recipe description must be between 10-180 characters. Tooltipped to aid the user | Pass |
| 03 | Meal Type dropdown | User has option to select between 3 meal types. If none are selected an alert will display when the add recipe button is clicked | Pass |
| 04 | Country of Origin Field | Country of origin field between 2-25 characters. Tooltipped to aid the user. 
| 05 | Vegan / Vegetarian Switches | User can choose whether a recipe is vegetarian only or vegetarian & vegan by setting the switches to "yes" | Pass |
| 06 | Servings Field | User can use the arrows to click up and down to select servings or type the number of servings. Only numbers can be accepted between 1-20 | Pass |
| 07 | Calories Field | Calories field will only accept numbers between 1-9999 | Pass |
| 08 | Preparation Time field | Prep time field will only accept numbers between 1-999 | Pass |
| 09 | Cooking time field | Cooking time field will only accept numbers between 1-999 | Pass |
| 10 | Image URL | Image URL must have a minimum length of 5 | Pass |
| 11 | Ingredients Field | Recipe ingredients must be between 2-100 characters. Tooltipped to aid the user of format wanted | Pass |
| 12 | Method Field | Method field must be between 10-500 characters | Pass |
| 13 | Add Ingredient / Step buttons | Add an additional ingredient / method input for separate ingredients / method steps | Pass |
| 14 | Remove Ingredient / step icon | Clicking the red trash icon will remove that ingredient / step | Pass |
| 15 | Add Recipe Button | Provided all fields meet the correct format, when submitted the user will be redirected to the recipes page and a flash message will display informing the user their recipe has been sucessfully added | Pass | 

All input fields, with the exception of the vegetarian / vegan switches, will display 
a red underline if they are invalid. If valid a green underline will be displayed. 

## Edit A Recipe 

|  Test  |  Purpose  |  Expected Result  |  Pass / Fail  |
|:---:|-----------------| ---------------- |:-----:|
| 01 | Edit Recipe Form | Edit recipe form should has the same fields available as the add a recipe form | Pass |
| 02 | Pre-populated fields | Each field should be pre-populated with the information already stored in the database | Pass |
| 03 | Field Editing | Any field that is edited displays with a green underline for valid inputs, and red for invalid inputs | Pass |
| 04 | Dropdown Selection | Ensure that the default option ("Choose Your Meal")is NOT clickable on dropdown field | Pass |
| 05 | Cancel Edit |  Clicking the cancel button redirects the user to the recipes page | Pass |
| 06 | Edit Recipe Button | Clicking the edit recipe button updates the recipe information in the database, and a flash message displays to inform the user that the recipe has been sucessfully updated | Pass |

## Deleting A Recipe 

|  Test  |  Purpose  |  Expected Result  |  Pass / Fail  |
|:---:|-----------------| ---------------- |:-----:|
| 01 | Delete Button | Delete button is only available when the user has uploaded the recipe and to the admin user. Delete button on the recipe page will trigger a modal | Pass |
| 02 | Delete Modal Close button | Clicking outside the modal or the close button will close the modal avoiding unwanted deletions | Pass |
| 03 | Delete Modal Delete button | Clicking the delete modal button will remove the recipe from the database and a flash message displays to inform the user the recipe has been sucessfully deleted | Pass |

## User Profile 
|  Test  |  Purpose  |  Expected Result  |  Pass / Fail  |
|:---:|-----------------| ---------------- |:-----:|
| 01 | Profile Information | First Name (profile), profile image, Recipes created & recipes saved display at the top of the page | Pass |
| 02 | Edit Profile Button | Triggers Edit Profile Modal | Pass |
| 03 | Edit Profile Modal | User can update there image URL by entering the URL into the field provided and clicking update. Clicking close will close the edit profile modal | Pass |
| 04 | Log Out Button | Triggers the log out modal seen in navigaion section | Pass |
| 05 | Delete Profile Button | Triggers the delete profile modal | Pass |
| 06 | Delete Profile Modal | User is asked to confirm whether they wish to delete there profile, and a warning to let the user know any recipes they have uploaded will not be deleted along with their profile is displayed. Clicking delete will remove the user from the database | Pass |
| 07 | Add Recipe Button | When a user has not uploaded any recipes, a button prompting the user to upload their own recipes redirects the user to the add a recipe page | Pass |
| 08 | User's/Saved Recipe Cards (View Recipe) | Clicking the recipe image or eye icon takes the user to that recipe page | Pass |
| 09 | User's Recipe Cards (Edit Recipe) | Clicking the edit icon will redirect the user to the edit recipe page for that recipe | Pass |
| 10 | Saved Recipe Cards | When a user has saved recipes to their profile they will display under the user's recipes. Clicking the minus icon will remove the recipe from their saved recipes and a flash message will display to confirm it has been removed from their profile | Pass |

## Saving a recipe to profile 

|  Test  |  Purpose  |  Expected Result  |  Pass / Fail  |
|:---:|-----------------| ---------------- |:-----:|
| 01 | Plus Icon on Recipes Cards | For recipes which have not been uploaded by the session user a plus icon will appear on all recipe cards. Clicking this will save the recipe to the user's profile and a flash message appears to confirm it has been saved to the user's profile | Pass |
| 02 | Recipes already saved to user profile | For recipes which have already been saved to the users profile, a flash message displays informing the user the recipe is already saved to the users profile, when the plus icon is clicked | Pass |
| 03 | Save Button on recipe page | Saves the recipe to the users profile, provided it is not already saved. Only displays on recipes not uploaded by the user, and when the user is logged in | Pass |

Removing saved recipes from a user's profile already covered in profile functionality. 

## Recipes Search & View

|  Test  |  Purpose  |  Expected Result  |  Pass / Fail  |
|:---:|-----------------| ---------------- |:-----:|
| 01 | Recipe Shuffle | Recipes are shuffled everytime each time the page is re-loaded | Pass |
| 02 | Recipe Filter | The recipe filter buttons will return recipes which match the category selected | Pass |
| 03 | Recipe Search | Returns recipes based on the user text input | Pass |
| 04 | Search Reset | Clears any filters or searches based on user text input and displays all recipes to the user | Pass |
| 05 | Pagination Display | Recipes are limited to 6 recipes per page when viewing all recipes or using the filter buttons. This has not been implemented with search functionality, as the number of recipes returned with specific queries will likely be quite low to begin with. As more recipes are added this may need to be implemented | Pass |
| 06 | Pagination Links | Next and previous arrows take the user to the next/previous page. Clicking the page numbers takes the user to the correct corresponding page | Pass |

## Recipe Page 

|  Test  |  Purpose  |  Expected Result  |  Pass / Fail  |
|:---:|-----------------| ---------------- |:-----:|
| 01 | Recipe information (Not logged in / registered) | Basic recipe information displays to the user (Recipe image, servings, prep-time, cook-time & calories) | Pass |
| 02 | Register / Log In Links (Not logged in / registered) | Register account and log in links redirect the user to the respective pages | Pass |
| 03 | Recipe information (Logged in) | Remaining recipe information is displayed to the user (ingredients, method, description, created by) | Pass |
| 04 | Recipes button | Displays to all users which redirects the user back to all recipes | Pass |
| 05 | Save Button | See saving a recipe to profile | Pass |
| 06 | Edit Button | Edit button will only be displayed to users who have uploaded the recipe and to the admin user, and will redirect the user to the edit recipe page | Pass |
| 07 | Delete Button | Edit button will only be displayed to users who have uploaded the recipe and to the admin user, and open the delete recipe modal | Pass |

## Dashboard 

|  Test  |  Purpose  |  Expected Result  |  Pass / Fail  |
|:---:|-----------------| ---------------- |:-----:|
| 01 | Charts & Maps | Various recipe / user information renders correctly from MongoDB Charts | Pass |


# Responsive Design 

Responsinator and Google Developer tools have been used to test the responsiveness. This tools have 
been utilised throughout the development of the project.

Responsinator examples only shown for pages, which do not require user log in. 

Responsinator provides landscape and portrait views for: 
- iPhone X
- Android (Pixel 2)
- iPhone 6-8
- iPad

I have added views from Google Dev Tools for: 
- Galaxy Fold 
- Iphone 4
- iPhone X - (When user logged in)
- Android (Pixel 2) - (When user logged in)
- iPhone 6-8 - (When user logged in)
- iPad - (When user logged in)

I have added Galaxy Fold & iPhone 4 as they are the smallest devices in height and width 
available, and are common enough devices to merit review. 


1. [Home Page: Responsinator](https://www.responsinator.com/?url=https%3A%2F%2Ffastara.herokuapp.com%2F)
    - [Home Page: Google Dev](documentation/testing/responsiveness/home.png)
2. [Recipes Page: Responsinator](https://www.responsinator.com/?url=https%3A%2F%2Ffastara.herokuapp.com%2Fget_recipes)
    - [Recipes Page: Google Dev](documentation/testing/responsiveness/recipes.png)
3. [Log In Page: Responsinator](http://www.responsinator.com/?url=fastara.herokuapp.com%2Flogin)
    - [Log In Page: Google Dev](documentation/testing/responsiveness/login.png)
4. [Register Page: Responsinator](http://www.responsinator.com/?url=http%3A%2F%2Ffastara.herokuapp.com%2Fregister)
    - Register page has the same styling as the log in page for Galaxy Fold & iphone4 views. 
5. [Profile Page: Google Dev](documentation/testing/responsiveness/profile.png)
6. [View Recipe Page: Google Dev](documentation/testing/responsiveness/view-recipe.png)
7. [Add / Edit Recipe Page: Google Dev](documentation/testing/responsiveness/add-recipe.png)
    - Add and edit recipe pages are nearly identical. The only differences between the two 
    are that the recipes fields will be auto-populated on the edit-recipe page, and there 
    is a cancel, and edit recipe buttons at the bottom of the page. 
8. [Dashboard Page: Google Dev](documentation/testing/responsiveness/dashboard.png)