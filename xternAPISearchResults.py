import requests, json
  
# enter your api key here
api_key = 
  
# url variable store url
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
location = "39.791000, -86.148003"
radius = 2000
place = ['amusement_park'
# ,'aquarium'
,'art_gallery'
# ,'atm'
# ,'bakery'
# ,'bank'
# ,'bar'
# ,'beauty_salon'
# ,'bicycle_store'
# ,'book_store'
# ,'bowling_alley'
# ,'bus_station'
# ,'cafe'
# ,'campground'
# ,'car_dealer'
# ,'car_rental'
# ,'car_repair'
# ,'car_wash'
# ,'casino'
# ,'cemetery'
# ,'church'
# ,'city_hall'
# ,'clothing_store'
# ,'convenience_store'
# ,'courthouse'
# ,'dentist'
# ,'department_store'
# ,'doctor'
# ,'drugstore'
# ,'electrician'
# ,'electronics_store'
# ,'embassy'
# ,'fire_station'
# ,'florist'
# ,'funeral_home'
# ,'furniture_store'
# ,'gas_station'
# ,'gym'
# ,'hair_care'
# ,'hardware_store'
# ,'hindu_temple'
# ,'home_goods_store'
# ,'hospital'
# ,'insurance_agency,'
# ,'jewelry_store'
# ,'laundry'
# ,'lawyer'
# ,'library'
# ,'light_rail_station'
# ,'liquor_store'
# ,'local_government_office'
# ,'locksmith'
# ,'lodging'
# ,'meal_delivery'
# ,'meal_takeaway'
# ,'mosque'
# ,'movie_rental'
# ,'movie_theater'
# ,'moving_company'
,'museum'
# ,'night_club'
# ,'painter'
,'park'
# ,'parking'
# ,'pet_store'
# ,'pharmacy'
# ,'physiotherapist'
# ,'plumber'
# ,'police'
# ,'post_office'
# ,'primary_school'
# ,'real_estate_agency'
,'restaurant'
# ,'roofing_contractor'
# ,'rv_park'
# ,'school'
# ,'secondary_school'
# ,'shoe_store'
# ,'shopping_mall'
# ,'spa'
# ,'stadium'
# ,'storage'
# ,'store'
# ,'subway_station'
# ,'supermarket'
# ,'synagogue'
# ,'taxi_stand'
,'tourist_attraction'
# ,'train_station'
# ,'transit_station'
# ,'travel_agency'
# ,'university'
# ,'veterinary_care'
# ,'zoo'
]
# The text string on which to search
# query = input('Search query: ')
  
# get method of requests module
# return response object
# r = requests.get(url + 'query=' + query +
#                         '&key=' + api_key)
for i in place:
    r = requests.get(url + '&location=' +str(location)+'&radius='+str(radius) +   
    '&type='+i+'&key=' + api_key) 
# json method of response object convert
#  json format data into python format data
    x = r.json()
    # next_page_token = r.json().get('next_page_token')

    # while next_page_token:
    #     r = requests.get(url + '&pagetoken=' + next_page_token)

    # # Parse the results page

    #     next_page_token = r.json().get('next_page_token') 
# now x contains list of nested dictionaries
# we know dictionary contain key value pair
# store the value of result key in variable y
    y = x['results']
  
# keep looping upto length of y
    for i in range(len(y)):
      
    # Print value corresponding to the
    # 'name' key at the ith index of y
        print(y[i]['name'])
    # https://www.geeksforgeeks.org/python-get-set-places-according-search-query-using-google-places-api/
