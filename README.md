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
    $ conda env create -f environment.yaml -n ipyfetch-env
    $ conda activate ipyfetch-env
    $ make develop

When actively developing your extension, build Jupyter Lab with the command:

    make jlab    
    
Actively test on voila:

    make voila
    
After making JavaScript code changes:

    make js
    
    
This takes a minute or so to get started, but then automatically rebuilds JupyterLab when your javascript changes.

Note on first `jupyter lab --watch`, you may need to touch a file to get Jupyter Lab to open.

