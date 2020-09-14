import ipywidgets as widgets
from traitlets import Unicode, Dict as DictTrait, Bool
from typing import Callable, Container, Dict


@widgets.register
class Fetch(widgets.DOMWidget):
    """Fetch widget"""

    _view_name = Unicode("FetchView").tag(sync=True)
    _model_name = Unicode("FetchModel").tag(sync=True)
    _view_module = Unicode("ipyfetch").tag(sync=True)
    _model_module = Unicode("ipyfetch").tag(sync=True)
    _view_module_version = Unicode("^0.1.0").tag(sync=True)
    _model_module_version = Unicode("^0.1.0").tag(sync=True)

    url = Unicode("").tag(sync=True)
    value = DictTrait({}).tag(sync=True)
    shared_origin = Bool(False).tag(sync=True)


def create_on_fetch(url: str, container: Dict) -> Callable:
    """
    Return a function to fetch URL.
    On fetch URL, fetch URL directly.
    It returns the result in container with key 'result'
    e.g container['result'] = <JSON_URL_RESPONSE>
    """
    f = Fetch(url=url)

    def on_fetch(change, *args, **kwargs):
        container["result"] = change["new"]

    f.observe(on_fetch, "value")
    return lambda: f
