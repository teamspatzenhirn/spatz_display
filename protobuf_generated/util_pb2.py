# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: util.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='util.proto',
  package='teamspatzenhirn',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nutil.proto\x12\x0fteamspatzenhirn\"+\n\x08Vector3D\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\"]\n\x0f\x46ourWheelDouble\x12\x11\n\tfrontLeft\x18\x01 \x01(\x01\x12\x12\n\nfrontRight\x18\x02 \x01(\x01\x12\x10\n\x08rearLeft\x18\x03 \x01(\x01\x12\x11\n\trearRight\x18\x04 \x01(\x01\x62\x06proto3'
)




_VECTOR3D = _descriptor.Descriptor(
  name='Vector3D',
  full_name='teamspatzenhirn.Vector3D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='teamspatzenhirn.Vector3D.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='teamspatzenhirn.Vector3D.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z', full_name='teamspatzenhirn.Vector3D.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=31,
  serialized_end=74,
)


_FOURWHEELDOUBLE = _descriptor.Descriptor(
  name='FourWheelDouble',
  full_name='teamspatzenhirn.FourWheelDouble',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='frontLeft', full_name='teamspatzenhirn.FourWheelDouble.frontLeft', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frontRight', full_name='teamspatzenhirn.FourWheelDouble.frontRight', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rearLeft', full_name='teamspatzenhirn.FourWheelDouble.rearLeft', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rearRight', full_name='teamspatzenhirn.FourWheelDouble.rearRight', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=76,
  serialized_end=169,
)

DESCRIPTOR.message_types_by_name['Vector3D'] = _VECTOR3D
DESCRIPTOR.message_types_by_name['FourWheelDouble'] = _FOURWHEELDOUBLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Vector3D = _reflection.GeneratedProtocolMessageType('Vector3D', (_message.Message,), {
  'DESCRIPTOR' : _VECTOR3D,
  '__module__' : 'util_pb2'
  # @@protoc_insertion_point(class_scope:teamspatzenhirn.Vector3D)
  })
_sym_db.RegisterMessage(Vector3D)

FourWheelDouble = _reflection.GeneratedProtocolMessageType('FourWheelDouble', (_message.Message,), {
  'DESCRIPTOR' : _FOURWHEELDOUBLE,
  '__module__' : 'util_pb2'
  # @@protoc_insertion_point(class_scope:teamspatzenhirn.FourWheelDouble)
  })
_sym_db.RegisterMessage(FourWheelDouble)


# @@protoc_insertion_point(module_scope)
