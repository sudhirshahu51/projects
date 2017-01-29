# To find the places to eat for the entered meal and location using api only

import json
from urllib import request


CLIENT_ID = 'NIXGTBEZBXMV34V4FEYEW3NSK5VGNA2A4KCDTIFWJM4O3SXL'		# Client id for foursquare api
CLIENT_SECRET = 'YN13GPF1NZISGAMIQZNXCSQKOBV3EEXWJHYR5RQDMPTSZZZF'	# secret id for foursquare api


def geo_location(location):			# finding the coordinates (latitude and longitude) using google map geolocation api
    google_api_key = "AIzaSyD-bpRw18oGFDix_FhqnSKlQz_Q-cVWd20"		# google geolocation map api
    location_string = location.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (location_string, google_api_key))
    result = json.loads(request.urlopen(url).read().decode('utf-8'))	# changing the type from byte to string
    try:
        latitude = result['results'][0]['geometry']['location']['lat']
        longitude = result['results'][0]['geometry']['location']['lng']
    except IndexError:				# if place not found then return 0.0 for special case
        return 0.0, 0.0
    return latitude, longitude


def find_restaurant(meal_type, location):		# function for finding the restaurants according to meal type of geographic location
    coordinates = geo_location(location)
    if coordinates[0] == 0.0 and coordinates[1] == [0.0]:	# if no place found
        return 'No such place found'
    url = 'https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20130815&ll' \
          '=%s,%s&query=%s' % (CLIENT_ID, CLIENT_SECRET, coordinates[0], coordinates[1], meal_type)
    venues = json.loads(request.urlopen(url).read().decode('utf-8'))
    try:
        rest_id = venues['response']['venues'][0]['id']	 # unique restaurant id
        rest_name = venues['response']['venues'][0]['name']	 # restaurant name
        rest_add = ','.join(venues['response']['venues'][0]['location']['formattedAddress'])  # restaurant address
        url_pic = 'https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&client_secret=%s&v=20161212&m=swarm'\
                  % (rest_id, CLIENT_ID, CLIENT_SECRET)		# url of restaurant image
        pic = json.loads(request.urlopen(url_pic).read().decode('utf-8'))
        try:
            url_pic = pic['response']['photos']['items'][0]['prefix'][:-1] + pic['response']['photos']['items'][0]['suffix']
        except IndexError:		# if no pic found
            url_pic = 'No Pic found'
        return {'name': rest_name, 'address': rest_add, 'image': url_pic}
    except IndexError:
        return "No Restaurants Found"


if __name__ == '__main__':
    meal = input('Enter the of meal you want to search\n')
    loc = input('Enter the location\n')
    print(find_restaurant(meal, loc))
