#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from libsms import sms_transport

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
