# TABLE OF CONTENT:
* [Unit Testing](#unit-testing)
    * [Testing Views](#testing-views)
    * [Testing Forms](#testing-forms)
    * [Testing Models](#testing-models)
* [Validator Testing](#validator-testing)
    * [Lighthouse Testing](#lighthouse)
    * [W3C Markup Validation](#w3c-markup-validation-servicehttpsvalidatorw3org)
    * [W3C CSS Validation Service](#w3c-css-validation-servicehttpsjigsaww3orgcss-validator)
    * [PEP8 Python Validator](#pep8-python-validatorhttppep8onlinecom)
* [Bugs](#bugs)
* [User Story Testing](#user-story-testing)
    * [Admin](#admin)
    * [Member User](#member-user)
    * [General User](#general-user)
* [Browser Compatability](#browser-compatability)
* [Responsiveness Testing](#responsiveness-testing)

# UNIT TESTING
I have used django TestCase for automated testing views, forms and models files.


## TESTING VIEWS: 
* Tested if the views are funcitoning as expected and returns pages that the user needs to be at.
    * Testing Index/Home page view:
        ```python
        class TestIndexViews(TestCase):
            def test_get_index_page(self):
                response = self.client.get('/')
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, 'index.html')
        ```

    * Testing Poem Lists Page View:
        ```python
        class TestPostListViews(TestCase):
            def test_get_post_list_page(self):
                response = self.client.get('/poem_list/')
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, 'poem_list.html')
        ```
    
    * Testing Profile Page View:
        ```python
        class TestProfileViews(TestCase):
            def test_profile_page(self):
                response = self.client.get('/profile')
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, 'profile.html')
        ```

    * Testing Adding Poems / Publish Poems Page View:
        ```python
        class TestPublishPoemViews(TestCase):
            def test_can_publish_poem(self):
                response = self.client.get('/publish')
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, 'publish.html')
        ```
    
    **Result:**
        
    ![Test Views](/documentation/test-views.png)


## TESTING FORMS: 
* Tested Poems Post form and Comment Form to make sure fields are as expected and the form is submitted to where it should:
    * Testing Poems Form:
        ```python
        class TestPoemForm(TestCase):

            def test_post_title_is_required(self):
                form = PoemForm(({'title': ''}))
                self.assertFalse(form.is_valid())
                self.assertIn('title', form.errors.keys())
                self.assertEqual(form.errors['title'][0], 'This field is required.')

            def test_post_content_is_required(self):
                form = PoemForm(({'content': ''}))
                self.assertFalse(form.is_valid())
                self.assertIn('content', form.errors.keys())
                self.assertEqual(form.errors['content'][0], 'This field is required.')

            def test_fields_are_explicit_in_form_metaclass(self):
                form = PoemForm()
                self.assertEqual(
                    form.Meta.fields, ('title', 'content', 'excerpt', 'featured_image')
                    )
        ```
    Result:
        
    ![Test Poem Form](/documentation/test-poem-form.png)

    * Testing Comments Form:
        ```python
        class TestCommentForm(TestCase):

            def test_post_title_is_required(self):
                form = CommentForm(({'body': ''}))
                self.assertFalse(form.is_valid())
                self.assertIn('body', form.errors.keys())
                self.assertEqual(form.errors['body'][0], 'This field is required.')

            def test_fields_are_explicit_in_form_metaclass(self):
                form = CommentForm()
                self.assertEqual(form.Meta.fields, ('body',))
        ```
        Result:
        
        ![Test Comments Form](/documentation/test-comment-form.png)


## Testing Models:
* Models are tested while testing views and forms as well. But in addition, I tested if the models shows that featured image is a requirement and successfully sent to the database:

    ```python
        class TestModels(TestCase):
            def test_has_featured_image(self):
            self.assertTrue(Post.featured_image)
    ```

    Result:
        
    ![Test Models](/documentation/test-models.png)

# Validator Testing
## Lighthouse
* Testing results:

    ![lighthouse](/documentation/lighthouse.png)

## [W3C Markup Validation Service](https://validator.w3.org/)
*  Errors and warnings found, reported as [bug](#bug-found-while-html-validation-testing), resolved the issues and all tests passed. [Click here](#bug-found-while-html-validation-testing) to view bug details.
    
    * Home Page:
        
        ![html home](/documentation/html-home.png)
    
    * Poem List Page:
        
        ![html poem list page](/documentation/html-poem-list.png)
    
    * Poem Details:
        
        ![html poem details](/documentation/html-poem-detail.png)
    
    * Sign-up page:
        
        ![sign up](/documentation/html-signup.png)
    
    * Login page:
        
        ![login](/documentation/html-login.png)
    
    * Logged in home page:
        
        ![Logged in home](/documentation/html-loggedin-home.png)
    
    * Logout:
        
        ![logout](/documentation/html-logout.png)
    
    * Poem Publish Page:
        
        ![html publish page](/documentation/html-publish.png)
    
    * Profile:
        
        ![profile page](/documentation/html-profile.png)

## [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
* No errors or warnings found:

    ![css validation](/documentation/css-validation.png)

## [PEP8 Python Validator](http://pep8online.com/)
* No errors or warnings found.
* models.py :

    ![models.py](/documentation/pep8-models.png)

* admin.py:

    ![admin.py](/documentation/pep8-admin.png)

* poems - urls.py:

    ![poems-urls.py](/documentation/pep8-urls.png)

* views.py:

    ![views.py](/documentation/pep8-views.png)

* forms.py:

    ![forms.py](/documentation/pep8-forms.png)

* test_views.py:

    ![test_views.py](/documentation/pep8-test-views.png)
    
* test_models.py:

    ![test_models.py](/documentation/pep8-test-models.png)

* test_forms.py:

    ![test_forms.py](/documentation/pep8-test-forms.png)

* apps.py:

    ![apps.py](/documentation/pep8-apps.png)

* asgi.py:

    ![asgi.py](/documentation/pep8-asgi.png)

* project - urls.py:

    ![project - urls.](/documentation/pep8-project-urls.png)


# BUGS
[Click here to view Bugs issues in GitHub](https://github.com/MerveKucukzoroglu/harmonic-poems/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

![bug issues page](/documentation/bug-issues.png)

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

* ### Bug found while HTML validation Testing:
    * During the HTML validator testing for some of the poems content page, I came accross an error and warning with `<o:p>`. 

        ![html error](/documentation/html-error.png)

    * The error displayed was for each paragraph. This was not familiar to me as there was nothing like `<o:p>` anywhere within my code. To figure out what is causing the error and where it is coming from, I opened one of the poems and did 'View Page Source'.

        ![page-source-error-view](/documentation/page-source-error-view.png)

    * I did a search on Google for what `<o:p>` means and how did it end up in my code if I have not added it myself. I found that "`<o:p>` means 'Office namespace'" from [Stack Overflow](https://stackoverflow.com/questions/7808968/what-do-op-elements-do-anyway#:~:text=For%20your%20specific%20question..%20the,equivalent%22%20and%20they%20have%20more.):

        ![Stack explanation for op error](/documentation/stack-explanation.png)

    *  This meant that the poems I added contained hidden Microsoft word tags. These hidden "Office Paragraph `<o:p>` tags" got carried along with the poem content when I copy + pasted the poem direclty from Microsoft Word document to the admin panel.

    * As a solution, my mentor from Code Institute - Tim Nelson, suggested me to first paste those poems that contained this bug to any 'Notes' file. The 'Notes' removes any kind of html tags or decorators. And later copy + paste them to their relevant posts. 
    
    * After following these steps, all the tests passed HTML validator testing without any issues or warnings.

* **Unsolved Bug**:
    * Once the user submits a poem, and if the admin edits any part of the users submission, such as a space or extra line, all the html content(tags and css) gets visible to user if they want to edit their own post after. 

        ![unsolved bug](/documentation/unsolved-bug.png)

    * If the post submitted by the user in not touched by admin, these codes are hidden to user, when they want to edit back their own post.

# User Story Testing

## Admin
* As a Site Admin I can approve or disapprove posts so that I can filter out objectionable posts.
* As a Site Admin I can create, read, update and delete posts so that I can manage my blog content.
* As a Site Admin I can aproove Posts before it is published so that the site content will be consistent.

    ![Admin](/documentation/admin-approve.png)

## Member User
* As a Member User I can register an account so that I can manage my posts, comment and like.

    ![Register](/documentation/sign-up.png)

* As a Member User I can post/add/edit/delete poems so that I can share and manage my poems.

    ![Profile](/documentation/user-account.png)

* As a Member User I can like or unlike a post so that I can interact with the content.
* As a Member User I can leave comments on a post so that I can be involved in the conversation.

    ![Likes and Comments](/documentation/registered-like-comment.png)

* As a Member User I can view my posts status of approval so that I can manage my poems.

    ![Manage My Poems](/documentation/manage-my-poems.png)

## General User
* As a Site User I can view a list of posts so that I can select one to read.

    ![Post List](/documentation/post-list.png)

* As a Site User I can click on a post so that I can read the full text.

    ![Post content](/documentation/user-post-content.png)

* As a Site User / Admin user I can view comments on an individual post so that I can read the conversation.
* As a Site User / Admin I can view the number of likes on each post so that I can see which is the most popular or viral.

    ![likes and comments](/documentation/likes-comments.png)

# Browser Compatability
* Checked and verified that the site works on different browsers. 
* Safari:

    ![Safari](/documentation/safari.png)

* Chrome:

    ![Chrome](/documentation/chrome.png)

# Responsiveness Testing

* Desktop - Large Screen sizes:

    ![Desktop](/documentation/chrome.png)

* Ipad - Medium Screen sizes:

    ![Ipad](/documentation/ipad.png)

* Mobile - Small Screen Sizes:

    ![Mobile](/documentation/mobile.png)