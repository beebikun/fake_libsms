#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

import libsms

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




SETTINGS = {
    "dummy": {"BACKEND": "SmsTransportJubber"},
}


class TestDateConversion(unittest.TestCase):
    phone = "123"
    msg = "qwerty"
    cfg = {"BACKEND": "SmsTransportJubber"}

    def testDummy(self):
        answer = 'Send message "%s" for number %s' % (self.msg, self.phone)
        transport_answer = sms_transport(**self.cfg).send(self.phone, self.msg)
        self.assertEqual(transport_answer, answer)
