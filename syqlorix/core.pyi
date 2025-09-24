from typing import Any, List, Dict, Tuple, Type, Set
from http.server import BaseHTTPRequestHandler
import re


class Plugin:
    def on_node_init(self, node: "Node") -> None: ...
    def load(self) -> None: ...

plugins: List[Plugin]
class Node:
    _SELF_CLOSING_TAGS: Set[str]
    tag_name: str
    attributes: Dict[str, Any]
    children: List[Any]
    def __init__(self, *children: Any, **attributes: Any) -> None: ...
    def __truediv__(self, other: Any) -> "Node": ...
    def __enter__(self) -> "Node": ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
    def _format_attrs(self) -> str: ...
    def render(self, indent: int = 0, pretty: bool = True) -> str: ...

class Syqlorix(Node):
    _routes: List[Tuple[re.Pattern, Set[str], Any]]
    def route(self, path: str, methods: List[str] = ...) -> Any: ...
    def render(self, pretty: bool = True, live_reload_port: int | None = None, live_reload_host: str | None = None) -> str: ...
    def run(self, file_path: str, host: str = "127.0.0.1", port: int = 8000, live_reload: bool = True, max_port_attempts: int = 10) -> None: ...

class Component(Node): ...
class Comment(Node): ...

class Request:
    method: str
    path_full: str
    path: str
    query_params: Dict[str, Any]
    headers: Dict[str, str]
    path_params: Dict[str, str]
    body: bytes
    form_data: Dict[str, Any]
    json_data: Dict[str, Any] | List[Any]
    def __init__(self, handler: BaseHTTPRequestHandler) -> None: ...

class head(Node): ...
class body(Node): ...
class style(Node):
    def __init__(self, css_content: str, **attributes: Any) -> None: ...

class script(Node):
    def __init__(self, js_content: str = "", src: str | None = None, type: str = "text/javascript", **attributes: Any) -> None: ...

doc: Syqlorix

class NodeWrapper:
    def __init__(self, node: Node, *cl):...

    def __getattr__(self, attr: str) -> "NodeWrapper":...

    def __call__(self, *children, **attrs) -> Node:...

    def __repr__(self) -> str:...

a: NodeWrapper
abbr: NodeWrapper
address: NodeWrapper
article: NodeWrapper
aside: NodeWrapper
audio: NodeWrapper
b: NodeWrapper
bdi: NodeWrapper
bdo: NodeWrapper
blockquote: NodeWrapper
button: NodeWrapper
canvas: NodeWrapper
caption: NodeWrapper
cite: NodeWrapper
code: NodeWrapper
data: NodeWrapper
datalist: NodeWrapper
dd: NodeWrapper
details: NodeWrapper
dfn: NodeWrapper
dialog: NodeWrapper
div: NodeWrapper
dl: NodeWrapper
dt: NodeWrapper
em: NodeWrapper
fieldset: NodeWrapper
figcaption: NodeWrapper
figure: NodeWrapper
footer: NodeWrapper
form: NodeWrapper
h1: NodeWrapper
h2: NodeWrapper
h3: NodeWrapper
h4: NodeWrapper
h5: NodeWrapper
h6: NodeWrapper
header: NodeWrapper
i: NodeWrapper
iframe: NodeWrapper
img: NodeWrapper
input_: NodeWrapper
ins: NodeWrapper
kbd: NodeWrapper
label: NodeWrapper
legend: NodeWrapper
li: NodeWrapper
link: NodeWrapper
main: NodeWrapper
map: NodeWrapper
mark: NodeWrapper
meta: NodeWrapper
meter: NodeWrapper
nav: NodeWrapper
noscript: NodeWrapper
object: NodeWrapper
ol: NodeWrapper
optgroup: NodeWrapper
option: NodeWrapper
output: NodeWrapper
p: NodeWrapper
picture: NodeWrapper
pre: NodeWrapper
progress: NodeWrapper
q: NodeWrapper
rp: NodeWrapper
rt: NodeWrapper
ruby: NodeWrapper
s: NodeWrapper
samp: NodeWrapper
section: NodeWrapper
select: NodeWrapper
small: NodeWrapper
source: NodeWrapper
span: NodeWrapper
strong: NodeWrapper
summary: NodeWrapper
sup: NodeWrapper
table: NodeWrapper
tbody: NodeWrapper
td: NodeWrapper
template: NodeWrapper
textarea: NodeWrapper
tfoot: NodeWrapper
th: NodeWrapper
thead: NodeWrapper
time: NodeWrapper
title: NodeWrapper
tr: NodeWrapper
u: NodeWrapper
ul: NodeWrapper
var: NodeWrapper
video: NodeWrapper
br: NodeWrapper
hr: NodeWrapper
