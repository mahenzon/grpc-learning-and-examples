# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: hello.proto
# Protobuf Python Version: 5.28.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    3,
    '',
    'hello.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bhello.proto\x12\x05hello\"n\n\x05Hello\x12\x0c\n\x04text\x18\x01 \x01(\t\x12$\n\x04kind\x18\x02 \x01(\x0e\x32\x11.hello.Hello.KindH\x00\x88\x01\x01\"(\n\x04Kind\x12\t\n\x05\x43ORPO\x10\x00\x12\n\n\x06STREET\x10\x01\x12\t\n\x05THIRD\x10\x02\x42\x07\n\x05_kindb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hello_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_HELLO']._serialized_start=22
  _globals['_HELLO']._serialized_end=132
  _globals['_HELLO_KIND']._serialized_start=83
  _globals['_HELLO_KIND']._serialized_end=123
# @@protoc_insertion_point(module_scope)