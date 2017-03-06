BIP39 seed generator
====================

This is a simple BIP39 seed generator for an ESP8266 running the MicroPython
firmware. To use it, install Adafruit's ampy:

~~~
pip install adafruit-ampy
~~~

Connect an OLED screen to the ESP8266 (I used one of those small 128x64 ones) to
pins 2 (SCL) and 4 (SDA). Copy things to the ESP (you may need to specify your
USB port to ampy):

~~~
ampy put english.txt
ampy put ssd1306.mpy
ampy put main.py
~~~

Now disconnect your NodeMCU/WeMos/whatever from power and reconnect it (or just
reset it), and it will start showing a 24-word BIP39 seed on its screen. Write
it down, and you're all set, no computers needed or anything (well, almost).

Voilà!
