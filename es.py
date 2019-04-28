import requests

url = "http://192.168.0.105:9200/gateway_runtime_journal_project_2"

payload = "{\n    \"aliases\": {},\n    \"mappings\": {\n        \"doc\": {\n            \"properties\": {\n                \"destination_address\": {\n                    \"type\": \"text\",\n                    \"fields\": {\n                        \"keyword\": {\n                            \"type\": \"keyword\",\n                            \"ignore_above\": 256\n                        }\n                    }\n                },\n                \"duration\": {\n                    \"type\": \"long\"\n                },\n                \"headers\": {\n                    \"type\": \"object\"\n                },\n                \"id\": {\n                    \"type\": \"text\",\n                    \"fields\": {\n                        \"keyword\": {\n                            \"type\": \"keyword\",\n                            \"ignore_above\": 256\n                        }\n                    }\n                },\n                \"is_succeed\": {\n                    \"type\": \"boolean\"\n                },\n                \"params\": {\n                    \"type\": \"object\"\n                },\n                \"remote_ip\": {\n                    \"type\": \"text\",\n                    \"fields\": {\n                        \"keyword\": {\n                            \"type\": \"keyword\"\n                        }\n                    }\n                },\n                \"request_path\": {\n                    \"type\": \"text\",\n                    \"fields\": {\n                        \"keyword\": {\n                            \"type\": \"keyword\",\n                            \"ignore_above\": 256\n                        }\n                    }\n                },\n                \"request_pattern\": {\n                    \"type\": \"text\",\n                    \"fields\": {\n                        \"keyword\": {\n                            \"type\": \"keyword\",\n                            \"ignore_above\": 256\n                        }\n                    }\n                },\n                \"request_time\": {\n                    \"type\": \"date\",\n                    \"format\": \"date_time || date_time_no_millis || yyyy-MM-dd'T'HH:mmZZ\"\n                },\n                \"response_time\": {\n                    \"type\": \"date\",\n                    \"format\": \"date_time || date_time_no_millis || yyyy-MM-dd'T'HH:mmZZ\"\n                },\n                \"status_code\": {\n                    \"type\": \"long\"\n                },\n                \"response_headers\": {\n                    \"type\": \"object\"\n                }\n            }\n        }\n    }\n}\n"
payload = {
    "mappings": {
        "doc": {
            "properties": {
                "destination_address": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "duration": {
                    "type": "long"
                },
                "headers": {
                    "type": "object"
                },
                "id": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "is_succeed": {
                    "type": "boolean"
                },
                "params": {
                    "type": "object"
                },
                "remote_ip": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword"
                        }
                    }
                },
                "request_path": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "request_pattern": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "request_time": {
                    "type": "date",
                    "format": "date_time || date_time_no_millis || yyyy-MM-dd'T'HH:mmZZ"
                },
                "response_time": {
                    "type": "date",
                    "format": "date_time || date_time_no_millis || yyyy-MM-dd'T'HH:mmZZ"
                },
                "status_code": {
                    "type": "long"
                },
                "response_headers": {
                    "type": "object"
                }
            }
        }
    }
}
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "3c01f642-525e-13e0-d974-419a183df83e"
    }


requests.request("DELETE", url)
response = requests.request("PUT", url, json=payload, headers=headers)

print(response.text)