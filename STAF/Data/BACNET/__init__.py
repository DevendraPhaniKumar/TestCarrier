from bacpypes.app import BIPSimpleApplication
from bacpypes.local.device import LocalDeviceObject
from threading import Thread
from bacpypes.core import run as startBacnetIPApp
import configparser
#import ConfigParser as configparser


class BacNet(object):
    def __init__(self):
        print("Initialising BacNet")

    def __new__(cls, *args):
        fileini = configparser.ConfigParser()
        #fileini = ConfigParser.ConfigParser()
        fileini.read(args)
        this_device = LocalDeviceObject(
            objectName=fileini.get('BACpypes', 'objectName'),
            objectIdentifier=int(fileini.get('BACpypes', 'objectidentifier')),
            maxApduLengthAccepted=int(fileini.get('BACpypes', 'maxapdulengthaccepted')),
            segmentationSupported=fileini.get('BACpypes', 'segmentationsupported'),
            vendorIdentifier=int(fileini.get('BACpypes', 'vendoridentifier')),
        )
        this_application = BIPSimpleApplication(this_device, fileini.get('BACpypes', 'address'))

        t = Thread(target=startBacnetIPApp, kwargs={
            'sigterm': None, 'sigusr1': None})
        t.start()
        print('BACNet - Connected')

        return this_application, t