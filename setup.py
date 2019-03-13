from setuptools import setup, find_namespace_packages
setup(
    name = 'opscli',
    version = '0.1.0',
    packages = find_namespace_packages(),
    entry_points = {
        'console_scripts': [
            'opscli = opscli.__main__:main'
        ]
    })
