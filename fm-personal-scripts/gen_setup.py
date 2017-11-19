#!/usr/bin/env python
"""'Generate a setup.py file

Usage:
  gen_setup.py NAME

Arguments:
  NAME      Name of the python module
"""
from contextlib import redirect_stdout
from pathlib import Path

from docopt import docopt


def _template()-> Path:
    """Get the path to the setup.py template"""
    this_file = Path(__file__)
    script_dir = this_file.parent
    module_name = this_file.with_suffix('').name
    template = script_dir / 'resources' / module_name / 'template.py'
    return template


def gen_setup(name: str, template: Path = _template())-> None:
    """Generate a setup.py file

    Parameters
    ----------
    name
        Name of the module
    template
        Template setup.py file

    Raises
    ------
    FileExistsError
        If setup.py already exists
    """
    output_path = Path('setup.py')

    if output_path.exists():
        raise FileExistsError

    with template.open('r') as inp:
        with output_path.open('w') as out:
            with redirect_stdout(out):
                for line in inp:
                    first_word = line.partition(' ')[0]
                    if first_word == 'NAME':
                        print(''.join(["NAME = '", name, "'"]))
                    else:
                        print(line.rstrip())


if __name__ == '__main__':
    args = docopt(__doc__)
    name = args['NAME']
    gen_setup(name)