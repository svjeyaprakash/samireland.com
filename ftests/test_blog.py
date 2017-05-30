"""Contains tests for the blog section."""

from time import sleep
from datetime import datetime
from .base import FunctionalTest

class BlogTest(FunctionalTest):

    def enter_blog_post(self, date, title, body, visible):
        # There is a form for submitting a blog post
        h1 = self.browser.find_element_by_tag_name("h1")
        self.assertEqual(h1.text, "New Blog Post")
        form = self.browser.find_element_by_tag_name("form")
        date_input, title_input = form.find_elements_by_tag_name("input")[:2]
        body_input = form.find_element_by_tag_name("textarea")
        visible_input = form.find_elements_by_tag_name("input")[2]
        self.assertEqual(date_input.get_attribute("type"), "date")
        self.assertEqual(title_input.get_attribute("type"), "text")
        self.assertEqual(visible_input.get_attribute("type"), "checkbox")

        # The form has today's date and visibility is checked
        today = datetime.now()
        self.assertEqual(date_input.get_attribute("value"), today.strftime("%Y-%m-%d"))
        self.assertTrue(visible_input.is_selected())

        # They enter a blog post
        date_input.send_keys(date)
        title_input.send_keys(title)
        body_input.send_keys(body)
        if not visible: visible_input.click()

        # They submit the blog post
        submit = form.find_elements_by_tag_name("input")[-1]
        submit.click()



class BlogCreationTests(BlogTest):

    def test_can_create_blog_post(self):
        self.login()
        self.get("/")

        # There is a blog link in the header
        header = self.browser.find_element_by_tag_name("header")
        blog_link = header.find_element_by_id("blog-link")

        # They click it and are taken to the blog creation page
        blog_link.click()
        self.check_page("/blog/new/")

        # They enter a blog post
        self.enter_blog_post(
         "01-06-2014", "My first post", "This is my first post!\n\nIt's super.", True
        )

        # They are on the blog posts page
        self.check_page("/blog/")
        h1 = self.browser.find_element_by_tag_name("h1")
        self.assertEqual(h1.text, "Blog Posts")
        posts_section = self.browser.find_element_by_id("posts")

        # There is one blog post there
        posts = posts_section.find_elements_by_class_name("blog-post")
        self.assertEqual(len(posts), 1)

        # The post has the correct details
        date = posts[0].find_element_by_class_name("post-date")
        self.assertEqual(date.text, "1 June, 2014")
        title = posts[0].find_element_by_class_name("post-title")
        self.assertEqual(title.text, "My first post")
        body = posts[0].find_element_by_class_name("post-body")
        paragraphs = body.find_elements_by_tag_name("p")
        self.assertEqual(len(paragraphs), 2)
        self.assertEqual(paragraphs[0].text, "This is my first post!")
        self.assertEqual(paragraphs[1].text, "It's super.")


    def test_blog_post_needs_correct_date(self):
        pass


    def test_blog_post_needs_correct_title(self):
        pass


    def test_blog_post_needs_correct_body(self):
        pass



class BlogReadingTests(BlogTest):

    def test_can_cycle_between_blog_posts(self):
        pass


    def test_can_get_blog_posts_by_period(self):
        pass



class BlogModificationTests(BlogTest):

    def test_can_modify_blog_post(self):
        pass


    def test_modified_blog_post_needs_correct_date(self):
        pass


    def test_modified_blog_post_needs_correct_title(self):
        pass


    def test_modified_blog_post_needs_correct_body(self):
        pass



class BlogDeletionTests(BlogTest):

    def test_can_delete_blog_post(self):
        pass



class BlogAccessTests(BlogTest):

    def test_cannot_access_new_blog_page_when_not_logged_in(self):
        pass


    def test_cannot_access_blog_edit_page_when_not_logged_in(self):
        pass


    def test_cannot_access_blog_delete_page_when_not_logged_in(self):
        pass
