import requests

class Common(object):
    def __init__(self):
        self._url = 'http://omdbapi.com/'
        self.payload = {'r':'json','plot':'short','tomatoes':'true'}
    def getDataByTitle(self,title):
        try:
            if self.payload.has_key('s'):del self.payload['s']
        finally:
            self.payload.update({'t':title})
            req = requests.get(self._url, params = self.payload)
            data = req.json()
            return data
    def getDataBySearch(self,title):
        try:
            if self.payload.has_key('t'):del self.payload['t']
        finally:
            self.payload.update({'s':title})
            req = requests.get(self._url,params = self.payload)
            data = req.json()
            return data

# class Tettikai(object):
#     def __init__(self):
#         pass
#     @classmethod
#     def setPicture(self,js_data):
#         poster = js_data['Poster']
#         req = requests.get(poster,stream=True)
#         im = Image.open(BytesIO(req.content))
#         return im
       
                
        
            
            
        
        