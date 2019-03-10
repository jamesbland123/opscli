from setuptools import setup
setup(
    name = 'opscli',
    version = '0.1.0',
    packages = ['opscli'],
    entry_points = {
        'console_scripts': [
            'opscli = opscli.__main__:main'
        ]
    })