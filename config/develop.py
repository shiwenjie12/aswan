# coding=utf8

#  存储各项配置信息的redis
REDIS_CONFIG = {
    "host": "192.168.100.202",
    "port": 6379,
    "db": 4,
    "password": "",
    "max_connections": 40,
    "socket_timeout": 1,
    "decode_responses": True
}

#  作为命中日志队列的redis
LOG_REDIS_CONFIG = {
    "host": "192.168.100.202",
    "port": 6379,
    "db": 4,
    "password": "",
    "max_connections": 40,
    "socket_timeout": 1,
    "decode_responses": True
}

#  存储上报数据的redis
REPORT_REDIS_CONFIG = {
    "host": "192.168.100.202",
    "port": 6379,
    "db": 4,
    "password": "",
    "max_connections": 40,
    "socket_timeout": 1,
    "decode_responses": True
}

# 存储命中日志的mysql
LOG_MYSQL_CONFIG = {
    'host': '192.168.100.202',
    'port': 3306,
    'user': 'root',
    'passwd': 'ChinaDaaS@2017',
    'charset': 'utf8',
    'db': 'risk_control',
}

# 存储权限等信息的mongo
SOC_MONGO_HOST = [
    "192.168.100.44:27017",
]


MONGO_DB = "risk_control"
