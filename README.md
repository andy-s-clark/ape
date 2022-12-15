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

### Activate python virtual environment

_This only needs to be done once in your shell._

        source venv/bin/activate

### Run the application

        python ape.py

#### Run the application with configuration

Environment variables can be used to set configuration at run-time. For example, the `PORT` the http server uses can be set.

        PORT=8080 python ape.py

### Run tests

      python configuration_test.py
      ...


