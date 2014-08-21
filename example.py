#!/usr/bin/env python
# -*- coding: utf-8 -*-
SETTINGS = {
    "default": {
        "BACKEND": "SmsTransportSimple",
        "PARAMS": {
            "a": 1,
            "b": 2,
        }
    },
    "dummy": {
        "BACKEND": "SmsTransportJubber"
    },
    "other": {
        "BACKEND": "SmsTransportGW1",
        "PARAMS": {
            "d": 3,
            "e": 4,
        }
    },
}

from libsms import sms_transport

NAME = "dummy"
PHONE = "123"
MSG = "qwerty"


cfg = SETTINGS[NAME]
"""
С помощью функции sms_transport получаем экзмепляр нужного класса
и вызываем у него метод send
"""
sms_transport(**cfg).send(PHONE, MSG)
