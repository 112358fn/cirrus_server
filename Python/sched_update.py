#!/usr/bin/python -u
# Filename: update_every5.py
#
# Schedule execution every 5 min
#
import sched
import time
from dest_path import get_path
from update_data import update_all_data
from gen_plotlyjs import update_graph
from datetime import date, datetime, timedelta

delay_seconds = 300
# origin = "/home/lucas/Dropbox/Cluster2/Data"
# web_root = "/home/lucas/Web/drupal/files"
origin = "test/Dropbox/Cluster1/Data"
web_root = "test/Web/drupal/files"
from_date = date(2016, 9, 19)
until_date = date(2016, 9, 20)


def sched_update():
    # until_date = datetime.today();
    # from_date = until_date - timedelta(hours=24)
    df = update_all_data(origin)
    destination = get_path(origin, web_root)
    temp_uri, hum_uri = update_graph(df, destination, from_date, until_date)
    print(temp_uri)
    print(hum_uri)
    # do your stuff
    s.enter(delay_seconds, 1, sched_update, ())


s = sched.scheduler(time.time, time.sleep)
s.enter(delay_seconds, 1, sched_update, ())
s.run()
