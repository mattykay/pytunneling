#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Usage:
    pytunneling.py [(-v | --verbose)] [<args> ...]
    pytunneling.py (-h | --help)
    pytunneling.py --version

Arguments:
  args          what arguments to pass to API call

Options:
  -h, --help
  --version
  -v, --verbose                      Whether to use verbose logging [default: False]
"""
from docopt import docopt
from os import path
import pytunneling

import logging.config
logger = logging.getLogger(__name__)


def main():
    arguments = docopt(__doc__, version=pytunneling.__version__)

    # Setup logging
    logging.config.fileConfig(path.join(path.dirname(path.abspath(__file__)),
                                        'logging.ini'),
                              disable_existing_loggers=False)
    if arguments['--verbose']:
        logging.getLogger().setLevel(logging.DEBUG)

    raise NotImplementedError(
        "Calling module from command line is not yet supported")


if __name__ == '__main__':
    main()
