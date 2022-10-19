#!/usr/bin/env python
import os,sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__))))                     
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(dirnameutils)

from bacpypes.core import run as startBacnetIPApp
from bacpypes.core import stop as stopBacnetIPApp
from bacpypes.basetypes import PropertyIdentifier
from bacpypes.object import get_object_class, get_datatype
from bacpypes.primitivedata import *
from bacpypes.constructeddata import *
from threading import Thread
import configparser

from bacpypes.iocb import IOCB
from bacpypes.apdu import WritePropertyMultipleRequest, \
    WriteAccessSpecification, PropertyValue

from bacpypes.apdu import ReadPropertyMultipleRequest, \
    PropertyReference, PropertyValue, ReadAccessSpecification, \
    ReadPropertyMultipleACK, ReinitializeDeviceRequest, \
    ConfirmedPrivateTransferRequest, ConfirmedPrivateTransferACK

from bacpypes.apdu import SimpleAckPDU, \
    ReadPropertyRequest, ReadPropertyACK, WritePropertyRequest
from bacpypes.pdu import Address
from bacpypes.apdu import AtomicReadFileRequest, \
    AtomicReadFileRequestAccessMethodChoice, \
    AtomicReadFileRequestAccessMethodChoiceStreamAccess, \
    AtomicReadFileACK,\
    AtomicReadFileRequestAccessMethodChoiceRecordAccess, \
    AtomicWriteFileRequest, \
    AtomicWriteFileRequestAccessMethodChoice, \
    AtomicWriteFileRequestAccessMethodChoiceRecordAccess, \
    AtomicWriteFileRequestAccessMethodChoiceStreamAccess, \
    AtomicWriteFileACK
from bacpypes.core import run, enable_sleeping
from bacpypes.apdu import ReadPropertyRequest, ReadPropertyACK
#import ProprietaryObject

from bacpypes.app import BIPSimpleApplication
from bacpypes.local.device import LocalDeviceObject
from bacpypes.core import deferred

from bacpypes.apdu import SubscribeCOVRequest, \
    SimpleAckPDU, RejectPDU, AbortPDU
 
#from bacpypes.primitivedata import Null
#from bacpypes.basetypes import PriorityValue, PriorityArray

from bacpypes.object import get_datatype
from bacpypes.apdu import (
    ReadRangeRequest,
    Range,
    RangeByPosition,
    RangeBySequenceNumber,
    RangeByTime,
    ReadRangeACK,
)
from bacpypes.primitivedata import Date, Time, ObjectIdentifier
from bacpypes.constructeddata import Array, List
from bacpypes.basetypes import DateTime

from Lib_space.BACNET import BacNet

#from BACNET_NEW import BacNet


