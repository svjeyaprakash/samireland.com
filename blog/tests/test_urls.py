from samireland.tests import UrlTest
from blog import views

class BlogUrlTests(UrlTest):

    def test_new_blog_url_resolves_to_new_blog_view(self):
        self.check_url_returns_view("/blog/new/", views.new_blog_page)


    def test_blog_url_resolves_to_blog_view(self):
        self.check_url_returns_view("/blog/", views.blog_page)


    def test_blog_post_url_resolves_to_blog_post_view(self):
        self.check_url_returns_view("/blog/2000/9/28/", views.one_post_page)


    def test_blog_year_url_resolves_to_blog_year_view(self):
        self.check_url_returns_view("/blog/2000/", views.year_page)


    def test_edit_blog_url_resolves_to_edit_blog_view(self):
        self.check_url_returns_view("/blog/2000/9/28/edit/", views.edit_post_page)


    def test_delete_blog_url_resolves_to_delete_blog_view(self):
        self.check_url_returns_view("/blog/2000/9/28/delete/", views.delete_post_page)
