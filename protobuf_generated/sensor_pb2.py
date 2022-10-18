# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensor.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import util_pb2 as util__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sensor.proto',
  package='teamspatzenhirn',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0csensor.proto\x12\x0fteamspatzenhirn\x1a\nutil.proto\"\x94\x02\n\x0cSensorUpdate\x12\x32\n\x0f\x61ngularVelocity\x18\x01 \x01(\x0b\x32\x19.teamspatzenhirn.Vector3D\x12/\n\x0c\x61\x63\x63\x65leration\x18\x02 \x01(\x0b\x32\x19.teamspatzenhirn.Vector3D\x12\x37\n\rsteeringAngle\x18\x03 \x01(\x0b\x32 .teamspatzenhirn.FourWheelDouble\x12\x37\n\rwheelVelocity\x18\x04 \x01(\x0b\x32 .teamspatzenhirn.FourWheelDouble\x12\x1a\n\x12\x66rontLaserDistance\x18\x05 \x01(\x01\x12\x11\n\trearLaser\x18\x06 \x01(\x08\x62\x06proto3'
  ,
  dependencies=[util__pb2.DESCRIPTOR,])




_SENSORUPDATE = _descriptor.Descriptor(
  name='SensorUpdate',
  full_name='teamspatzenhirn.SensorUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='angularVelocity', full_name='teamspatzenhirn.SensorUpdate.angularVelocity', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='acceleration', full_name='teamspatzenhirn.SensorUpdate.acceleration', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='steeringAngle', full_name='teamspatzenhirn.SensorUpdate.steeringAngle', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='wheelVelocity', full_name='teamspatzenhirn.SensorUpdate.wheelVelocity', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frontLaserDistance', full_name='teamspatzenhirn.SensorUpdate.frontLaserDistance', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rearLaser', full_name='teamspatzenhirn.SensorUpdate.rearLaser', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=322,
)

_SENSORUPDATE.fields_by_name['angularVelocity'].message_type = util__pb2._VECTOR3D
_SENSORUPDATE.fields_by_name['acceleration'].message_type = util__pb2._VECTOR3D
_SENSORUPDATE.fields_by_name['steeringAngle'].message_type = util__pb2._FOURWHEELDOUBLE
_SENSORUPDATE.fields_by_name['wheelVelocity'].message_type = util__pb2._FOURWHEELDOUBLE
DESCRIPTOR.message_types_by_name['SensorUpdate'] = _SENSORUPDATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SensorUpdate = _reflection.GeneratedProtocolMessageType('SensorUpdate', (_message.Message,), {
  'DESCRIPTOR' : _SENSORUPDATE,
  '__module__' : 'sensor_pb2'
  # @@protoc_insertion_point(class_scope:teamspatzenhirn.SensorUpdate)
  })
_sym_db.RegisterMessage(SensorUpdate)


# @@protoc_insertion_point(module_scope)