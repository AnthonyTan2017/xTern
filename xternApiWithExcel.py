from pprint import pprint
import os
import googlemaps # pip install googlemaps
import win32com.client as win32

# API_KEY = open('API_KEY.txt').read()
map_client = googlemaps.Client('AIzaSyDyycuzhKtyHuHEOQjrVzbvjlomP65cbGk')

def get_place_info(location_name):
    try:
        response = map_client.places(query=location_name)
        results = response.get('results')[0]
        return results
    except Exception as e:
        print(e)
        return None

xlApp = win32.Dispatch('Excel.Application')
xlApp.Visible = True
wb = xlApp.workbooks.open(os.path.join(os.getcwd(), 'xternDataScience.xlsx'))
wsList = wb.Worksheets('Sheet1')

LastRow = wsList.Cells(wsList.Rows.Count, 'A').End(-4162).Row

for i in range(2, LastRow+1):
    # LastRow+1
    place_info = get_place_info(wsList.Cells(i, 1).Value)
    wsList.cells(i, 2).Value = place_info['name']
    wsList.cells(i, 3).Value = place_info['formatted_address']
    wsList.cells(i, 4).Value = place_info['place_id']
    wsList.cells(i, 5).Value = place_info['rating']
    wsList.cells(i, 6).Value = place_info['user_ratings_total']
    wsList.cells(i, 7).Value = place_info['types']
wb = None
wsList = None
xlApp = None
# source :https://learndataanalysis.org/source-code-find-places-and-businesses-with-google-maps-api-in-python/