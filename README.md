# APE

API Prometheus Exporter. Periodically query an API, cache the results, and present the results as prometheus metrics.

## Set up local development environment

1. Install Python 3.10 and virtualenv.
2. Change to the directory of your local clone of this repository.

        cd ~/work/ape
3. Create python virtual environment.

        python3 -m venv venv
4. Activate python virtual environment.

        source venv/bin/activate
5. Install required packages.

        pip install -r requirements.txt

## Run locally

1. Activate python virtual environment. Only needs to be done once in your shell.

        source venv/bin/activate

2. Run the application.

        python ape.py

3. View the API in a web browser at http://127.0.0.1:8000 .
