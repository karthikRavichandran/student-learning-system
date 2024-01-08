import unittest
import os
import pandas as pd
import sys
sys.path.append('../')
sys.path.append('../src')
from src.server.llm import llm
from src.database.dataloader import Dataloader

class TestOpenAIAPI(unittest.TestCase):

    def setUp(self):
        # Set your OpenAI GPT-3.5 API key
        self.api_key = os.environ['OPENAI_API_KEY']
        self.openai_endpoint = 'https://api.openai.com/v1/engines/text-davinci-003/completions'
        self.student_id=1001
        self.dataloader = Dataloader(student_id=self.student_id)
        self.dashboard_data = self.dataloader.get_dashboard_data(f"../data/dashboard/dash_board_data.json") \
            if os.path.exists(f"../data/dashboard/dash_board_data.json") else None
        self.DashB = pd.DataFrame(self.dashboard_data)
    def test_generate_summary(self):
        self.llm = llm()
        summary_from_llm = self.llm.generate_summary(self.DashB, prompt_user=self.llm.get_prompts(field='advice')[1])
        summary_len = len(summary_from_llm.split(" "))
        # summary_len = 10
        self.assertGreater(summary_len, 5, f"The Summary doesn't have words to be considered as summary")


if __name__ == '__main__':
    unittest.main()
