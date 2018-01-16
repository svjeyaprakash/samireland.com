from .base import FunctionalTest

class WritingPageTests(FunctionalTest):

    def test_writing_page_layout(self):
        # The user goes to the writing page
        self.get("/")
        nav = self.browser.find_element_by_tag_name("nav")
        nav_links = nav.find_elements_by_tag_name("a")
        self.click(nav_links[3])

        # The page has the correct heading
        self.check_page("/writing/")
        self.check_title("Writing")
        self.check_h1("Writing")

        # There's some summary text
        summary = self.browser.find_element_by_class_name("summary")
        with self.assertRaises(self.NoElement):
            summary.find_element_by_tag_name("button")
        with self.assertRaises(self.NoElement):
            summary.find_element_by_tag_name("form")

        # There is a writing section
        articles = self.browser.find_element_by_id("articles")
        self.assertIn("no articles", articles.text)
        with self.assertRaises(self.NoElement):
            articles.find_element_by_tag_name("a")


    def test_can_change_writing_page_text(self):
        self.check_editable_text("/writing/", "summary")



class ArticleAdditionTests(FunctionalTest):

    def test_can_add_article(self):
        self.login()
        self.get("/writing/")

        # There is a link to create a new article
        articles = self.browser.find_element_by_id("articles")
        link = articles.find_element_by_tag_name("a")
        self.click(link)

        # They are on the new project page
        self.check_page("/writing/new/")
        self.check_title("New Article")
        self.check_h1("New Article")

        # There is a form
        form = self.browser.find_element_by_tag_name("form")
        id_input = form.find_elements_by_tag_name("input")[0]
        title_input = form.find_elements_by_tag_name("input")[1]
        date_input = form.find_elements_by_tag_name("input")[2]
        body_input = form.find_elements_by_tag_name("textarea")[0]

        # They enter some data and submit
        id_input.send_keys("my-first-article")
        title_input.send_keys("My First Article")
        date_input.send_keys("01-06-2017")
        body_input.send_keys("Line 1\n\nLine 2")
        submit = form.find_elements_by_tag_name("input")[-1]
        self.click(submit)

        # They are on the page for the new article
        self.check_page("/writing/my-first-article/")
        self.check_title("My First Article")
        self.check_h1("My First Article")

        # There is a date
        date = self.browser.find_element_by_class_name("date")
        self.assertEqual(date.text, "1 June, 2017")

        # There is a body
        body = self.browser.find_element_by_class_name("article-body")
        paragraphs = body.find_elements_by_tag_name("p")
        self.assertEqual(len(paragraphs), 2)
        self.assertEqual(paragraphs[0].text, "Line 1")
        self.assertEqual(paragraphs[1].text, "Line 2")

        # They go back to the writing page and the article is there too
        self.get("/writing/")
        articles = self.browser.find_element_by_id("articles")
        self.assertNotIn("no publications", articles.text)
        articles = articles.find_elements_by_class_name("article")
        self.assertEqual(len(articles), 1)
        self.assertEqual(
         articles[0].find_element_by_class_name("article-title").text,
         "My First Article"
        )
        self.assertEqual(
         articles[0].find_element_by_class_name("article-date").text,
         "1 June, 2017"
        )
        self.assertEqual(
         articles[0].find_element_by_class_name("article-link").text,
         "Read More"
        )
        self.click(articles[0].find_element_by_tag_name("a"))
        self.check_page("/writing/my-first-article/")