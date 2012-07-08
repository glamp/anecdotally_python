from api import API

class Anecdotally(object):
    def __init__(self, apikey):
        self.apikey = apikey
        self.base_uri = "http://api.anecdotal.ly/"
        # self.base_uri = "http://127.0.0.1:8000/"
        self.programs = API(apikey, self.base_uri + "programs?")
        self.users = API(apikey, self.base_uri + "users?")
        self.anecdotes = API(apikey, self.base_uri + "anecdotes?")