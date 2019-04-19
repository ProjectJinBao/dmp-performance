import requests
import datetime
import time
import mysql_handle
import json
import os

start_time = datetime.datetime.now()

median_response_time = 230
min_response_time = 223
current_rps = 2
name = "/service/s1/200ms/1k"
num_failures = 0
max_response_time = 301
avg_response_time = 231.35714285714286
num_requests = 14
user_count = 10
used_time = datetime.datetime.now() - start_time



mysql_conn = mysql_handle.mysql_handle()

sql = "insert into locust (time, median_response_time, min_response_time, current_rps, name, num_failures, " \
      "max_response_time, avg_response_time, num_requests, used_time, user_count) value (NOW(), %s, %s, %s, " \
      "\"%s\", %s, %s, %s, %s, %s, %s)" \
      % (median_response_time, min_response_time, current_rps, name, num_failures, max_response_time,
         avg_response_time, num_requests, used_time.seconds, user_count)


mysql_conn.insert_data(sql=sql)