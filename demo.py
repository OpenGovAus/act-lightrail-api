'''
This is just a little demo script I wrote to show some basics of what you can do with the API.
'''

import api

FEED_URL = 'http://files.transport.act.gov.au/feeds/lightrail.pb'

data_feed = api.download_feed(FEED_URL)

for entity in data_feed.entity:
    if(entity.HasField('vehicle')):
        vehicle_position = entity.vehicle.position
        print(vehicle_position.latitude, vehicle_position.longitude)