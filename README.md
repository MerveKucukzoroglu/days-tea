# About
Harmonic Poems is a platform for poets to share their poems and inspire young poets. This platforms aims to be a Harmonic Poets Community, where poets can like, comment and share their poems with the world. 

![Am I Responsive](/documentation/am-i-responsive.png) 

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
        
        ![Home Page](/documentation/home-page.png)

    * If the user is logged in member, the navigation bar will have an accunts icon and instead of login, one of the buttons takes the user to their account profile.
        
        ![Home Page](/documentation/member-home-page.png)
    
    * The Poem button takes any site user to the list of poems page for any user to access and read.

* **Poems Page**
    * Poems page is the page to showcase list of all poems. 
    * The list is diplayed with a blurred image as background for that particular post. 
    * The title and excrept of the poem, name of author, date of publication and number of likes visible for each post. 

        ![Poems Page](/documentation/post-list.png)

    * This feature helps user choose which poem they want to read and have an insight about the poems content before openenig the post.
    * The Poems page also has *Pagination* feature with each page upto 6 posts. 

        ![Poems Page](/documentation/next.pgn) 

        ![Poems Page](/documentation/prev.png)
        
* **Sign Up**
    * Users can register and create their own account. 
    * The sign-up form checks if the username is used by someone else, alerts the user if any infomration is incorrect, such as passwords not matching or empty required fields.
    * Creating account enables access to more features. 
    * Registered members can publish and manage their poems (edit/delete).
    * These users can also like and comment on others posts.
        
        ![Sign Up](/documentation/sign-up.png)
    
* **Sign In**
    * Users can access their account via sign-in/login feature.
    * By logging in the users can publish and manage their poems (edit/delete). They can also like and comment on others posts.
    * Users can find login option from Menu and from home page.
    * If the user don't have an accoun, they can click 'sign up' link on the login page and create their account.
        
        ![Sign-in](/documentation/sign-in.png)

* **Logout**
    * The user can logout from Menu and from their accounts page.
    * When the user wants to logout a pop-up modal is triggered for confirmation. 
    * The logout modal asks the user if they confirm to logout.

        ![Logout](/documentation/log-out.png)
    
* **User Account / Profile Page**
    * Once the user is registered or logged in, they have a user profile page. 
    * In this page users can publish a poem, or manage their poems. 
    * If they want, they can access the logout feature through the logout button from this page as well.

        ![User Account](/documentation/user-account.png)
    
* **Publish a Poem**
    * Creating and adding a poem by a registered user is possible. 
    * The user can publish a poem after signing in and from their profile page.
    * The user must enter a title, content and image. The excrept is optional if the user want to enter a brief explanation about their poem.

        ![Publish/Add poem](/documentation/publish.png)

    * Once the poem is published, the poem is submitted for approval to the admin. The submitted poem can be viewed/edited/deleted by the owner from 'Manage my poems Page'.

* **Manage My Poems Page**
    * User has the control to their published and pending approval poems.
    * The user can see the list of thier own poems from 'Manage My Poems' page.
    * Each poem listed has information about that particular post/poem. 
    * Status of poem: If the poem is sent for approval and is not yet publlished, it displays "pending approval on the top". If it is approved by the admin and is published, at top it displays "Published" with a green icon next to it.
    * The poem title, excrept and the date/time of submission is present separately for each post.
    * Finally, the buttons for editing and deleting options are given for the user management.
    * The listing is sorted out from latest created/updated at the top of the page and the old ones are below.
    * The poems are approved by the admin. This is to ensure that poems submitted are by the user and is not by another poet.

        ![Manage My Poems](/documentation/manage-my-poems.png)

* **Edit a Poem**
    * The authenticated and owner of the poem can only edit the poem.
    * Both the pending approval poems and published (approved) poems can be edited. 
    * The poems that are selected for editing are prepopulated form that is ready for editing.

         ![Edit a poem](/documentation/edit.png)

* **Delete a Poem**
    * The authenticated and owner of the poem can only delete the poem.
    * Both the pending approval poems and published (approved) poems can be deleted. 
    * The poems that are chosen to be deleted asks the user for confirmation by pop-up alert on the window.

        ![Delete a poem](/documentation/delete.png)

* **Like and Comment on a Poem Post**
    * All the site visiters can view the comments and the number of likes.
    * The unregistered site visiters cannot view the comment box to write a comment. Once they register, then it is visible for them and they can post a comment on any post they want.

        ![View likes and comments](/documentation/view-like-comment.png)

    * The registered site members can like and comment on a post.

        ![Like and comment](/documentation/registered-like-comment.png)

# Future Features
* Connect with Google translate API, so users can submit poems from different languages and also translate to language they want.
* Members can save poems that they like (inn save category) and go back to read it later.
* Users can set up their own profile page, add information about themselves, upload a profile picture and connect with other members.
* Create a community group and vote for their own admin/admins to review their poems.
* Follow other poet members.

