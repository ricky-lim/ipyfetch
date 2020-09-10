import ipywidgets as widgets
from traitlets import Unicode, Dict, Bool


@widgets.register
class Fetch(widgets.DOMWidget):
    """Fetch widget"""

    _view_name = Unicode('FetchView').tag(sync=True)
    _model_name = Unicode('FetchModel').tag(sync=True)
    _view_module = Unicode('ipyfetch').tag(sync=True)
    _model_module = Unicode('ipyfetch').tag(sync=True)
    _view_module_version = Unicode('^0.1.0').tag(sync=True)
    _model_module_version = Unicode('^0.1.0').tag(sync=True)

    url = Unicode('').tag(sync=True)
    value = Dict({}).tag(sync=True)
    shared_origin = Bool(False).tag(sync=True)
