import unittest
import pprint as pp
from datetime import datetime
import anecdotally
from test_properties import *

class ProgramTest(unittest.TestCase):
    def setUp(self):
        self.api = anecdotally.Anecdotally(username, api_key, dev=True)

    def test_b_get(self):
        """
        Test a basic get
        """
        self.assertEqual(len(self.api.programs.find_one()['objects']), 1)
        self.assertTrue(self.api.programs.find({})['meta']['total_count'] >= 1)

    def test_a_post(self):
        """
        Tests creating an object
        """
        data = {
            "id":"2012000",
            "name":"MYTEST",
            "summary": "You can image how suprised I was...",
            "episode": 2,
            "season":1,
            "media_type":"tv",
            "genre":"thriller",
            "date_released":"2012-01-01"
        }
        rsp = self.api.programs.create(data)
        self.assertEqual(rsp.get("ERROR"), None)

    def test_c_put(self):
        """
        Tests editing an object
        """

        program = self.api.programs.find({"id": "2012000"}).get("objects")[0]
        program['episode'] = 999
        rsp = self.api.programs.edit({"id":"2012000"}, program)
        self.assertEqual(rsp.get("ERROR"), None)

    # def test_d_delete(self):
    #     """
    #     Tests delete an object
    #     """

    #     deleteable_programs = self.api.programs.find({"id":"2012000"}).get("objects")

    #     self.assertTrue(len(deleteable_programs) > 0)

    #     for program in deleteable_programs:
    #         rsp = self.api.programs.delete({"id":program["id"]}, {})

class AnecdoteTest(unittest.TestCase):
    def setUp(self):
        self.api = anecdotally.Anecdotally(username, api_key, dev=True)

    def test_b_get(self):
        """
        Test a basic get
        """
        self.assertEqual(len(self.api.anecdotes.find_one()['objects']), 1)
        self.assertTrue(self.api.anecdotes.find({})['meta']['total_count'] >= 1)

    def test_a_post(self):
        """
        Tests creating an object
        """
        anecdote_data = {
            "id":"1234456",
            "program":"/api/v1/programs/2012000/",
            "user":"/api/v1/users/1/",
            "category":"funny",
            "headline":"This is a headline",
            "text":"this is some text",
            "media_url":"http://www.twitter.com/someurl",
            "media_credit":"glamp",
            "media_caption":"this is a caption",
            "display_time":50000
        }
        rsp = self.api.anecdotes.create(anecdote_data)
        self.assertEqual(rsp.get("ERROR"), None)

    def test_c_put(self):
        """
        Tests editing an object
        """

        anecdote = self.api.anecdotes.find({"id": "1234456"}).get("objects")[0]
        anecdote['category'] = "sad"
        rsp = self.api.anecdotes.edit({"id":"1234456"}, anecdote)
        self.assertEqual(rsp.get("ERROR"), None)

    def test_d_delete(self):
        """
        Tests delete an object
        """

        deleteable_aneccotes = self.api.anecdotes.find({"id":"1234456"}).get("objects")

        self.assertTrue(len(deleteable_aneccotes) > 0)

        for anecdote in deleteable_aneccotes:
            rsp = self.api.anecdotes.delete({"id":anecdote["id"]}, {})

if __name__ == '__main__':
    unittest.main()