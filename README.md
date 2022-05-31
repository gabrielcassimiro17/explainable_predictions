# Explainable Predictions
Package used to create predictions with explainability and confidence intervals

![check](https://github.com/gabrielcassimiro17/explainable-predictions/actions/workflows/explainable-predictions.yml/badge.svg)

# Startup the project

The initial setup.


# Install

Go to `https://github.com/{group}/explainable-predictions` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/explainable-predictions.git
cd explainable-predictions
pip install -r requirements.txt
make clean install test                # install and test
```

Unittest test:
```bash
make clean install test
```
