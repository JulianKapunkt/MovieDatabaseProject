import requests 

apiKey = '5067a32b'
t = "Avengers"  # Titel des Films
y = None        # Release Datum

url = "http://www.omdbapi.com/"

req = requests.get(url+'?'+'apikey='+apiKey+'&t='+t)

print (type(req.text))