class Adapter:
    def __init__(self, fileini):
        self.this_application, self.t = BacNet(fileini)

    def set_destination(self, addr):
        self.addr = addr

    def readatomicfile(self, obj_inst, start_record, record_count):
        """readatomicfile <addr> <inst> <start> <count>"""
        try:
            obj_type = 'file'
            obj_inst = int(obj_inst)
            start_position = int(start_record)
            octet_count = int(record_count)

            # build a request
            request = AtomicReadFileRequest(
                fileIdentifier=(obj_type, obj_inst),
                accessMethod=AtomicReadFileRequestAccessMethodChoice(
                    streamAccess=AtomicReadFileRequestAccessMethodChoiceStreamAccess(
                        fileStartPosition=start_position,
                        requestedOctetCount=octet_count,
                    ),
                ),
            )
            request.pduDestination = Address(self.addr)

            # make an IOCB
            iocb = IOCB(request)
            deferred(self.this_application.request_io, iocb)

            # give it to the application
            self.this_application.request_io(iocb)

            # wait for it to complete
            iocb.wait()

            value = None
            # parse response for success
            if iocb.ioResponse:
                apdu = iocb.ioResponse

                # should be an ack
                if not isinstance(apdu, AtomicReadFileACK):
                    return

                # suck out the record data
                if apdu.accessMethod.recordAccess:
                    value = apdu.accessMethod.recordAccess.fileRecordData
                elif apdu.accessMethod.streamAccess:
                    value = apdu.accessMethod.streamAccess.fileData
                                
                return bytes(value)
            # report and exit for error/reject/aborts
            if iocb.ioError:
                print(str(iocb.ioError))

        except Exception as error:
            print("exception: %r", error)

    def writeatomicfile(self,  obj_inst, start_position, data):
        """writeatomicfile <addr> <inst> <start> <data>"""
        try:
            obj_type = 'file'
            obj_inst = int(obj_inst)
            start_position = int(start_position)
            #data = data.encode('utf-8')

            # build a request
            request = AtomicWriteFileRequest(
                fileIdentifier=(obj_type, obj_inst),
                accessMethod=AtomicWriteFileRequestAccessMethodChoice(
                    streamAccess=AtomicWriteFileRequestAccessMethodChoiceStreamAccess(
                        fileStartPosition=start_position,
                        fileData=data,
                        ),
                    ),
                )
            request.pduDestination = Address(self.addr)

            # make an IOCB
            iocb = IOCB(request)

            value = None
            # give it to the application
            self.this_application.request_io(iocb)
            deferred(self.this_application.request_io, iocb)

            # wait for it to complete
            iocb.wait()

            # parse response for success
            if iocb.ioResponse:
                apdu = iocb.ioResponse

                # should be an ack
                if not isinstance(apdu, AtomicWriteFileACK):
                    return

                # suck out the record data
                if apdu.fileStartPosition is not None:
                    value = apdu.fileStartPosition
                elif apdu.fileStartRecord is not None:
                    value = apdu.fileStartRecord

                return repr(value)

            # report and exit for error/reject/abort
            if iocb.ioError:
                print(str(iocb.ioError) + '\n')

        except Exception as error:
            print("exception: %r", error)

    def readproperty(self, obj_type, obj_inst, prop_id, prop_array_index=None):
        """readproperty <addr> <type> <inst> <prop> [ <indx> ]"""
        try:
            if obj_type.isdigit():
                obj_type = int(obj_type)
            elif not get_object_class(obj_type):
                raise ValueError("unknown object type")

            obj_inst = int(obj_inst)

            if prop_id.isdigit():
                prop_id = int(prop_id)

            # build a request
            request = ReadPropertyRequest(
                objectIdentifier=(obj_type, obj_inst),
                propertyIdentifier=prop_id,
            )

            # set destination address
            request.pduDestination = Address(self.addr)

            if prop_array_index is not None:
                request.propertyArrayIndex = int(prop_array_index)

            # make an IOCB
            iocb = IOCB(request)
            deferred(self.this_application.request_io, iocb)

            # give it to the application
            self.this_application.request_io(iocb)

            # wait for it to complete
            iocb.wait()

            # report and exit for error/reject/abort
            if iocb.ioError:
                print(str(iocb.ioError) + '\n')

            # parse response for success
            elif iocb.ioResponse:
                apdu = iocb.ioResponse

                # should be an ack
                if not isinstance(apdu, ReadPropertyACK):
                    return

                # find the datatype
                datatype = get_datatype(apdu.objectIdentifier[0], apdu.propertyIdentifier)
                if not datatype:
                    # peek at the value tag
                    value_tag = apdu.propertyValue.tagList.Peek()
                    # make sure that it is application tagged
                    if value_tag.tagClass != Tag.applicationTagClass:
                        print("value is not application encoded\n")
                    else:
                        # find the datatype
                        datatype = Tag._app_tag_class[value_tag.tagNumber]
                        if not datatype:
                            raise TypeError("unknown datatype")

                        # cast out the value
                        value = apdu.propertyValue.cast_out(datatype)

                        return value

                # special case for array parts, others are managed by cast_out
                if issubclass(datatype, Array) and (apdu.propertyArrayIndex is not None):
                    if apdu.propertyArrayIndex == 0:
                        value = apdu.propertyValue.cast_out(Unsigned)
                    else:
                        value = apdu.propertyValue.cast_out(datatype.subtype)
                else:
                    value = apdu.propertyValue.cast_out(datatype)

                if hasattr(value, 'debug_contents'):
                    value.debug_contents(file=sys.stdout)
                return str(value)

            # exit is no response
            else:
                print('error')

        except Exception as error:
            print("exception: %r", error)

    def writeproperty(self, obj_type, obj_inst, prop_id, value, prop_array_index=None, priority=None):
        """writeproperty <addr> <type> <inst> <prop> <value> [ <indx> ] [ <priority> ]"""
        try:
            if obj_type.isdigit():
                obj_type = int(obj_type)

            obj_inst = int(obj_inst)

            if prop_id.isdigit():
                prop_id = int(prop_id)
            
            # get the propertyArrayIndex if any
            if prop_array_index is not None:
                prop_array_index = int(prop_array_index)
            
            # get the priority if any
            if priority is not None:
                priority = int(priority)

            # get the datatype
            proprietary = False
            datatype = get_datatype(obj_type, prop_id)
            if not datatype:
                proprietary = True
                
            # change atomic values into something encodeable, null is a special case
            if value == 'null':
                value = Null()

            # elif (Proprietary == True) and issubclass(datatype, AnyAtomic):
            elif proprietary:
                dtype, dvalue = value.split(':')

                datatype = {
                    'b': Boolean,
                    'u': lambda x: Unsigned(int(x)),
                    'i': lambda x: Integer(int(x)),
                    'r': lambda x: Real(float(x)),
                    'd': lambda x: Double(float(x)),
                    'o': OctetString,
                    'c': CharacterString,
                    'bs': lambda x: BitString([int(y) for y in x]),
                    #'bs': BitString,
                    'date': Date,
                    'time': Time,
                    'datetime': DateTime,
                    }[dtype]

                value = datatype(dvalue)
                value = Any(value)
                
            elif issubclass(datatype, Atomic):
                if datatype is Integer:
                    value = int(value)
                elif datatype is Real:
                    value = float(value)
                elif datatype is Unsigned:
                    value = int(value)
                    
                value = datatype(value)
                #value = Any(value)
                
            elif issubclass(datatype, Array) and (prop_array_index is not None):
                if prop_array_index == 0:
                    value = Integer(value)
                elif issubclass(datatype.subtype, Atomic):
                    value = datatype.subtype(value)
                elif not isinstance(value, datatype.subtype):
                    raise TypeError("invalid result datatype, expecting %s" % (datatype.subtype.__name__,))
            elif not isinstance(value, datatype):
                raise TypeError("invalid result datatype, expecting %s" % (datatype.__name__,))
            
            #date_value = Date(input("date_value: ")) 
            # build a request
            request = WritePropertyRequest(
                objectIdentifier=(obj_type, obj_inst),
                propertyIdentifier=prop_id
                )
            request.pduDestination = Address(self.addr)

            # save the value
            request.propertyValue = Any()
            try:
                request.propertyValue.cast_in(value)
            except Exception as error:
                print("WriteProperty cast error: %r", error)

            # optional array index
            if prop_array_index is not None:
                request.propertyArrayIndex = prop_array_index

            # optional priority
            if priority is not None:
                request.priority = priority

            # make an IOCB
            iocb = IOCB(request)
            deferred(self.this_application.request_io, iocb)

            # give it to the application
            self.this_application.request_io(iocb)

            # wait for it to complete
            iocb.wait()

            # parse response for success
            if iocb.ioResponse:
                # should be an ack
                if not isinstance(iocb.ioResponse, SimpleAckPDU):
                    return

                return "ack"

            # report and exit for error/reject/abort
            if iocb.ioError:
                print(str(iocb.ioError) + '\n')

        except Exception as error:
            print("exception: %r", error)

    def readmultiple(self, args):
        """read <addr> ( <type> <inst> ( <prop> [ <indx> ] )... )..."""
        try:
            j = 0
            read_access_spec_list = []
            while j < len(args):

                i = 0
                while i < len(args[j]):
                    obj_type = args[j][i]
                    i += 1
                    if type(obj_type) != int:
                        if obj_type.isdigit():
                            obj_type = int(obj_type)
                        elif not get_object_class(obj_type):
                            raise ValueError("unknown object type")

                    obj_inst = int(args[j][i])
                    i += 1

                    prop_reference_list = []
                    prop_id = args[j][i]
                    if prop_id not in PropertyIdentifier.enumerations:
                        if type(prop_id) != int:
                            if prop_id.isdigit():
                                prop_id = int(prop_id)
                        # break

                    i += 1
                    prop_reference = PropertyReference(
                        propertyIdentifier=prop_id,
                        )

                    # check for an array index
                    if (i < len(args[j])) and args[j][i].isdigit():
                        prop_reference.propertyArrayIndex = int(args[j][i])
                        i += 1

                    # add it to the list
                    prop_reference_list.append(prop_reference)

                    # check for at least one property
                    if not prop_reference_list:
                        raise ValueError("provide at least one property")

                # build a read access specification
                read_access_spec = ReadAccessSpecification(
                    objectIdentifier=(obj_type, obj_inst),
                    listOfPropertyReferences=prop_reference_list,
                    )

                # add it to the list
                read_access_spec_list.append(read_access_spec)
                j = j+1

            # check for at least one
            if not read_access_spec_list:
                raise RuntimeError("at least one read access specification required")

            # build the request
            request = ReadPropertyMultipleRequest(
                listOfReadAccessSpecs=read_access_spec_list,
                )
            request.pduDestination = Address(self.addr)

            # make an IOCB
            iocb = IOCB(request)

            # give it to the application
            self.this_application.request_io(iocb)

            # wait for it to complete
            iocb.wait()

            # parse response for success
            if iocb.ioResponse:
                apdu = iocb.ioResponse

                # should be an ack
                if not isinstance(apdu, ReadPropertyMultipleACK):
                    return

                result_list = []
                # loop through the results
                for result in apdu.listOfReadAccessResults:
                    # here is the object identifier
                    objectIdentifier = result.objectIdentifier

                    # now come the property values per object
                    for element in result.listOfResults:
                        # get the property and array index
                        propertyIdentifier = element.propertyIdentifier
                        propertyArrayIndex = element.propertyArrayIndex

                        # here is the read result
                        readResult = element.readResult

                        print(propertyIdentifier)
                        if propertyArrayIndex is not None:
                            print("[" + str(propertyArrayIndex) + "]")

                        # check for an error
                        if readResult.propertyAccessError is not None:
                            print (" ! " + str(readResult.propertyAccessError) + '\n')
                            print ("Error Class:", readResult.propertyAccessError.errorClass)
                            print ("Error Code:", readResult.propertyAccessError.errorCode)

                        else:
                            # here is the value
                            propertyValue = readResult.propertyValue

                            # find the datatype
                            datatype = get_datatype(objectIdentifier[0], propertyIdentifier)
                            if not datatype:
                                # peek at the value tag
                                value_tag = propertyValue.tagList.Peek()
                                # make sure that it is application tagged
                                if value_tag.tagClass != Tag.applicationTagClass:
                                    print("value is not application encoded\n")
                                else:
                                    # find the datatype
                                    datatype = Tag._app_tag_class[value_tag.tagNumber]
                                    if not datatype:
                                        raise TypeError("unknown datatype")

                                    # cast out the value
                                    value = propertyValue.cast_out(datatype)

                            # special case for array parts, others are managed by cast_out
                            if issubclass(datatype, Array) and (propertyArrayIndex is not None):
                                if propertyArrayIndex == 0:
                                    value = propertyValue.cast_out(Unsigned)
                                else:
                                    value = propertyValue.cast_out(datatype.subtype)
                                # result_list.append(value)
                            else:
                                value = propertyValue.cast_out(datatype)
                                # return value
                    result_list.append(value)
                            # print(" = " + str(value) + '\n')
                    sys.stdout.flush()
                return result_list
            # report and exit for error/reject/abort
            if iocb.ioError:
                print(str(iocb.ioError) + '\n')

        except Exception as error:
            print("exception: %r", error)        

    def writemultiple(self, args):
        """write <addr> <type> <inst> <prop> <value> [ <indx> ] [ <priority> ]"""
        # args = args.split()

        try:
            # addr = args[i]
            # i += 1

            write_access_spec_list = []
            write_values_list = []
            j = 0
            while j < len(args):
                i = 0
                while i < len(args[j]):
                    obj_type = args[j][i]
                    i += 1
                    if type(obj_type) is not int:
                        if obj_type.isdigit():
                            obj_type = int(obj_type)
                        # elif not get_object_class(obj_type):
                        #     raise ValueError("unknown object type")

                    obj_inst = int(args[j][i])
                    i += 1

                    prop_value_list = []

                    # while i < len(args):
                    prop_id = args[j][i]
                    # if prop_id not in PropertyIdentifier.enumerations:
                    if type(prop_id) is not int:
                        if prop_id.isdigit():
                            prop_id = int(prop_id)

                    i += 1
                    # get the property value from args
                    value = args[j][i]

                    # get the datatype
                    Proprietary = False
                    datatype = get_datatype(obj_type, args[j][i-1])
                    # increment for the next property
                    i += 1
                    if not datatype:
                        Proprietary = True

                    # change atomic values into something encodeable, null is a special case
                    if value == 'null':
                        value = Null()
          #          elif issubclass(datatype, AnyAtomic):
                    elif (Proprietary == True):
                        dtype, dvalue = value.split(':')

                        datatype = {
                            'b': Boolean,
                            'u': lambda x: Unsigned(int(x)),
                            'i': lambda x: Integer(int(x)),
                            'r': lambda x: Real(float(x)),
                            'd': lambda x: Double(float(x)),
                            'o': OctetString,
                            'c': CharacterString,
                            'bs': BitString,
                            'date': Date,
                            'time': Time,
                        }[dtype]

                        value = datatype(dvalue)
                        value = Any(value)

                    elif issubclass(datatype, Atomic):
                        if datatype is Integer:
                            value = int(value)
                        elif datatype is Real:
                            value = float(value)
                        elif datatype is Unsigned:
                            value = int(value)

                        value = datatype(value)
                        value = Any(value)

                    elif not isinstance(value, datatype):
                        raise TypeError("invalid result datatype, expecting %s" % (datatype.__name__,))

                    # build a property reference
                    prop_value = PropertyValue(propertyIdentifier=prop_id, value=value, priority=1)

                    # add it to the list
                    prop_value_list.append(prop_value)

                    # check for an array index
                    if (i < len(args[j])) and args[j][i].isdigit():
                        prop_value.propertyArrayIndex = int(args[j][i])
                        i = i+1

                    # optional priority
                    if (i < len(args[j])):
                        prop_value.priority = int(args[j][i])
                        i = i+1

                    # check for at least one property
                    if not prop_value_list:
                        raise ValueError("provide at least one property")

                    # build a read access specification
                    write_access_spec = WriteAccessSpecification(
                        objectIdentifier=(obj_type, obj_inst),
                        listOfProperties=prop_value_list,
                        )

                    # add it to the list
                    write_access_spec_list.append(write_access_spec)

                    # add values to list
                    write_values_list.append(value)
                j = j+1
            # check for at least one
            if not write_access_spec_list:
                raise RuntimeError("at least one read access specification required")

            # build the request
            request = WritePropertyMultipleRequest(
                listOfWriteAccessSpecs=write_access_spec_list,
                )
            request.pduDestination = Address(self.addr)

            # save the value
            request.propertyValue = Any()

            # make an IOCB
            iocb = IOCB(request)
            deferred(self.this_application.request_io, iocb)

            # give it to the application
            self.this_application.request_io(iocb)

            # wait for it to complete
            iocb.wait()

            # do something for success
            if iocb.ioResponse:
                apdu = iocb.ioResponse

                # should be an ack
                if not isinstance(apdu, SimpleAckPDU):
                    return

                return 'ack'

            # do something for error/reject/abort
            if iocb.ioError:
                print(str(iocb.ioError) + '\n')

        except Exception as error:
            print("exception: %r", error)
    
    def ReinitializeRequest(self, state, pwd):
        # args = args.split()
        # state, pwd = args
        state = str(state)
        pwd = str(pwd)

        try:
        # build a request
          request = ReinitializeDeviceRequest(
            reinitializedStateOfDevice = state,
            password = pwd
          )
        
          request.pduDestination = Address(self.addr)

        # make an IOCB
          iocb = IOCB(request)
          deferred(self.this_application.request_io, iocb)

        # give it to the application
          self.this_application.request_io(iocb)

        # wait for it to complete
          iocb.wait()
    
        # parse response for success
          if iocb.ioResponse:
              apdu = iocb.ioResponse

            # should be an ack
              if not isinstance(apdu, SimpleAckPDU):
                    return

              return 'ack'

          # report and exit for error/reject/abort
          if iocb.ioError:
                print(str(iocb.ioError) + '\n')

        except Exception as error:
            print("exception: %r", error)


    def CPTRequest(self, vendorid, srvnum, srvparam):
        # args = args.split()
        # vendorid, srvnum, srvparam = args
        vendorid = int(vendorid)
        srvnum = int(srvnum)
        srvparam = str(srvparam).split(",")

        try:
        # build a request
          request = ConfirmedPrivateTransferRequest(
            vendorID = vendorid,
            serviceNumber = srvnum,
          )
        
          request.pduDestination = Address(self.addr)
          request.serviceParameters = Any()
          for parameter in srvparam:
              dtype, dvalue = parameter.split(':')
              datatype = {
                    'b': Boolean,
                    'u': lambda x: Unsigned(int(x)),
                    'i': lambda x: Integer(int(x)),
                    'r': lambda x: Real(float(x)),
                    'd': lambda x: Double(float(x)),
                    'o': OctetString,
                    'c': CharacterString,
                    'bs': BitString,
                    'date': Date,
                    'time': Time,
                    }[dtype]

              srvparam = datatype(dvalue)
              try:
                request.serviceParameters.cast_in(srvparam)
              except Exception as error:
                print("WriteProperty cast error: %r", error)
        # make an IOCB
          iocb = IOCB(request)
          deferred(self.this_application.request_io, iocb)

        # give it to the application
          self.this_application.request_io(iocb)

        # wait for it to complete
          iocb.wait()
    
        # parse response for success
          if iocb.ioResponse:
              apdu = iocb.ioResponse

            # should be an ack
              if not isinstance(apdu, ConfirmedPrivateTransferACK):
                    return
              print (apdu.resultBlock.cast_out(Unsigned))
              return 'ack'

          # report and exit for error/reject/abort
          if iocb.ioError:
                print(str(iocb.ioError) + '\n')

        except Exception as error:
            print("exception: %r", error)

    def read_datatype_property(self, obj_type, obj_inst, prop_id, prop_array_index=None):
        """readproperty <addr> <type> <inst> <prop> [ <indx> ]"""        
        try:
            if obj_type.isdigit():
                obj_type = int(obj_type)
            elif not get_object_class(obj_type):
                raise ValueError("unknown object type")

            obj_inst = int(obj_inst)

            if prop_id.isdigit():
                prop_id = int(prop_id)

            # build a request
            request = ReadPropertyRequest(
                objectIdentifier=(obj_type, obj_inst),
                propertyIdentifier=prop_id,
            )
            # set destination address
            request.pduDestination = Address(self.addr)

            if prop_array_index is not None:
                request.propertyArrayIndex = int(prop_array_index)

            # make an IOCB
            iocb = IOCB(request)
            deferred(self.this_application.request_io, iocb)

            # give it to the application
            self.this_application.request_io(iocb)

            # wait for it to complete
            iocb.wait()

            # report and exit for error/reject/abort
            if iocb.ioError:
                print(str(iocb.ioError) + '\n')

            # parse response for success
            elif iocb.ioResponse:
                apdu = iocb.ioResponse
                # should be an ack
                if not isinstance(apdu, ReadPropertyACK):
                    return

                # find the datatype
                datatype = get_datatype(apdu.objectIdentifier[0], apdu.propertyIdentifier)
            # exit is no response
            else:
                print('error')
            datatype = get_datatype(apdu.objectIdentifier[0], apdu.propertyIdentifier)    
            return datatype.__name__
        
        except Exception as error:
            print("exception: %r", error)

    def SubscribeCOV(self,obj_type, obj_inst, prop_id,confirmed,lifetime):

        obj_type = obj_type
        obj_inst = obj_inst
        proc_id = prop_id
        issueConfirmedNotifications = confirmed
        lifetime = lifetime
        
        try:
        # build a request
            request = SubscribeCOVRequest(
                subscriberProcessIdentifier=proc_id,
                monitoredObjectIdentifier=(int(obj_type), int(obj_inst)),
                )
            request.pduDestination = Address(self.addr)
        # optional parameters
            if issueConfirmedNotifications is not None:
                request.issueConfirmedNotifications = issueConfirmedNotifications
            if lifetime is not None:
                request.lifetime = lifetime        
            
            # make an IOCB
            iocb = IOCB(request)
            deferred(self.this_application.request_io, iocb)

            # give it to the application
            self.this_application.request_io(iocb)

        # wait for it to complete
            iocb.wait()
    
        # parse response for success
            if iocb.ioResponse:
              apdu = iocb.ioResponse

            # should be an ack
              if not isinstance(apdu, SimpleAckPDU):
                    return

              return 'ack'

          # report and exit for error/reject/abort
            if iocb.ioError:
                print(str(iocb.ioError) + '\n')

                    
        except Exception as error:
            print("exception: %r", error)

    def Readrange(self, obj_type, obj_inst, prop_id,prop_array_index,range=None):
    #def Readrange(self, obj_type, obj_inst, prop_id,prop_array_index):
        #Readrange 10.16.0.104 trendLog 1 logBuffer        
        """readrange <addr> <objid> <prop> [ <indx> ]
            [ p <indx> <count> ]
            [ s <seq> <count> ]
            [ t <date> <time> <count> ]"""        
        try:
            if obj_type.isdigit():
                obj_type = int(obj_type)

            obj_inst = int(obj_inst)

            if prop_id.isdigit():
                prop_id = int(prop_id)
 
            obj_id = ObjectIdentifier(obj_type,obj_inst).value
            
            datatype = get_datatype(obj_id[0], prop_id)
            if not datatype:
                raise ValueError("invalid property for object type")                      

            # build a request            
            request = ReadRangeRequest(
                objectIdentifier=(obj_type, obj_inst),
                propertyIdentifier=prop_id
                )
            
            request.pduDestination = Address(self.addr)
            # index is optional
            if obj_type.isdigit():
                    if not issubclass(datatype, Array):
                        raise ValueError("property is not an array")
                    request.propertyArrayIndex = obj_type
                    datatype = datatype.subtype
            if not issubclass(datatype, List):
                raise ValueError("property is not a list")
            
            # range is optional
            range_type = range
            #print(range_type)
            if range_type != None :                
                if range[0] == "p":
                    rbp = RangeByPosition(
                        referenceIndex=range[1], count=int(range[2])
                        )
                    request.range = Range(byPosition=rbp)
                elif range[0] == "s":
                    rbs = RangeBySequenceNumber(
                        referenceSequenceNumber=int(range[1]), count=int(range[2])
                        )
                    request.range = Range(bySequenceNumber=rbs)
                elif range[0] == "t":
                    #print(range[1])
                    rbt = RangeByTime(
                        referenceTime=DateTime(
                            date=Date(range[1]).value, time=Time(range[2]).value
                            ),
                        count=int(range[3]),
                        )
                    request.range = Range(byTime=rbt)
                elif range_type == "x":
            # should be missing required parameter
                    request.range = Range()
            else:
                pass
                #raise ValueError("unknown range type: %r" % (range_type,))
                #print("unknown range type: %r" % (range_type,))
            
            # make an IOCB
            iocb = IOCB(request)
            # give it to the application
            deferred(self.this_application.request_io, iocb)

            # wait for it to complete
            iocb.wait()

            # do something for success
         # report and exit for error/reject/abort
            if iocb.ioError:
                print(str(iocb.ioError) + '\n')
                            
            elif iocb.ioResponse:
                apdu = iocb.ioResponse

                # should be an ack
                if not isinstance(apdu, ReadRangeACK):
                    return
                                
                # find the datatype
                datatype = get_datatype(
                    apdu.objectIdentifier[0], apdu.propertyIdentifier
                )
                if not datatype:
                    raise TypeError("unknown datatype")

                #print(
                #    "firstSequenceNumber: %s\n" % (apdu.firstSequenceNumber,)
                #)
                print("resultFlags: %s\n" % (apdu.resultFlags,))

                # cast out the data into a list
                value = apdu.itemData[0].cast_out(datatype)                
                print (value)
                # dump it out
                '''
                if hasattr(value, 'debug_contents'):
                    value.debug_contents(file=sys.stdout)
                return value.debug_contents()           
                
                #temp_file = dirnameutils+"\\Logs\\_trendLog_file.txt"
                for i, item in enumerate(value):
                    print("[%d]\n" % (i,))
                    item.debug_contents(file=sys.stdout, indent=2)
                    #str= str+item.debug_contents(file=sys.stdout, indent=2)
                    #print(str)
                #return str
                '''
                return value
                
#            request.propertyArrayIndex = int(prop_array_index)
            # give it to the application
            #self.this_application.request(request)
            
        except Exception as error:
            print("exception: %r", error)
        
        
        
    def disconnect(self):
        try:
            self.this_application.mux.directPort.handle_close()
        except:
            self.this_application.mux.broadcastPort.handle_close()
        stopBacnetIPApp()
    
        self.t.join()

