# act-lightrail-api

Python wrapper for Transport Canberra's GTFS-R Lightrail feed

Info [here](https://www.transport.act.gov.au/contact-us/information-for-developers).

Unlike [act-nxtbus-api](https://github.com/OpenGovAus/act-nxtbus-api), you won't need an API key to access any of the Lightrail data.

## Setup

### Installation

Clone repository:
```sh
git clone https://github.com/OpenGovAus/act-lightrail-api.git
```

Enter cloned repository:
```sh
cd act-lightrail-api
```

Install `poetry`:

```sh
pip3 install poetry
```

Update/install Python dependencies:
```
poetry update
```

## Usage

To get a brief overview at the functions of the wrapper, run `demo.py`:

```sh
poetry run python3 demo.py
```

### Interacting with the API

Begin by importing the API:

```py
import api
```

You'll need to tell the API where to find the data. Transport Canberra uses a GTFS-R specification behind a ProtocolBuffer feed to serve the data. If you don't know what that means, don't stress, that's what this API is for.

This is the feed URL: [http://files.transport.act.gov.au/feeds/lightrail.pb](http://files.transport.act.gov.au/feeds/lightrail.pb).

Simply copy it into a script like this:

```py
lightrail_feed = api.download_feed('http://files.transport.act.gov.au/feeds/lightrail.pb')
```

`lightrail_feed` now contains all the data for vehicles and stop IDs (not the actual stops) in a JSON-like format. You can refer to different chunks of the data by just navigating it like a standard Python object.

`entity` is the actual block of data, some of these are for vehicles and others are for stops.

```py
for entity in lightrail_feed.entity:
    if(entity.HasField('vehicle')): # Check if this block of data contains information about a lightrail vehicle.
        print(entity)
```

Prints something similar to this for each vehicle:

```sh
id: "102778725"
vehicle {
  trip {
    trip_id: "811"
    schedule_relationship: SCHEDULED
  }
  position {
    latitude: -35.22311
    longitude: 149.14407
    bearing: 193.02516
    odometer: 136838673.0
    speed: 2.5472221
  }
  current_stop_sequence: 9
  current_status: IN_TRANSIT_TO
  timestamp: 1619416710
  congestion_level: RUNNING_SMOOTHLY
  stop_id: "8111"
  vehicle {
    id: "1"
    label: "LRV1"
    license_plate: "LRV1"
  }
  occupancy_status: EMPTY
}
```

Then, you can access each value like a Python object, in this case we'll get the vehicle's location:

```py
for entity in lightrail_feed.entity:
    if(entity.HasField('vehicle')):
        vehicle_position = entity.vehicle.position
        print(vehicle_position.latitude, vehicle_position.longitude)
```

The above script would print the latitude and longitude of every active lightrail vehicle in Canberra, like this:

```sh
-35.235497 149.14442
-35.25031661987305 149.13377380371094
-35.18691635131836 149.1432647705078
-35.26974868774414 149.13059997558594
```

You can then use that GPS data with other applications, like Google Maps:

![Lightrail GPS data in Google Maps](/.github/img/maps.jpg)