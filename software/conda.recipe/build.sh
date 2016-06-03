#!/bin/bash

$PYTHON setup.py install
$PYTHON setup.py --version > __conda_version__.txt
