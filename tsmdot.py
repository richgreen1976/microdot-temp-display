#!/usr/bin/env python
import urllib2,json
import sys
import time
from microdotphat import clear, show, write_string, scroll, set_decimal

READ_API_KEY='HSYK0UT7YHMUPP35'
CHANNEL_ID='256881'

def main():
    conn = urllib2.urlopen("https://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                           % (CHANNEL_ID,READ_API_KEY))
    response = conn.read()
    print "http status code=%s" % (conn.getcode())

    while  conn.getcode() != 200:
        conn = urllib2.urlopen("https://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                               % (CHANNEL_ID,READ_API_KEY))
        response = conn.read()
        set_decimal(0, 1)
        set_decimal(1, 1)
        set_decimal(2, 1)
        set_decimal(3, 1)
        set_decimal(4, 1)
        set_decimal(5, 1)
        show()
        print "http status code=%s" % (conn.getcode())
        
    set_decimal(0, 0)
    set_decimal(1, 0)
    set_decimal(2, 0)
    set_decimal(3, 0)
    set_decimal(4, 0)
    set_decimal(5, 0)
    show()
    
    data=json.loads(response)
    print data['field1'],data['field2'],data['field3'],data['created_at']
    outtemp = data['field1']
    temp = float(outtemp)
    tempstring = str(round(temp,1))

    print("""Displays the current outdoor temperature.
    Press Ctrl+C to exit.
    """)
    conn.close()

    write_string(" " + tempstring + "C", kerning=False)

    set_decimal(0, 1)
    set_decimal(1, 1)
    show()
    time.sleep(1)
    clear()
x = 0

    while x < 30:
        write_string(" " + tempstring + "C", kerning=False)
        set_decimal(0, 1)
        show()
        time.sleep(1)
        write_string(" " + tempstring + "C", kerning=False)
        set_decimal(0, 0)
        show()
        time.sleep(1)
        clear()
        
        x = x+1

while True:
        try:
           main()
        except KeyboardInterrupt:
                clear()
                sys.exit(-1)
