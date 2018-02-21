import sys
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
import argparse

def create_sender(dbus_interface_name, object_path):
    class Sender(dbus.service.Object):
        def __init__(self):
            dbus.service.Object.__init__(self, dbus.SessionBus(), object_path)
        @dbus.service.signal(dbus_interface=dbus_interface_name,signature='s')
        def message(self, message):
            pass
     
    return Sender()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='stdin to dbus')
    parser.add_argument('dbus_interface_name', type=str)
    parser.add_argument('object_path', type=str)
    args = parser.parse_args()
        
    arg_dbus_interface_name = args.dbus_interface_name
    arg_object_path = args.object_path

    DBusGMainLoop(set_as_default=True)
      
    sender = create_sender(arg_dbus_interface_name,arg_object_path)
     
    for line in sys.stdin:
        if line == None:
            break
        l = line.rstrip('\n')
        sender.message(l)
