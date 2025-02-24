import sys
from datetime import datetime as _datetime
from email._header_value_parser import (
    AddressList,
    ContentDisposition,
    ContentTransferEncoding,
    ContentType,
    MIMEVersion,
    TokenList,
    UnstructuredTokenList,
)
from email.errors import MessageDefect
from email.policy import Policy
from typing import Any, Dict, Iterable, Mapping, Tuple, Type

class BaseHeader(str):
    @property
    def name(self) -> str: ...
    @property
    def defects(self) -> Tuple[MessageDefect, ...]: ...
    @property
    def max_count(self) -> int | None: ...
    def __new__(cls, name: str, value: Any) -> BaseHeader: ...
    def init(self, name: str, *, parse_tree: TokenList, defects: Iterable[MessageDefect]) -> None: ...
    def fold(self, *, policy: Policy) -> str: ...

class UnstructuredHeader:
    @staticmethod
    def value_parser(value: str) -> UnstructuredTokenList: ...
    @classmethod
    def parse(cls, value: str, kwds: Dict[str, Any]) -> None: ...

class UniqueUnstructuredHeader(UnstructuredHeader): ...

class DateHeader:
    @property
    def datetime(self) -> _datetime: ...
    @staticmethod
    def value_parser(value: str) -> UnstructuredTokenList: ...
    @classmethod
    def parse(cls, value: str | _datetime, kwds: Dict[str, Any]) -> None: ...

class UniqueDateHeader(DateHeader): ...

class AddressHeader:
    @property
    def groups(self) -> Tuple[Group, ...]: ...
    @property
    def addresses(self) -> Tuple[Address, ...]: ...
    @staticmethod
    def value_parser(value: str) -> AddressList: ...
    @classmethod
    def parse(cls, value: str, kwds: Dict[str, Any]) -> None: ...

class UniqueAddressHeader(AddressHeader): ...

class SingleAddressHeader(AddressHeader):
    @property
    def address(self) -> Address: ...

class UniqueSingleAddressHeader(SingleAddressHeader): ...

class MIMEVersionHeader:
    @property
    def version(self) -> str | None: ...
    @property
    def major(self) -> int | None: ...
    @property
    def minor(self) -> int | None: ...
    @staticmethod
    def value_parser(value: str) -> MIMEVersion: ...
    @classmethod
    def parse(cls, value: str, kwds: Dict[str, Any]) -> None: ...

class ParameterizedMIMEHeader:
    @property
    def params(self) -> Mapping[str, Any]: ...
    @classmethod
    def parse(cls, value: str, kwds: Dict[str, Any]) -> None: ...

class ContentTypeHeader(ParameterizedMIMEHeader):
    @property
    def content_type(self) -> str: ...
    @property
    def maintype(self) -> str: ...
    @property
    def subtype(self) -> str: ...
    @staticmethod
    def value_parser(value: str) -> ContentType: ...

class ContentDispositionHeader(ParameterizedMIMEHeader):
    @property
    def content_disposition(self) -> str: ...
    @staticmethod
    def value_parser(value: str) -> ContentDisposition: ...

class ContentTransferEncodingHeader:
    @property
    def cte(self) -> str: ...
    @classmethod
    def parse(cls, value: str, kwds: Dict[str, Any]) -> None: ...
    @staticmethod
    def value_parser(value: str) -> ContentTransferEncoding: ...

if sys.version_info >= (3, 8):
    from email._header_value_parser import MessageID
    class MessageIDHeader:
        @classmethod
        def parse(cls, value: str, kwds: Dict[str, Any]) -> None: ...
        @staticmethod
        def value_parser(value: str) -> MessageID: ...

class HeaderRegistry:
    def __init__(
        self, base_class: Type[BaseHeader] = ..., default_class: Type[BaseHeader] = ..., use_default_map: bool = ...
    ) -> None: ...
    def map_to_type(self, name: str, cls: Type[BaseHeader]) -> None: ...
    def __getitem__(self, name: str) -> Type[BaseHeader]: ...
    def __call__(self, name: str, value: Any) -> BaseHeader: ...

class Address:
    @property
    def display_name(self) -> str: ...
    @property
    def username(self) -> str: ...
    @property
    def domain(self) -> str: ...
    @property
    def addr_spec(self) -> str: ...
    def __init__(
        self, display_name: str = ..., username: str | None = ..., domain: str | None = ..., addr_spec: str | None = ...
    ) -> None: ...
    def __str__(self) -> str: ...

class Group:
    @property
    def display_name(self) -> str | None: ...
    @property
    def addresses(self) -> Tuple[Address, ...]: ...
    def __init__(self, display_name: str | None = ..., addresses: Iterable[Address] | None = ...) -> None: ...
    def __str__(self) -> str: ...
