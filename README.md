INSTALL
-------

```
    python setup.py install
````

UNINSTALL
---------

```
    python setup.py install --record files.txt
    cat files.txt | xargs rm -rf
```

<br>
<br>
Both operations can require root privilege
<br>

USAGE
---------

```py
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

NAME = "dummy"<br>
PHONE = "123"<br>
MSG = "qwerty"<br>


cfg = SETTINGS[NAME]
sms_transport(**cfg).send(PHONE, MSG)
```
<br>
here it returns 
```'Send message "qwerty" for number 123'```
