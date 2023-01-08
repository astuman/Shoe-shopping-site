from django.test import SimpleTestCase
from django.urls import reverse, resolve
from shoeshop.views import *
from django.contrib.auth.views import LoginView,LogoutView
from shoeshop import test


class TestUrls(SimpleTestCase):
    def test_home_view_is_resolved(self):
        url = reverse('')
        print(resolve(url))
        self.assertEqual(resolve(url).func, home_view)
    
    def test_afterlogin_view_is_resolved(self):
        url = reverse('afterlogin')
        print(resolve(url))
        self.assertEqual(resolve(url).func, afterlogin_view)
    def test_contactus_view_is_resolved(self):
        url = reverse('contactus')
        print(resolve(url))
        self.assertEqual(resolve(url).func, contactus_view)

    def test_search_view_is_resolved(self):
        url = reverse('search')
        print(resolve(url))
        self.assertEqual(resolve(url).func, search_view)