# Wireframes
* Each pages wireframes includes mobile(small screen), tablet(medium screen), desktop(large screens).
    * Home page:
        ![Wireframes](/documentation/w-home.png)

    * Login page:
        ![Wireframes](/documentation/w-login.png)

    * Manage My Poems page:
        ![Wireframes](/documentation/w-manage-my-poems.png)

    * Poem Content:
        ![Wireframes](/documentation/w-poem-content.png)
    
    * Poem List:
        ![Wireframes](/documentation/w-poem-lists.png)
    
    * Publish Poem:
        ![Wireframes](/documentation/w-publish-poem.png)
    
    * Register:
        ![Wireframes](/documentation/w-register.png)

    * User Account Page:
        ![Wireframes](/documentation/w-user-account-page.png)

# Structure
The structure idea for Harmonic Poems was to keep it simple and unnecessary-content-free. The simplicity helps user to easily access and navigate within the application. 

Only one color shades are used throughout to keep the user focused more on the content and if any important information is to be delivered to user, such as alerts or post status. 

This project has one main app, poems blog app.

Throughout the project development, GitHub projects is used. Click [here](https://github.com/MerveKucukzoroglu/harmonic-poems/projects/1) to view the process.

# Databases
As the Harmonic Poems require a database, I have created two database models:
    ![Wireframes](/documentation/w-models.png)

## Post Model:
Post model handles poems details: title, content, approval status, date created/updated, featured image, excrept and likes. This post model handles the base for confirming user/author authentication to manage their own poems.
    
## Comment Model:
Comment model handles the content of the comment, the username of the person commenting, date/time of commenting.

# Technologies Used:
* HTML
* CSS
* JavaScript
* Python

# Frameworks, Libraries & Tools Used
* Bootstrap - grid, layout, columns, cards and forms structure.
* Django - django frameworks to manage apps.
* GitHub - to store the overall project repository.
* GitPod - used as workspace to do the coding.
* Balsamiq Wireframes - To design the wireframe of the complete project.
* Google Fonts - to brandize 'Harmonic Poems' with google fonts. Used for logo and all the written content.
* Fontawesome - fontawesome icons for social media links and as additional design.
* Heroku - for the [deployement](#deployment) of the project.
* Coolors - to choose the color palette and color shades.
* PostgreSQL - database storage of the models.
* Cloudinary - image and static files storage.
* AmIResponsinve - responsiveness of the site.
* Lighthouse - used for testing site functionality.
* W3C Markup Validation Service - used for HTML testing.
* W3C CSS Validation Service - used for CSS testing
* PEP8 - used for Python files testing.

# Testing
*Unit Testing* *Validator Testing* and *Bugs* are documented [here](/TESTING.md).

# Deployment:
Deployement has been done to [Herokuapps](https://www.heroku.com/).

* The initial deployment was immediately after cretaing all the file directories within the repository. This is to ensure and overcome any deployment error before hand and resolve the issue before it gets more complicated.
    
    * I have followed Code Institute's [Django Blog Cheat Sheet](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf) steps to follow, create and deploy the project on Herokuapps. 

    * To open an account in [Heroku](https://www.heroku.com/):
        * [Signup here](https://signup.heroku.com/) if you do not have an account already.
        * After you fill in all the information for account and sign in, you will be on Dashbord. Here is where you will create an application.
        * Click on New => Create new app.
        * Choose a name to your application and select location that you are based.

# Credits
During the process of project development, there have been various sources that gave me idea how to do a particular feature or fix a bug. The following are the sources that I got knowledge from:
* [Stack Overflow](https://stackoverflow.com/)
* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/#)
* [Django Project Documentation](https://www.djangoproject.com/)
* [Code Instiute](https://codeinstitute.net/se/full-stack-software-development-diploma/?utm_term=code%20institute&utm_campaign=CI+-+SWE+-+Search+-+Brand&utm_source=adwords&utm_medium=ppc&hsa_acc=8983321581&hsa_cam=14660337051&hsa_grp=134087657984&hsa_ad=581817633089&hsa_src=g&hsa_tgt=kwd-319867646331&hsa_kw=code%20institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gclid=Cj0KCQjw0PWRBhDKARIsAPKHFGgmnuTJCpzeJBqKg9fy2p-7NlU8NY95XaXmoPzBpuDdIekQWqUKxocaAso5EALw_wcB) course materials and Django Blog Walkthrough Project.
* [Bootstrap Navbar](https://getbootstrap.com/docs/5.0/components/navbar/)
* [Bootstrap Modal](https://getbootstrap.com/docs/5.1/components/modal/#tooltips-and-popovers)
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
* [User registration email form by Corey Schafer](https://www.youtube.com/watch?v=q4jPR-M0TAQ&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=6)
* [Coolors](https://coolors.co/) color palette
* [AmIResponsive]()for mockup of the site


# Acknowledgements
I would like to acknowledge and present my thanks to Tim Nelson, my mentor from Code Insitute for his guidance and constant support. It wouldn't have been possible without the amazing community in Slack, Tutors of Code insitute Tutor supports, and my friends who constantly motivated and supported me. 
