from bs4 import BeautifulSoup
from django.template import Context
from django.template.base import Template
from django.test import TestCase


class TestLazySizes(TestCase):
    def test_lazysize_images_template_tag_should_replace_img_src_and_add_class(self):
        template = """
        {{% load lazysizes_tags %}
        {% lazysize_images %}
            <img src="http://someurl.com" />
        {% endlazysize_images %}
        """

        soup = BeautifulSoup(Template(template).render(Context()), 'lxml')
        for img in soup.find_all('img'):
            self.assertNotIn('src', img.attrs)
            self.assertIn('data-src', img.attrs)
            self.assertIn('lazyload', img.attrs.get('class', []))

    def test_lazysize_images_template_tag_should_not_touch_img_with_emtpy_src(self):
        template = """
        {{% load lazysizes_tags %}
        {% lazysize_images %}
            <img src="" />
        {% endlazysize_images %}
        """

        soup = BeautifulSoup(Template(template).render(Context()), 'lxml')
        for img in soup.find_all('img'):
            self.assertNotIn('src', img.attrs)
            self.assertNotIn('data-src', img.attrs)
            self.assertNotIn('lazyload', img.attrs.get('class', []))

    def test_lazysize_images_template_tag_should_not_touch_img_without_src(self):
        template = """
        {{% load lazysizes_tags %}
        {% lazysize_images %}
            <img />
        {% endlazysize_images %}
        """

        soup = BeautifulSoup(Template(template).render(Context()), 'lxml')
        for img in soup.find_all('img'):
            self.assertNotIn('src', img.attrs)
            self.assertNotIn('data-src', img.attrs)
            self.assertNotIn('lazyload', img.attrs.get('class', []))

    def test_lazysize_images_template_tag_should_not_touch_already_lazysizes_img(self):
        template = """
        {{% load lazysizes_tags %}
        {% lazysize_images %}
            <img data-src="http://someurl.com" class="lazyload" />
        {% endlazysize_images %}
        """

        soup = BeautifulSoup(Template(template).render(Context()), 'lxml')
        for img in soup.find_all('img'):
            self.assertNotIn('src', img.attrs)
            self.assertIn('data-src', img.attrs)
            self.assertIn('lazyload', img.attrs.get('class', []))
