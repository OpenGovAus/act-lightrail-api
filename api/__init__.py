import os, glob
from . import gtfs_realtime_pb2
from requests import get
from datetime import datetime

TIMETABLE_DIR = f'{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}/timetable/'

def download_feed(feed_url):
    lr_feed = gtfs_realtime_pb2.FeedMessage()
    lr_feed.ParseFromString(get(feed_url).content)
    return(lr_feed)

def get_epoch():
    return int(datetime.timestamp(datetime.now()))

def write_zip(timetable_url):
    with open(f'{TIMETABLE_DIR}{get_epoch()}.zip', 'wb') as f:
                f.write(get(timetable_url).content)

def get_timetable(timetable_url):
    if(not os.path.isdir(TIMETABLE_DIR)):
        os.mkdir(TIMETABLE_DIR)
    os.chdir(TIMETABLE_DIR)
    files = glob.glob('*.zip')
    if(files):
        if(get_epoch() - int(files[-1][:-4]) > 7*24*3600): # Check timetable difference every week
            for filename in files:
                os.remove(f'{TIMETABLE_DIR}{filename}')
            write_zip(timetable_url)
        else:
            if(len(files[:-1]) > 0):
                for filename in files[:-1]:
                    os.remove(f'{TIMETABLE_DIR}{filename}')
    else:
        write_zip(timetable_url)