#!/usr/bin/env python
# -*- coding: utf-8 -*-

class SmsTransport(object):
    def __init__(self, params=None):
        self.params = params

    def send(self, phone_number, msg):
        """производит отправку смс"""
        print('Send message "%s" for number %s' % (msg, phone_number))


class SmsTransportSimple(SmsTransport):
    pass


class SmsTransportJubber(SmsTransport):
    pass


class SmsTransportGW1(SmsTransport):
    pass


class SmsTransportGW2(SmsTransport):
    pass

