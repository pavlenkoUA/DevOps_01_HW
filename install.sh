#!/bin/bash

venv_name="myenv"

echo "Creating virtual environment..."
python3 -m venv "$venv_name"
sleep 5
# Step 2: Activate the virtual environment
if [ "$VIRTUAL_ENV" != "$PWD/$venv_name" ]; then
    echo "Activating virtual environment..."
    source "$venv_name/bin/activate"
else
    echo "Virtual environment already activated."
fi

echo "Installing requirements..."
python3 -m pip install -r requirements.txt

python3 -m pylint password_generator_oop.py
python3 password_generator_oop_test.py
deactivate