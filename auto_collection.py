import requests
import datetime
import time
import mysql_handle
import json
import os


def main(count, hatch_rate, users):
    # workspace_base = "/Users/xumin/Desktop/test"
    workspace_base = "/data/locust_data"
    start_time = datetime.datetime.now()

    workspace_path = create_workspace(workspace_base=workspace_base, start_time=start_time)

    start(count=users, hatch_rate=hatch_rate)
    mysql_data = mysql_handle.mysql_handle()
    for i in range(0, count, 1):
        stats(start_time=start_time, mysqlconn=mysql_data)
        time.sleep(5)
    end_time = datetime.datetime.now()

    end()
    mysql_data.close_connect()
    download_exceptions(workspace_path=workspace_path)
    donwload_statistics(workspace_path=workspace_path)
    download_distribution(workspace_path=workspace_path)

    write_time(workspace_path=workspace_path, start_time=start_time, end_time=end_time)
    print(start_time)
    print(end_time)
    print(end_time - start_time)


def start(count, hatch_rate):
    start_url = "http://106.75.239.226:8089/swarm"

    payload = "locust_count=%s&hatch_rate=%s" % (count, hatch_rate)
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "e6c9632a-87a9-f141-94ea-e1b3ae6c038b"
    }

    response = requests.request("POST", start_url, data=payload, headers=headers)
    print(response.content)


def end():
    end_url = "http://106.75.239.226:8089/stop"
    requests.request("GET", end_url)


def stats(start_time, mysqlconn):
    stats_url = "http://106.75.239.226:8089/stats/requests"
    response = requests.request("GET", stats_url)

    content = json.loads(response.text)
    median_response_time = content['stats'][0]["median_response_time"]
    min_response_time = content['stats'][0]["min_response_time"]
    current_rps = content['stats'][0]["current_rps"]
    name = content['stats'][0]["name"]
    num_failures = content['stats'][0]["num_failures"]
    max_response_time = content['stats'][0]["max_response_time"]
    avg_response_time = content['stats'][0]["avg_response_time"]
    num_requests = content['stats'][0]["num_requests"]
    user_count = content['user_count']
    used_time = datetime.datetime.now() - start_time

    sql = "insert into locust (time, median_response_time, min_response_time, current_rps, name, num_failures, " \
          "max_response_time, avg_response_time, num_requests, used_time, user_count) value (NOW(), %s, %s, %s, " \
          "\"%s\", %s, %s, %s, %s, %s, %s)" \
          % (median_response_time, min_response_time, current_rps, name, num_failures, max_response_time,
             avg_response_time, num_requests, used_time.seconds, user_count)
    try:
        mysqlconn.insert_data(sql=sql)
    except Exception:
        print("------------------error data start--------------------------")
        print(content)
        print(sql)
        print("------------------error data end--------------------------")


def create_workspace(workspace_base, start_time):
    fold_name = "%s-%s-%s-%s-%s" % (start_time.month, start_time.day, start_time.hour, start_time.minute,
                                    start_time.second)
    fold_path = os.path.join(workspace_base, fold_name)
    os.mkdir(fold_path)
    return fold_path


def donwload_statistics(workspace_path):
    url = "http://106.75.239.226:8089/stats/requests/csv"
    response = requests.request("GET", url)
    with open("%s/statistics_data_%s.csv" % (workspace_path, time.time()), "wb") as code:
        code.write(response.content)


def download_distribution(workspace_path):
    url = "http://106.75.239.226:8089/stats/distribution/csv"
    response = requests.request("GET", url)
    with open("%s/distribution_data_%s.csv" % (workspace_path, time.time()), "wb") as code:
        code.write(response.content)


def download_exceptions(workspace_path):
    url = "http://106.75.239.226:8089/exceptions/csv"
    response = requests.request("GET", url)
    with open("%s/exceptions_data_%s.csv" % (workspace_path, time.time()), "wb") as code:
        code.write(response.content)


def write_time(workspace_path, start_time, end_time):
    content = "start: %s \n end: %s \n used: %s" % (str(start_time), str(end_time), str(end_time - start_time))
    f = open("%s/log.txt" % workspace_path, 'w')
    f.write(content)
    f.close()


if __name__ == '__main__':

    # try:
    #     print("start users 3500")
    #     main(count=1464, hatch_rate=50, users=3500)
    #     time.sleep(60)
    # except:
    #     print("users 3500 error")
    #     time.sleep(60)
    # try:
    #     print("start users 4000")
    #     main(count=1464, hatch_rate=50, users=4000)
    #     time.sleep(60)
    # except:
    #     print("users 4000 error")
    #     time.sleep(60)
    # try:
    #     print("start users 4500")
    #     main(count=1464, hatch_rate=75, users=4500)
    #     time.sleep(60)
    # except:
    #     print("users 4500 error")
    #     time.sleep(60)
    # try:
    #     print("start users 5000")
    #     main(count=1464, hatch_rate=75, users=5000)
    #     time.sleep(60)
    # except:
    #     print("users 5000 error")
    #     time.sleep(60)

    main(count=1460, hatch_rate=50, users=3000)
    time.sleep(60)
    main(count=1460, hatch_rate=50, users=3500)
    time.sleep(60)
    main(count=1460, hatch_rate=50, users=4000)
    time.sleep(60)
    main(count=1460, hatch_rate=50, users=4500)
    time.sleep(60)
    main(count=1460, hatch_rate=50, users=5000)
    time.sleep(60)
    main(count=1460, hatch_rate=50, users=5500)
    time.sleep(60)
    main(count=1460, hatch_rate=50, users=6000)
    time.sleep(60)

    # main(count=740, hatch_rate=50, users=3500)
    # time.sleep(60)
    # main(count=740, hatch_rate=50, users=1500)
    # time.sleep(60)
    # main(count=740, hatch_rate=50, users=2000)
    # time.sleep(60)
    # main(count=740, hatch_rate=50, users=2500)
    # time.sleep(60)
    # main(count=740, hatch_rate=50, users=3000)
    # time.sleep(60)

