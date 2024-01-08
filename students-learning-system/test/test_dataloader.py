import unittest
import sys
sys.path.append('../')
sys.path.append('../src')
from src.database.dataloader import Dataloader

class TestDataloader(unittest.TestCase):

    def setUp(self):
        self.dataloader = Dataloader(student_id=1001)

    def test_get_moodle_data_columns(self):
        json_file_path = '../data/moodle/lang101.json'
        _, moodle_df, _, _ = self.dataloader.get_moodle_data(json_file_path)

        expected_columns = sorted(['Title', 'Description', 'Due Date'])
        actual_columns = sorted(list(moodle_df.columns))

        self.assertEqual(expected_columns, actual_columns, "Columns in moodle_df are not as expected")

    def test_get_gradescope_data_columns(self):
        json_file_path = '../data/gradescope/math314.json'
        hws, _, _ = self.dataloader.get_gradescope_data(json_file_path)

        expected_columns = sorted(['Title', 'Description', 'Due Date']) # Replace with expected columns
        actual_columns = sorted(list(hws.columns))

        self.assertEqual(expected_columns, actual_columns, "Columns in hws are not as expected")

    def test_get_piazza_df_columns(self):
        json_file_path = '../data/piazza/math314.json'
        piazza_df = self.dataloader.get_piazza_df(json_file_path)

        expected_columns = sorted(['title', 'topic', 'poster', 'poster_date', 'body', 'follow_up_1', 'follow_up_2',
                            'follow_up_3', 'follow_up_4'])
        actual_columns = sorted(list(piazza_df.columns))

        self.assertEqual(expected_columns, actual_columns, "Columns in piazza_df are not as expected")

if __name__ == '__main__':
    unittest.main()
