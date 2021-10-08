#!/usr/bin/env python3

import argparse
import sys
import re
from subprocess import check_output


def run_command(command):
    stdout = check_output(command.split(), universal_newlines=True).strip()
    return stdout


def get_current_branch():
    return run_command("git rev-parse --abbrev-ref HEAD")


def find_jira_id(text):
    project_key = r"[A-Z]{2,}"
    issue_id = r"[0-9]+"
    match = re.search(f"{project_key}-{issue_id}", text)
    if match:
        return match.group(0)


def set_jira_ref(issue_id, filename):
    atlassian_url = "https://sureswift.atlassian.net"
    trailer = f"Jira-Ref={atlassian_url}/browse/{issue_id}"
    command = f"git interpret-trailers --trailer {trailer} --in-place {filename}"
    run_command(command)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("commit_msg_filepath")
    args = parser.parse_args()

    commit_msg_filepath = args.commit_msg_filepath
    current_branch = get_current_branch()
    jira_issue_id = find_jira_id(current_branch)

    if not jira_issue_id:
        exit()

    set_jira_ref(jira_issue_id, commit_msg_filepath)


if __name__ == "__main__":
    exit(main())
