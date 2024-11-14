import hello_pb2 as _hello_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HelloRequest(_message.Message):
    __slots__ = ("hello",)
    HELLO_FIELD_NUMBER: _ClassVar[int]
    hello: _hello_pb2.Hello
    def __init__(self, hello: _Optional[_Union[_hello_pb2.Hello, _Mapping]] = ...) -> None: ...

class MultiHelloResponse(_message.Message):
    __slots__ = ("title", "greetings")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    GREETINGS_FIELD_NUMBER: _ClassVar[int]
    title: str
    greetings: _containers.RepeatedCompositeFieldContainer[_hello_pb2.Hello]
    def __init__(self, title: _Optional[str] = ..., greetings: _Optional[_Iterable[_Union[_hello_pb2.Hello, _Mapping]]] = ...) -> None: ...
