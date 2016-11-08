from unittest import TestCase
from update_data import update_data, update_all_data


class TestUpdate_data(TestCase):
    def test_update_data(self):
        path = "Dropbox/Cluster1/Data/DataNode1.csv"
        singledata = update_data(path)
        self.assertEqual(1416, singledata.loc[1].Temp.size)

    def test_update_data_exception(self):
        path = "Dropbox/Cluster1/Data/DataNode5.csv"
        singledata = update_data(path)
        self.assertIsNone(singledata)

    def test_update_all_data(self):
        path = "Dropbox/Cluster1/Data/"
        alldata = update_all_data(path)
        self.assertEqual(1416, alldata.loc[1].Temp.size)
        self.assertEqual(1459, alldata.loc[2].Temp.size)
        self.assertEqual(6899, alldata.loc[3].Temp.size)
        self.assertEqual(6966, alldata.loc[4].Temp.size)