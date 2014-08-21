INSTALL
-------

<code>
    python setup.py install
</code>

UNINSTALL
---------

<code>
    python setup.py install --record files.txt
    cat files.txt | xargs rm -rf
</code>

<br>
<br>
Both operations can require root privilege
<br>

USAGE
---------

<code>
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
sms_transport(**cfg).send(PHONE, MSG)
#here it returns "Send message "qwerty" for number 123"
</code>
