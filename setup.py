from setuptools import setup

REQUIRED = ['humanfriendly', 'redis', 'six', 'tabulate']

setup(name='pyrau',
    version='0.1',
    description='Redis administration utility',
    url='https://github.com/alanc10n/pyrau',
    author='Alan Christianson',
    author_email='git@c10n.net',
    license='MIT',
    packages=['pyrau'],
    entry_points={
        'console_scripts': ['pyrau=pyrau.rau:main'],
    },
    install_requires=REQUIRED
)
