from unittest import TestCase
from gen_plotlyjs import update_graph
from update_data import update_all_data
from dest_path import get_path
from datetime import datetime
from os.path import basename


class TestUpdate_graph(TestCase):
    def test_update_graph(self):
        origin = "Dropbox/Cluster1/Data"
        web_root = "Web/drupal/files"
        df = update_all_data(origin)
        destination = get_path(origin, web_root)
        from_date = datetime(2016, 9, 19)
        until_date = datetime(2016, 9, 20)
        # until_date = datetime.today();
        # from_date = until_date - timedelta(hours=24)
        temp_uri, hum_uri = update_graph(df, destination, from_date, until_date)
        self.assertEqual("Temp_AllNodes.html", basename(temp_uri))
        self.assertEqual("Hum_AllNodes.html", basename(hum_uri))
