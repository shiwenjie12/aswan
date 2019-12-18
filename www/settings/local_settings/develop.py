# coding=utf8
"""开发环境配置"""

DATABASES = {
    'default': {
        "ENGINE": 'django.db.backends.mysql',
        "HOST": "192.168.100.202",
        "PORT": 3306,
        "USER": "root",
        "PASSWORD": "ChinaDaaS@2017",
        "DATABASE_CHARSET": "utf8",
        "NAME": "risk_control",
    },
}

DEBUG = True
