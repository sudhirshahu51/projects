import http.client
import json

def geo_location(inputString):
    google_api_key = "AIzaSyD-bpRw18oGFDix_FhqnSKlQz_Q-cVWd20"
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (locationString, google_api_key))
    h = http.client.HTTPConnection('maps.googleapis.com')
    result = json.loads(h.request(url,'GET')[1])
    print(result)
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return (latitude,longitude)


print(geo_location(input()))
