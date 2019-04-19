import pymysql


class mysql_handle():

    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1",
                                    port=3306,
                                    user="root",
                                    passwd="123456",
                                    db="grafana")
        self.cur = self.conn.cursor()

    def insert_data(self, sql):
        self.cur.execute(sql)
        self.conn.commit()

    def close_connect(self):
        self.conn.close()

# import datetime
# workspace_path = "/Users/xumin/Desktop/test/10-5-14-50-37"
# start_time = datetime.datetime.now()
# import time
# time.sleep(1)
# end_time = datetime.datetime.now()
# used_time = end_time - start_time
#
# content = "start: %s \n end: %s \n used: %s" % (str(start_time), str(end_time), str(used_time))
# f = open("%s/log.txt" % workspace_path, 'w')
# f.write(content)
# f.close()


# content = b"test"
#
# with open("%s/statistics_data_%s.csv" % (workspace_path, "123"), "wb") as code:
#         code.write(content)