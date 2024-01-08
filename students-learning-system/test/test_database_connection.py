import unittest
import sys
sys.path.append('../')
sys.path.append('../src')
from src.database.dataloader import Dataloader
from src.database.firebase_data_download import DownloadDataFirebase
import pandas as pd


class TestDataBaseConnection(unittest.TestCase):
    def setUp(self):
        self.download_data_firebase = DownloadDataFirebase(service_account_json='../data/serviceAccount.json')
        self.dataloader = Dataloader(student_id=1001)
    def test_import_firebase_collection_to_json(self):
        _ = self.download_data_firebase.import_firebase_collection_to_json(self.download_data_firebase.
                                                                           gradescope_endpoint, 'math314',
                                                                           download_path='./')
        json_file_path = './math314.json'
        f = open(json_file_path, "r")

        hws, _, _ = self.dataloader.get_gradescope_data(json_file_path)

        expected_columns = sorted(['Title', 'Description', 'Due Date'])  # Replace with expected columns
        actual_columns = sorted(list(hws.columns))

        self.assertEqual(expected_columns, actual_columns, "Columns in math314.json are not as expected")

    def test_import_firestore_collection_to_csv(self):
        _ = self.download_data_firebase.import_firestore_collection_to_csv('test', './test.csv')
        data = pd.read_csv('./test.csv')
        expected_columns = sorted(["Due_date", "Title", "Event", "Description"])
        actual_columns = sorted(list(data.columns))
        self.assertEqual(expected_columns, actual_columns, "Columns of test.csv are not as expected")


if __name__ == '__main__':
    unittest.main()
