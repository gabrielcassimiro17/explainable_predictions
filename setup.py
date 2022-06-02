from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

setup(name='explainable_predictions',
      version="0.1",
      description="Package used to create predictions with explainability and confidence intervals",
      packages=find_packages(),
      install_requires=requirements,
      test_suite='tests',
      include_package_data=True,
      zip_safe=False)