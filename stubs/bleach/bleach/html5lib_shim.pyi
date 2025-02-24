from typing import Any, Generator, Iterable, List, Text

class HTMLParser(object):  # actually html5lib.HTMLParser
    def __getattr__(self, __name: Text) -> Any: ...  # incomplete

class Filter(object):  # actually html5lib.filters.base.Filter
    def __getattr__(self, __name: Text) -> Any: ...  # incomplete

class SanitizerFilter(object):  # actually html5lib.filters.sanitizer.Filter
    def __getattr__(self, __name: Text) -> Any: ...  # incomplete

class HTMLSerializer(object):  # actually html5lib.serializer.HTMLSerializer
    def __getattr__(self, __name: Text) -> Any: ...  # incomplete

class BleachHTMLParser(HTMLParser):
    tags: List[Text] | None
    strip: bool
    consume_entities: bool
    def __init__(self, tags: Iterable[Text] | None, strip: bool, consume_entities: bool, **kwargs) -> None: ...

class BleachHTMLSerializer(HTMLSerializer):
    escape_rcdata: bool
    def escape_base_amp(self, stoken: Text) -> Generator[Text, None, None]: ...
    def serialize(self, treewalker, encoding: Text | None = ...) -> Generator[Text, None, None]: ...

def __getattr__(__name: Text) -> Any: ...  # incomplete
