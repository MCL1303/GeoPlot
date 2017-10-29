#! /usr/bin/env python3

from glob import iglob
import sys
import subprocess
import os
import os.path


def main():
    program_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(program_dir)

    subprocess.check_call(
        os.path.join('..', 'extract', 'extract *'),
        stderr=subprocess.DEVNULL,
        shell=True
    )

    try:
        subprocess.check_call(["git", "diff", "--no-patch", "--exit-code", "data/facts"])
    except subprocess.CalledProcessError:
        subprocess.call(['git', 'checkout', 'data/facts/'])
        exit(1)

if __name__ == '__main__':
    main()
