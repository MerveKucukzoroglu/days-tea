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
*  No errors or warnings found:
    
    * Home Page
        ![html home](/documentation/html-home.png)
    
    * Poem List Page
        ![html poem list page](/documentation/html-poem-list.png)
    
    * Poem Details
        ![html poem details](/documentation/html-poem-detail.png)
    
    * Sign-up page
        ![sign up](/documentation/html-signup.png)
    
    * Login page
        ![login](/documentation/html-login.png)
    
    * Logged in home page
        ![Logged in home](/documentation/html-loggedin-home.png)
    
    * Logout
        ![logout](/documentation/html-logout.png)
    
    * Poem Publish Page
        ![html publish page](/documentation/html-publish.png)
    
    * Profile
        ![profile page](/documentation/html-profile.png)

## [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
* No errors or warnings found:

    ![css validation](/documentation/css-validation.png)

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

