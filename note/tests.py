from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from .models import Note


class HomeMainViewTest(TestCase):
    """"
    Tests views
    """
    def setUp(self):
        """
        Set for working tests
        """
        self.client = Client()
        self.url = reverse('index')

    def create_object(self):
        """
        Create instance of Note
        """
        Note.objects.create(
            title='Title',
            text='Note text and others other other '
                 'text something else ',
            rubric='Other'
        )

    def test_empty_index_views(self):
        """
        Test index empty index views
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Home')
        self.assertContains(response, 'About')
        self.assertContains(response, 'Contact')

        self.assertNotIn('/note/', response)
        self.assertContains(response,
                            '<script type="text/javascript" '
                            'src="/static/js/lib/jquery-3.1.1.js"></script>')
        self.assertContains(response, '<link rel="stylesheet" href="/static/css/bootstrap.css">')

    def test_index_view_with_note(self):
        """
        Test index with one note on main page
        """
        self.create_object()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '/note/1/')
        self.assertContains(response, 'Title')
        self.assertContains(response, 'Note text and others')
