iexviz
==============================
This is demo of working with IEX message data. Most of the documenation and narrative is in the notebook/iex_viz directory.

This is a notebook to show how to work with IEX historic [TOP and DEEPs](https://iextrading.com/trading/alerts/2017/014/) data. The data downloads compresed as a large (3-4GB) pcap file, which a raw TCPIP format. This format is basically a stream of tcp messages, where IP headers have to be parsed from each message. 

- First you need to parse the IEX pcap file.
  - if using python:, try IEX_hist_parser from [IEXTools](https://github.com/vfrazao-ns1/IEXTools)
  - if using java: try [IEX Trading 4j-Hist](https://github.com/WojciechZankowski/iextrading4j-hist)
  - I recommend and will show using go. Secifically using the ``pcap2json`` and ``pcap2csv`` parsers from the [go IEX project](https://github.com/timpalpant/go-iex)

- Pandas has issues reading the json, so I then used spark and python's json2parquet to convert json to parquet. Spark worked great on the TOPS.json, but required a debug config I didn't feel like fixing. So I resorted to python's json2parquet, which worked surprisingly well.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
