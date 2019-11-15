#
#
#

import sys
import bluetooth
import msvcrt
import pythoncom

from PySide2.QtCore import QThread
from PySide2.QtCore import Signal
from PySide2.QtCore import Slot

import excel

UUID_RFCOMM = '00000003-0000-1000-8000-00805F9B34FB'
UUID_SPP = '00001101-0000-1000-8000-00805F9B34FB'
BT_ADDR = '98:D3:91:FD:50:03'

#================================
#
#
class BtRxThread(QThread):

    rx_signal = Signal(int, int)

    def __init__(self, sock):
        super(BtRxThread, self).__init__()
        self.sock = sock
        self.rotation = 0
        self.dir = 0
        self.s = 0
        self.r = 0
        self.d = 0
        return

    def run(self):
        pythoncom.CoInitialize()
        x = excel.Excel()
        x.connect()

        #---- rx loop ----
        while True:
            rx = self.sock.recv(1024)

            x.write((4,4,4,4)) #---- test ----
            self.rx_signal.emit(self.rotation, self.dir) #---- test ----

            if  rx:
                rd = rx.decode()
                #print(rd, end = '', flush = True)
                for i in range(len(rd)):
                    self.state_machine(rd[i])
        return

    def state_machine(self, d):
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
            #print('R: %d' % (self.rotation))
            return

        if  self.s == 8:
            self.dir = self.d
            #print('D: %d' % (self.dir))
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
        return

    def connect_rx(self, handler):
        self.thread.rx_signal.connect(handler)
        return

    def connect_excel(self, app):
        self.excel = app
        self.excel.hi()
        return

    def inquiry(self):
        print('inquery')
        devices = bluetooth.discover_devices(duration = 8, lookup_names = True, flush_cache = True, lookup_class = False)
        print('found %d devices' % (len(devices)))
        n = 1
        for addr, name in devices:
            try:
                print('%d: %s - %s' % (n, addr, name))
            except UnicodeEncodeError:
                print('%d: %s - %s' % (n, addr, name.encode('utf-8', 'replace')))
            n += 1
        print('select device to connect > ', end = '', flush = True)
        k = msvcrt.getch()
        print(k.decode())
        n = int(k.decode())
        self.addr = devices[n - 1][0]
        #print('connect to %s ...' % (self.addr))
        self.spp_client()
        return

    def sdp(self, target):
        print('sdp')
        if  target == 'all':
            target = None
        services = bluetooth.find_service(address = target)
        if  len(services) > 0:
            print('found %d services on %s' % (len(services), target))
        else:
            print('no services found')
        for svc in services:
            print('service name: %s' % (svc['name']))
            print('host: %s' % (svc['host']))
            print('description: %s' % (svc['description']))
            print('provider: %s' % (svc['provider']))
            print('protocol: %s' % (svc['protocol']))
            print('channel/psm: %s' % (svc['port'])) # psm - protocol and service multiplexer
            print('profiles: %s' % (svc['profiles']))
            print('service classes: %s' % (svc['service-classes']))
            print('service id: %s' % (svc['service-id']))
        return

    def spp_client(self):
        print('spp client')
        print('searching for spp server on %s' % (self.addr))
        uuid = UUID_SPP
        services = bluetooth.find_service(uuid = uuid, address = self.addr)
        if  len(services) == 0:
            print('could not find the spp server service')
            sys.exit(0)

        svc = services[0]
        port = svc['port']
        name = svc['name']
        host = svc['host']
        print('connecting to %s on %s' % (name, host))
        self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.sock.connect((host, port))
        print('connected')

        #---- thread ----
        self.thread = BtRxThread(self.sock)
        self.thread.start(QThread.IdlePriority)
        return

#
# eof
#