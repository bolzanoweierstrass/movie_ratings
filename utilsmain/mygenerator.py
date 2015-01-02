import requests

class Common(object):
    def __init__(self):
        self._url = 'http://omdbapi.com/?'
        self.payload = {'r':'json','plot':'short','tomatoes':'true'}
    def getData(self,title):
        payload = self.payload.update({'t':title})
        req = requests.get(self._url, params = payload)
        data = req.json()
        if not data.has_key('Error'):
            return data
        else:
            payload = self.payload.update({'s':title})
            req = requests.get(self._url,params = payload)
            data = req.json()
            return data
        