from setuptools import setup, find_packages

setup(
    name='test-python-pip',
    version='0.1.0',
    description='Test project for PIP package manager detection',
    author='Test',
    packages=find_packages(),
    install_requires=[
        'Django==2.2.0',
        'requests==2.20.0',
        'urllib3==1.24.1',
        'Jinja2==2.10.0',
        'Flask==1.0.0',
    ],
    python_requires='>=3.6',
)
