# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: users-response.proto
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
    'users-response.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import user_pb2 as user__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14users-response.proto\x12\rusersResponse\x1a\nuser.proto\"=\n\x0cResponseMeta\x12\x0c\n\x04page\x18\x01 \x02(\x05\x12\r\n\x05total\x18\x02 \x02(\x05\x12\x10\n\x08pageSize\x18\x03 \x02(\x05\"U\n\rUsersResponse\x12)\n\x04meta\x18\x01 \x02(\x0b\x32\x1b.usersResponse.ResponseMeta\x12\x19\n\x05users\x18\x02 \x03(\x0b\x32\n.user.User')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'users_response_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_RESPONSEMETA']._serialized_start=51
  _globals['_RESPONSEMETA']._serialized_end=112
  _globals['_USERSRESPONSE']._serialized_start=114
  _globals['_USERSRESPONSE']._serialized_end=199
# @@protoc_insertion_point(module_scope)