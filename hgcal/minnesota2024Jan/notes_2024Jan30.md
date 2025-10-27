
# python virtual environment in aidan's directory:
python venv setup:

python -m venv --system-site-packages ~/pyenv/tilebd

source ~/pyenv/tilebd/bin/active

# installed packages in virtual environment:

needed for billy's script:
pip install nested_dict

needed for uhal_backend_v3.py:
pip install tabulate

needed for guiPEconD_backend_v3.py
pip install tk
but gui still doesn't work, need to install tkinter software

for econ:
pip install bitstruct

for econ in econd-sw repo:
pip install -r requirements.txt
(but was not successful)

