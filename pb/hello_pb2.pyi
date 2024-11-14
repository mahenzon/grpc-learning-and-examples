from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Hello(_message.Message):
    __slots__ = ("text", "kind")
    class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CORPO: _ClassVar[Hello.Kind]
        STREET: _ClassVar[Hello.Kind]
        THIRD: _ClassVar[Hello.Kind]
    CORPO: Hello.Kind
    STREET: Hello.Kind
    THIRD: Hello.Kind
    TEXT_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    text: str
    kind: Hello.Kind
    def __init__(self, text: _Optional[str] = ..., kind: _Optional[_Union[Hello.Kind, str]] = ...) -> None: ...
