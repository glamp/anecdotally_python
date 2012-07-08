import unittest
from anecdotally import Anecdotally

from test_properties import api_test_key


class AnecdotallyPrograms(unittest.TestCase):
    def setUp(self):
        self.anecdotally = Anecdotally(api_test_key)

    def test_basic(self):
        self.assertEqual(self.anecdotally.apikey, api_test_key)

    def test_get_one(self):
        progs = self.anecdotally.programs.find_one()
        self.assertEqual(progs['status'], "success")
        self.assertTrue(isinstance(progs['response'], dict))

    def test_get_many(self):
        progs = self.anecdotally.programs.find({})
        self.assertEqual(progs['status'], "success")
        self.assertEqual(len(progs['response']) > 2, True)

class AnecdotallyAnecdotes(unittest.TestCase):
    def setUp(self):
        self.anecdotally = Anecdotally(api_test_key)

    def test_basic(self):
        self.assertEqual(self.anecdotally.apikey, api_test_key)

    def test_get_one(self):
        progs = self.anecdotally.anecdotes.find_one()
        self.assertEqual(progs['status'], "success")
        self.assertTrue(isinstance(progs['response'], dict))

    def test_get_many(self):
        progs = self.anecdotally.anecdotes.find({})
        self.assertEqual(progs['status'], "success")
        self.assertEqual(len(progs['response']) > 2, True)

    def test_create(self):
        data = {
            "program_ref":"4ff8f549e4b099a44894961b",
            "category":["history"],
            "headline":"A Tweet for the Ages",
            "text": "This is some content to display",
            "media_url":"http://www.twitter.com/",
            "media_credit":"Joe Smith",
            "media_caption": "look at this tweet!",
            "display_time":99999,
            "created_by_name":"lamp.greg@gmail.com"
        }
        rsp = self.anecdotally.anecdotes.create(data)
        self.assertEqual(rsp['status'], "success")

    def test_delete(self):
        to_delete = self.anecdotally.anecdotes.find({"headline":"A Tweet for the Ages"})
        for anecdote in to_delete['response']:
            rsp = self.anecdotally.anecdotes.delete({}, {"_id":anecdote['_id']})
            self.assertEqual(rsp['status'], "success")

class AnecdotallyUsers(unittest.TestCase):
    def setUp(self):
        self.anecdotally = Anecdotally(api_test_key)

    def test_basic(self):
        self.assertEqual(self.anecdotally.apikey, api_test_key)

    def test_get_one(self):
        progs = self.anecdotally.users.find_one()
        self.assertEqual(progs['status'], "success")
        self.assertTrue(isinstance(progs['response'], dict))

    def test_get_many(self):
        progs = self.anecdotally.users.find({})
        self.assertEqual(progs['status'], "success")
        self.assertEqual(len(progs['response']) > 2, True)


if __name__ == '__main__':
    unittest.main()