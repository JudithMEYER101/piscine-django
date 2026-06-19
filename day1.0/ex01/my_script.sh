#!/bin/sh

python3 -m pip --version  #Check pip version

rm -rf local_lib          #Remove local_lib/ if existing
rm -f install.log         #Remove intall.log if existing

#Install the Path library localy in local_lib/
python3 -m pip install --upgrade --force-reinstall \
    --target local_lib \
    git+https://github.com/jaraco/path.git \
    > install.log 2>&1

if [ $? -eq 0 ]; then #if previous command worked then
    PYTHONPATH=local_lib python3 my_program.py
else
    echo "Installation failed. Check install.log"
fi