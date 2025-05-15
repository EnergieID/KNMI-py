#!/usr/bin/env bash
rm dist/*
source .venv/bin/activate
python -m build
python -m twine upload dist/*
