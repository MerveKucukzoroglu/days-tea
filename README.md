# About
Harmonic Poems is a platform for poets to share their poems and inspire young poets. This platforms aims to be a Harmonic Poets Community, where poets can like, comment and share their poems with the world. 

*Poem is all about rhythm, harmony and soul. Find yourself in one of them or share one of yours with us!*

The Live Site can be found [here](https://harmonic-poems.herokuapp.com/).

# Table of Contents
* [User Experience](#user-experience)
    * [Admin](#admin)
    * [Member User](#member-user)
    * [General User](#general-user)
* [Features](#features)
    * [Existing Features](#existing-features)
* [Future Features](#future-features)
* [Wireframes](#wireframes)
* [Structure](#structure)
* [Databases](#databases)
    * [Post Model](#post-model)
    * [Comment Model](#comment-model)
* [Technologies Used](#technologies-used)
* [Frameworks, Libraries & Tools Used](#frameworks-libraries--tools-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

# User Experience
I designed this platform with desgin thinking approach. With only the necessary content/information. User can surf the site easily and get the information they are looking for.
Please find all my defined user stories [here](https://github.com/MerveKucukzoroglu/harmonic-poems/labels/USER-STORIES)
## Admin
* As a Site Admin I can approve or disapprove posts so that I can filter out objectionable posts.
* As a Site Admin I can create, read, update and delete posts so that I can manage my blog content.
* As a Site Admin I can aproove Posts before it is published so that the site content will be consistent.

## Member User
* As a Member User I can register an account so that I can manage my posts, comment and like.
* As a Member User I can post/add/edit/delete poems so that I can share and manage my poems.
* As a Member User I can like or unlike a post so that I can interact with the content.
* As a Member User I can leave comments on a post so that I can be involved in the conversation.
* As a Member User I can view my posts status of approval so that I can manage my poems.

## General User
* As a Site User I can view a list of posts so that I can select one to read.
* As a Site User I can click on a post so that I can read the full text.
* As a Site User / Admin user I can view comments on an individual post so that I can read the conversation.
* As a Site User / Admin I can view the number of likes on each post so that I can see which is the most popular or viral.


# Features
## Existing Features
* **Home Page**
    * The home page is minimal content to not bother user with loads of information. The page has a Navigation bar and two buttons on the page. If the user is not registered user and not logged in. The navbar has a login/register options and the button to take user ot login page.
        
        ![Home Page](/static/assets/images/home-page.png)

    * If the user is logged in member, the navigation bar will have an accunts icon and instead of login, one of the buttons takes the user to their account profile.
        
        ![Home Page](/static/assets/images/member-home-page.png)
    
    * The Poem button takes any site user to the list of poems page for any user to access and read.

* **Poems Page**
    * Poems page is the page to showcase list of all poems. 
    * The list is diplayed with a blurred image as background for that particular post. 
    * The title and excrept of the poem, name of author, date of publication and number of likes visible for each post. 

        ![Poems Page](/static/assets/images/post-list.png)

    * This feature helps user choose which poem they want to read and have an insight about the poems content before openenig the post.
    * The Poems page also has *Pagination* feature with each page upto 6 posts. 

        ![Poems Page](/static/assets/images/next.png) 

        ![Poems Page](/static/assets/images/prev.png)
        
* **Sign Up**
    * Users can register and create their own account. 
    * The sign-up form checks if the username is used by someone else, alerts the user if any infomration is incorrect, such as passwords not matching or empty required fields.
    * Creating account enables access to more features. 
    * Registered members can publish and manage their poems (edit/delete).
    * These users can also like and comment on others posts.
        
        ![Sign Up](/static/assets/images/sign-up.png) 

# Future Features

# Wireframes

# Structure

# Databases
## Post Model
## Comment Model

# Technologies Used

# Frameworks, Libraries & Tools Used

# Testing

# Deployment

# Credits

# Acknowledgements
