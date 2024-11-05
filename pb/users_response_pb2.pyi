from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

from . import user_pb2 as _user_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ResponseMeta(_message.Message):
    __slots__ = ("page", "total", "pageSize")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    PAGESIZE_FIELD_NUMBER: _ClassVar[int]
    page: int
    total: int
    pageSize: int
    def __init__(self, page: _Optional[int] = ..., total: _Optional[int] = ..., pageSize: _Optional[int] = ...) -> None: ...

class UsersResponse(_message.Message):
    __slots__ = ("meta", "users")
    META_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    meta: ResponseMeta
    users: _containers.RepeatedCompositeFieldContainer[_user_pb2.User]
    def __init__(self, meta: _Optional[_Union[ResponseMeta, _Mapping]] = ..., users: _Optional[_Iterable[_Union[_user_pb2.User, _Mapping]]] = ...) -> None: ...
