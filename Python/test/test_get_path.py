from unittest import TestCase
from dest_path import get_path


class TestGet_path(TestCase):
    def test_get_path(self):
        path = get_path("Dropbox/Cluster1/Data", "Web/drupal/files")
        self.assertEqual("Web/drupal/files/Cluster1/Data", path, msg="Destination path generation error")
