ipyfetch
===============================

ipywidget to fetch URL

Installation
------------

To install use pip:

    $ pip install ipyfetch
    $ jupyter nbextension enable --py --sys-prefix ipyfetch

To install for jupyterlab

    $ jupyter labextension install ipyfetch

For a development installation (requires npm),

    $ git clone https://github.com//ipyfetch.git
    $ cd ipyfetch
    $ pip install -e .
    $ jupyter nbextension install --py --symlink --sys-prefix ipyfetch
    $ jupyter nbextension enable --py --sys-prefix ipyfetch
    $ jupyter labextension install js

When actively developing your extension, build Jupyter Lab with the command:

    $ jupyter lab --watch
    
    
After making JavaScript code changes:

    cd js
    npm run build
    
This takes a minute or so to get started, but then automatically rebuilds JupyterLab when your javascript changes.

Note on first `jupyter lab --watch`, you may need to touch a file to get Jupyter Lab to open.

