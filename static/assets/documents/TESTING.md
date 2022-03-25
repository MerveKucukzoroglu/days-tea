# Manual Testing
I have used django TestCase for manually testing views, forms and models files.
* Testing Views : Tested if the views are funcitoning as expected and returns pages that the user needs to be at.
* Testing Forms: Tested Poems Post form and Comment Form to make sure fields are as expected and the form is submitted to where it should.
* Testing Models: Models are tested while testing views and forms as well. But in addition, I tested if the models shows that featured image is a requirement and successfully sent to the database.

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
