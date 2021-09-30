# python-utils

This is where I keep python scripts I write to automate tasks on my computer.

## Directory Organizer

This simple script handles some basic tasks for making messy directory structures more organized. Right now its primary function is to group directories by common prefixes.
For example, if you have many folders with names like "foo - x", "foo - y", etc, it will turn that into one folder called "foo" with child folders "x", "y", etc.

Example usage: `python directory_organizer.py ~/Documents/foo --delimiter "__" -f`

See `directory_organizer.py --help` for options.