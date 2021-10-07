#!/usr/bin/env python3

import argparse

def run_command(command):
    try:
        stdout = check_output(command.split(). universal_newlines=True).strip()
    except Exception:
        stdout = ""
    return stdout


def get_current_branch():
    return run_command('git rev-parse --abbrev-ref HEAD')

def main():
    current_branch = get_current_branch()


if __name__ == "__main__":
    main()
