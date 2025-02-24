import sys
from _typeshed import SupportsRead
from importlib.abc import Loader, MetaPathFinder, PathEntryFinder
from typing import IO, Any, Callable, Iterable, Iterator, List, NamedTuple, Tuple

class ModuleInfo(NamedTuple):
    module_finder: MetaPathFinder | PathEntryFinder
    name: str
    ispkg: bool

def extend_path(path: List[str], name: str) -> List[str]: ...

class ImpImporter:
    def __init__(self, path: str | None = ...) -> None: ...

class ImpLoader:
    def __init__(self, fullname: str, file: IO[str], filename: str, etc: Tuple[str, str, int]) -> None: ...

def find_loader(fullname: str) -> Loader | None: ...
def get_importer(path_item: str) -> PathEntryFinder | None: ...
def get_loader(module_or_name: str) -> Loader: ...
def iter_importers(fullname: str = ...) -> Iterator[MetaPathFinder | PathEntryFinder]: ...
def iter_modules(path: Iterable[str] | None = ..., prefix: str = ...) -> Iterator[ModuleInfo]: ...
def read_code(stream: SupportsRead[bytes]) -> Any: ...  # undocumented
def walk_packages(
    path: Iterable[str] | None = ..., prefix: str = ..., onerror: Callable[[str], None] | None = ...
) -> Iterator[ModuleInfo]: ...
def get_data(package: str, resource: str) -> bytes | None: ...

if sys.version_info >= (3, 9):
    def resolve_name(name: str) -> Any: ...
