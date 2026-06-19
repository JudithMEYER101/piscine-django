#!/bin/sh

python3 -m venv django_venv

if [ $? -ne 0 ]; then
    echo "Error: virtualenv creation failed."
    exit 1
fi

. django_venv/bin/activate

pip install -r requirement.txt

if [ $? -ne 0 ]; then
    echo "Error: installation failed."
    exit 1
fi

exec "$SHELL"