from locust import HttpLocust, TaskSet, task, between
import json


class WebsitTasks(TaskSet):
    @task
    # 实际测试服务发现
    # def s1_500ms1k(self):
    #     with self.client.get("/2x/200ms", catch_response=True) as response:
    #         if response.status_code == 200:
    #             pass
    #         else:
    #             pass
    #             response.failure(response)
    @task
    # 测试新网关
    def s1_500ms1k(self):

        # "/test/50/0"
        headers = {
            "Content-Type": "application/json",
            "DMP-Project": "2",
            "X-DMP-MARS": "3327c2a3-7eb7-47c9-9870-4fecb9389ad6"

        }
        payload = {
            "configText": "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:cus=\"http://siebel.com/CustomUI\">\n   <soapenv:Header/>\n   <soapenv:Body>\n      <cus:ASWPOSInboundLoyaltyMember_Input>\n         <cus:CardNumber>${posCardNum}</cus:CardNumber>\n         <cus:MessageXML><![CDATA[<?xml version=\"1.0\"?>\n<PrivateData>\n  <LoyaltyMessageNumber1>\n    <Customer MsgType=\"1\" StoreID=\"829\" PosID=\"1\" TransID=\"5\" BusinessDate=\"2020/01/02\">\n      <LoyaltyInfo CardID=\"${posCardNum}\" CardType=\"P\" />\n    </Customer>\n  </LoyaltyMessageNumber1>\n</PrivateData>]]></cus:MessageXML>\n         <cus:BUID>9999000499</cus:BUID>\n         <cus:MessageType>0100</cus:MessageType>\n      </cus:ASWPOSInboundLoyaltyMember_Input>\n   </soapenv:Body>\n</soapenv:Envelope>\n1",
            "format": "xml", "namespaceId": 5747}
        with self.client.put("/2x/post", headers=headers, json=payload, catch_response=True) as response:
            if response.status_code == 200:
                pass
            else:
                pass
                response.failure(response)


class WebsiteUser(HttpLocust):
    task_set = WebsitTasks
    host = "http://172.16.111.181:38953"
    wait_time = between(0, 0)
