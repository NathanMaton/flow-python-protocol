# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flow/entities/block_header.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='flow/entities/block_header.proto',
  package='flow.entities',
  syntax='proto3',
  serialized_options=_b('Z\010entities'),
  serialized_pb=_b('\n flow/entities/block_header.proto\x12\rflow.entities\x1a\x1fgoogle/protobuf/timestamp.proto\"k\n\x0b\x42lockHeader\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x11\n\tparent_id\x18\x02 \x01(\x0c\x12\x0e\n\x06height\x18\x03 \x01(\x04\x12-\n\ttimestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\nZ\x08\x65ntitiesb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_BLOCKHEADER = _descriptor.Descriptor(
  name='BlockHeader',
  full_name='flow.entities.BlockHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='flow.entities.BlockHeader.id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent_id', full_name='flow.entities.BlockHeader.parent_id', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='flow.entities.BlockHeader.height', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='flow.entities.BlockHeader.timestamp', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=84,
  serialized_end=191,
)

_BLOCKHEADER.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['BlockHeader'] = _BLOCKHEADER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BlockHeader = _reflection.GeneratedProtocolMessageType('BlockHeader', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKHEADER,
  '__module__' : 'flow.entities.block_header_pb2'
  # @@protoc_insertion_point(class_scope:flow.entities.BlockHeader)
  })
_sym_db.RegisterMessage(BlockHeader)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
