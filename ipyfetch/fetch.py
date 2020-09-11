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

    @classmethod
    def create(cls, url, container):
        f = cls(url=url)

        def on_fetch(change, *args, **kwargs):
            container['result'] = change['new']

        f.observe(on_fetch, "value")
        return f
