

from unittest import TestCase

from main import get_names, get_shelves, get_list, add_doc

class TestGetNames (TestCase):

    def test_get_names(self):
        self.assertEqual(get_names(), 'Документ принадлежит: Василий Гупкин')
