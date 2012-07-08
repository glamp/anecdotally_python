import json
import urllib, urllib2

class API(object):
    def __init__(self, apikey, endpoint):
        self.endpoint = endpoint
        self.apikey = apikey

    def _req(self, req_type, params, data):
        params['apikey'] = self.apikey
        rsp = http_request(self.endpoint, params, data, req_type)
        return rsp

    def _get(self, params={}, data={}):
        return self._req("GET", params, data)
    
    def _post(self, params={}, data={}):
        return self._req("POST", params, data)
    
    def _put(self, params={}, data={}):
        return self._req("PUT", params, data)
    
    def _delete(self, params={}, data={}):
        return self._req("DELETE", params, data)

    def find_one(self):
        return self._get({"limit":1})

    def find(self, params):
        return self._get(params)

    def create(self, data):
        return self._post({}, data)

    def edit(self, params, data):
        return self._put(params, data)

    def delete(self, params, data):
        return self._delete(params, data)



def http_request(url, params, data, method):
    "creates an http request"

    url += urllib.urlencode(params)

    try:
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        request = urllib2.Request(url, data=json.dumps(data),
                            headers={'Content-Type':'application/json'})
        request.get_method = lambda: method
        r = opener.open(request).read()
        rsp = json.loads(r)
    except:
        rsp = {"ERROR":"NO RESPONSE"}
   
    return rsp