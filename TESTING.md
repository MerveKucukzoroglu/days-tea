# Unit Testing
I have used django TestCase for automated testing views, forms and models files.
* **Testing Views**: Tested if the views are funcitoning as expected and returns pages that the user needs to be at.
* **Testing Forms**: Tested Poems Post form and Comment Form to make sure fields are as expected and the form is submitted to where it should.
* **Testing Models**: Models are tested while testing views and forms as well. But in addition, I tested if the models shows that featured image is a requirement and successfully sent to the database.

# Testing
* *Lighthouse* testing results:

    ![lighthouse](/static/assets/images/lighthouse.png)

* *[W3C Markup Validation Service](https://validator.w3.org/)* No errors or warnings found:

    ![html validation](/static/assets/images/html-validation.png)

* *[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)* No errors or warnings found:

    ![css validation](/static/assets/images/css-validation.png)

# BUGS
Throughout the development project, I came accross several bugs. I have noted them in projects page as issues in Github, you can view them [here](https://github.com/MerveKucukzoroglu/harmonic-poems/issues?q=label%3Abug+is%3Aclosed). The bugs found and resolved are as follows:

* [Wire-up poems list page once opened.](https://github.com/MerveKucukzoroglu/harmonic-poems/issues/22): 
    * The list of post is not visible when the page is opened. 
    * Contacted Code institute tutor support. The issue was in views.py.
    * Details can be viewed along with the bugs screenshots [here](https://github.com/MerveKucukzoroglu/harmonic-poems/issues/22).

* [View submitted poem form as admin and approve to publish it in poems page](https://github.com/MerveKucukzoroglu/harmonic-poems/issues/29):
    * The form to submit a poem is created. Form is visible by authenticated user and can be submitted. It is not known where the form is submitted currently. The form must be visible to admin to be approved.
    * The bug avoided me to submit the form from front end. The form submitted was not getting submitted to Admin panel to get approved.
    * Steps taken:
        * Contacted Code Insitute's Tutor Support.
        * Suggestions to make following changes to my views.py file and from django.contrib.auth.models import User
    * Details can be viewed along with the bugs screenshots [here](https://github.com/MerveKucukzoroglu/harmonic-poems/issues/29).

* [Image upload does not save, placeholder image publishes.](https://github.com/MerveKucukzoroglu/harmonic-poems/issues/30):
    * The user can upload the image, the form gets through correctly. However, the image is not saved and placeholder image gets published.
    * Add `request.FILES` in views.py. Images were uploading, but after submitting the form it did not get through, so placeholder image was in use. Now the user image upload is working.
    * Details can be viewed along with the bugs screenshots [here](https://github.com/MerveKucukzoroglu/harmonic-poems/issues/30).

* [delete the correct post](https://github.com/MerveKucukzoroglu/harmonic-poems/issues/37):
    * When user wants to delete a post of their own, the latest post added gets deleted. The post user choses to delete is therefore not deleted if it is not the latest one.
    * Code Institute tutor support suggested me to target delete modal id with:
        * `id="deleteModal{{ post.id }}"` and the button to trigger it would have `data-bs-target="#deleteModal{{ post.id }}"`
    *  * Details can be viewed along with the bugs screenshots [here](https://github.com/MerveKucukzoroglu/harmonic-poems/issues/37).

