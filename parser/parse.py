"""
http://blog.ploeh.dk/2015/04/13/less-is-more-language-features/
No:
    1. GOTO - duh
    2. Exceptions - 'railway-oriented programming', use Maybe/Either or even Harrow
    3. Pointers - duh
    4. Different number types - use float
    5. Null pointers - use Maybe/Either
    6. Mutation - always return new copies of objects
    7. Reference equality - use structural equality instead (==)
    8. Inheritance - use composition instead
    9. Interfaces - don't really exist in python
    10. Reflection - not sure what it is
    11. Cyclic dependencies - dunno
"""
import docopt
from pymonad.Either import *


def parse_file(file_path):
    """Extracts contact details from a vcard file."""
    try:
        with open(file_path, 'rb') as vcard:
            line = vcard.readline()
            if not line:
                return Result([])
            if line != 'BEGIN:VCARD':
                raise ValueError('not a Vcard file')
    except Exception as Message:
        return Error(Message)
    return Result([])

if __name__ == '__main__':
    pass
