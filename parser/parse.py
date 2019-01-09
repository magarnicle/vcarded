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
from pymonad.List import *

def parse_file(file_path):
    """Extracts contact details from a vcard file."""
    lines = _read_file(file_path)
    if lines.getValue() == [] or isinstance(lines, Error):
        return lines
    return (_check_lines * lines).getValue()

def _check_lines(lines):
    if len(lines) == 1:
        return Error(ValueError('Not a vCard file'))
    if lines[0] != 'BEGIN:VCARD':
        return Error(ValueError('First line is not BEGIN:VCARD'))
    if lines[-1] != 'END:VCARD':
        return Error(ValueError('Last line is not BEGIN:VCARD'))
    if lines[1] != 'PRODID:-//Apple Inc.//Mac OS X 10.14.1//EN':
        return Error(ValueError('Unrecognised line %s' % lines[1]))
    return lines

def _read_file(file_path):
    """Read all physical lines of the file and turn them into logical vCard lines."""
    lines = []
    try:
        with open(file_path, 'r') as vcard:
            while True:
                line = vcard.readline()
                if not line:
                    break
                lines.append(line.rstrip('\n'))
    except (TypeError, FileNotFoundError) as Message:
        return Error(Message)
    return Result(lines)

if __name__ == '__main__':
    pass

