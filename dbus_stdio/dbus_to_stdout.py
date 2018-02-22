import sys
import dbus
from dbus.mainloop.glib import DBusGMainLoop
import gi.repository.GLib
import argparse

def signal_handler(message):
    try:
        print(message)
        sys.stdout.flush()
    except:
        loop.quit()

loop = None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='stdin to dbus')
    parser.add_argument('dbus_interface_name', type=str)
    args = parser.parse_args()

    arg_dbus_interface_name = args.dbus_interface_name

    DBusGMainLoop(set_as_default=True)
    
    bus = dbus.SessionBus()
    bus.add_signal_receiver(signal_handler,dbus_interface=arg_dbus_interface_name)

    loop = gi.repository.GLib.MainLoop()
    loop.run()
