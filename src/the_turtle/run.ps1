# Create a new virtual environment
python -m venv venv

# Activate the virtual environment
& venv\Scripts\Activate.ps1

# Install required packages
pip install -r requirements.txt

# Run the Python application
python src/main.py

# Deactivate the virtual environment
# deactivate