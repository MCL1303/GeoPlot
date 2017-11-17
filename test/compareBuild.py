#! /usr/bin/env python3

import subprocess
import os
import os.path
from glob import iglob, glob


def main():
    program_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(program_dir)

    for i in iglob(os.path.join('data', 'facts', '*.xml')):
        subprocess.check_call([os.path.join('..', 'model', 'build.bat'), i])

    try:
        subprocess.check_call([
            "git", "diff",
            "--no-patch", "--exit-code",
            "../model/models"
        ])
    except subprocess.CalledProcessError as err:
        if err.returncode != 1:
            raise
        subprocess.call(['git', 'checkout', 'data/facts/'])
        exit(1)

if __name__ == '__main__':
    main()
