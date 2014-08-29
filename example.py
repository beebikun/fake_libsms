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

import libsms

NAME = "dummy"
PHONE = "123"
MSG = "qwerty"


cfg = SETTINGS[NAME]

class SmsTransportFactory(object):
    """Фабрика для SmsTransport"""
    def __init__(self):
        pass

    def get_transport(self, transport_name):
        """Возвращает нужный класс"""
        return getattr(libsms, transport_name)


def sms_transport(BACKEND, PARAMS=None):
    """Возвращает экземпляр нужного класса"""
    transport = SmsTransportFactory().get_transport(BACKEND)
    return transport(PARAMS)


"""
С помощью функции sms_transport получаем экзмепляр нужного класса
и вызываем у него метод send
"""
sms_transport(**cfg).send(PHONE, MSG)
