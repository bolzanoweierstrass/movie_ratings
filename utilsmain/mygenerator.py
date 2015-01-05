import requests
class Common(object):
    def __init__(self):
        self._url = 'http://omdbapi.com/'
        self.payload = {'r':'json','plot':'short','tomatoes':'true'}
    def getDataByTitle(self,title,plot="short"):
        try:
            if self.payload.has_key('s'):del self.payload['s']
            if plot == "long": self.payload.update({'plot':'full'})
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

class Tettikai(object):
    def __init__(self):
        pass
    def getIm(self,dada):
        if dada.has_key('Poster'):
            poster = dada['Poster']
            localfile = '/tmp'+'/'+ poster.split('/')[-1]
            req = requests.get(poster, stream=True)
            with open(localfile, 'w+b') as infile:
                for chunk in req.iter_content(2*1024):
                    if chunk:
                        infile.write(chunk)
                        infile.flush()
            return localfile
        else:
            pass
                
            
            
        
        