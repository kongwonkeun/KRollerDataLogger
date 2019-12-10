#
#
#

import sys
import bluetooth
import win32file, pywintypes
import msvcrt
import threading
from datetime import datetime

from PySide2.QtCore import QThread
from PySide2.QtCore import Signal
from PySide2.QtCore import Slot

import zExcel

UUID_RFCOMM = '00000003-0000-1000-8000-00805F9B34FB'
UUID_SPP = '00001101-0000-1000-8000-00805F9B34FB'

BT_NAME = "HC-05"

G_connected = False
G_found = False

#================================
#
#
class BtRxThread(QThread):

    rx_signal = Signal(int, int)

    def __init__(self, sock):
        super(BtRxThread, self).__init__()
        self.sock = sock
        self.rotation = 0
        self.speed = 100
        self.dir = 10
        self.s = 0
        self.r = 0
        self.v = 0
        self.d = 0
        self.f = True
        return

    def stop(self):
        self.f = False
        return

    #============================
    #
    #
    def run(self):

        #---- rx loop ----
        while (self.f):
            rx = self.sock.recv(1024)
            #---- test ----
            #self.rx_signal.emit(self.rotation, self.dir)
            #----
            if  rx:
                rd = rx.decode() # rd is str
                print(rd, end='', flush=True)
                for i in range(len(rd)):
                    self.state_machine_1(rd[i])

        self.close()
        return

    def state_machine_1(self, d):
        b = ord(d)
        if   b == 86: self.s = 1; self.v = 0 # 86 = 'V' of 'Vnnnnn'
        elif b == 68: self.s = 7; self.d = 0 # 68 = 'D' of 'Dnnn'
        else:
            if    self.s == 1: self.s = 2;  self.v = (b - 48)
            elif  self.s == 2: self.s = 3;  self.v = (self.v * 10) + (b - 48)
            elif  self.s == 3: self.s = 4;  self.v = (self.v * 10) + (b - 48)
            elif  self.s == 4: self.s = 5;  self.v = (self.v * 10) + (b - 48)
            elif  self.s == 5: self.s = 6;  self.v = (self.v * 10) + (b - 48)
            elif  self.s == 7: self.s = 8;  self.d = (b - 48)
            elif  self.s == 8: self.s = 9;  self.d = (self.d * 10) + (b - 48)
            elif  self.s == 9: self.s = 10; self.d = (self.d * 10) + (b - 48)
            else: pass

        if  self.s == 6:
            self.speed = self.v
            #print(f"R:{self.speed}")
            return
        if  self.s == 10:
            self.dir = self.d
            #print(f"D:{self.dir}")
        return
    
    def state_machine_2(self, d):
        b = ord(d)
        if   b == 82: self.s = 1; self.r = 0 # 82 = 'R' of 'Rnnn'
        elif b == 68: self.s = 5; self.d = 0 # 68 = 'D' of 'Dnnn'
        else:
            if    self.s == 1: self.s = 2; self.r = (b - 48)
            elif  self.s == 2: self.s = 3; self.r = (self.r * 10) + (b - 48)
            elif  self.s == 3: self.s = 4; self.r = (self.r * 10) + (b - 48)
            elif  self.s == 5: self.s = 6; self.d = (b - 48)
            elif  self.s == 6: self.s = 7; self.d = (self.d * 10) + (b - 48)
            elif  self.s == 7: self.s = 8; self.d = (self.d * 10) + (b - 48)
            else: pass

        if  self.s == 4:
            self.rotation = self.r
            #print(f"R:{self.rotation}")
            return
        if  self.s == 8:
            self.dir = self.d
            #print(f"D:{self.dir}")
        return

#================================
#
#
class Bt(object):

    def __init__(self):
        self.sock = None
        self.s = 0
        self.r = 0
        self.d = 0
        self.max = 0
        self.min = 40
        self.width = 0
        self.distance_sum = 0
        self.distance_sum_meter = 0;
        self.sec_sum = 0
        return

    def stop(self):
        print("BT: stop rx thread")
        self.thread.stop()
        return

    def connect_rx(self, handler):
        self.thread.rx_signal.connect(handler)
        return

    def connect_excel(self, app):
        self.excel = app
        self.excel.write_header()
        return

    def tick(self):
        now = datetime.now()
        self.excel.write((now.day, now.hour, now.minute, now.second, self.thread.speed, self.thread.dir))
        self.max = max(self.max, self.thread.dir)
        self.min = min(self.min, self.thread.dir)
        self.width = self.max - self.min
        self.distance_sum += self.thread.speed
        self.distance_sum_meter = self.distance_sum / 100
        self.sec_sum += 1
        self.excel.write_summery((self.max, self.min, self.width, self.distance_sum_meter, self.sec_sum))
        return

    #============================
    #
    #
    def connect(self):

        global G_found
        print("BT: start inquery")
        devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)
        print(f"BT: found {len(devices)} neighbor devices")

        n = 1
        for addr, name in devices:
            try:
                print(f"{n}: {addr} - {name}")
            except UnicodeEncodeError:
                print(f"{n}: {addr} + {name.encode('utf-8', 'replace')}")
            n += 1

        #---- kong ---- for manual connection
        #print("select device to connect > ", end='', flush=True)
        #c = msvcrt.getch()
        #print(c.decode())
        #n = int(c.decode())
        #----

        n = 1
        for addr, name in devices:
            if  name == BT_NAME:
                break
            n += 1
            if  n > len(devices):
                G_found = False
                return

        print("BT: found kroller device")
        G_found = True
        self.addr = devices[n-1][0]
        self.name = devices[n-1][0]
        print(f"BT: try to connect ({self.name}, {self.addr}) ...")
        self.spp_client()
        return

    #============================
    #
    #
    def sdp(self, target):

        print("BT: sdp begin")
        
        if  target == 'all':
            target = None
        services = bluetooth.find_service(address=target)

        if  len(services) > 0:
            print("BT: found %d services on %s" % (len(services), target))
        else:
            print("BT: no services found")

        for s in services:
            print("service name: %s" % (s['name']))
            print("host: %s" % (s['host']))
            print("description: %s" % (s['description']))
            print("provider: %s" % (s['provider']))
            print("protocol: %s" % (s['protocol']))
            print("channel/psm: %s" % (s['port'])) # psm - protocol and service multiplexer
            print("profiles: %s" % (s['profiles']))
            print("service classes: %s" % (s['service-classes']))
            print("service id: %s" % (s['service-id']))

        print("BT: sdp end")
        return

    #============================
    #
    #
    def spp_client(self):

        global G_connected
        print("BT: start spp client")
        print(f"BT: search for spp server on {self.addr}")

        uuid = UUID_SPP
        services = bluetooth.find_service(uuid=uuid, address=self.addr)
        if  len(services) == 0:
            print("BT: could not find spp server")
            G_connected = False
            return

        s = services[0]
        port = s['port']
        name = s['name']
        host = s['host']
        print(f"BT: connecting to {name} on {host}")

        self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.sock.connect((host, port))
        print("BT: connected")

        #---- thread ----
        self.thread = BtRxThread(self.sock)
        self.thread.start(QThread.IdlePriority)
        return

#
# eof
#