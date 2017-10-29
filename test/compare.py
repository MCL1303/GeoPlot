#! /usr/bin/env python3

from glob import iglob
import sys
import subprocess
import os
import os.path


def main():
    program_dir = os.path.dirname(os.path.realpath(__file__))
    files = ' '.join(
        i for i in iglob(os.path.join(program_dir, 'data', 'facts', '*'))
        if os.path.splitext(i)[-1] == '.xml'
    )

    subprocess.check_call([
        os.path.join(program_dir, '..', 'extract', 'extract'),
        files, '2>',
        ('nul' if sys.platform.startswith('win') else '/dev/null')
    ])

    try:
        subprocess.check_call(["git", "diff", "--no-path", "--exit-code", files]):
    except subprocess.CalledProcessError:
        os.chdir(program_dir)
        subprocess.call(['git', 'checkout', 'data/facts/'])
        exit(1)

if __name__ == '__main__':
    main()
