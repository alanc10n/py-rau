# pyrau
Python Redis Admin Utility

This is a simple utility to aid in manual redis administration tasks such as removing keys matching a given pattern.
This is very much a work in progress, so expect more commands to appear as I attempt to scratch itches or think of 
useful features. At the moment, it only supports deleting keys matching a given pattern and listing keys.

## Usage

Install the dependencies (optionally in a virtual environment) with `pip install -r requirements.txt`. Then run 
`python rau.py -h` to see options.

### Examples

To delete all keys starting with 'foo' from a local redis instance: `python rau.py delete 'foo*'`.

To list all keys with details: `python rau.py keys -d`.
