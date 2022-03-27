#!/usr/bin/env python3

import argparse
import subprocess
import yaml


def install(args):
    try:
        subprocess.run(['sudo', 'apt-get', 'install', args.install[0], '-y'],
                       check=True)
    except subprocess.CalledProcessError:
        print(f'{args.install[0]} is not installed.')
    else:
        print(f"{args.install[0]} is installed successfully.")


def uninstall(args):
    try:
        subprocess.run(['sudo', 'apt-get', 'purge', args.uninstall[0], '-y'],
                       check=True)
        subprocess.run(['sudo', 'apt-get', 'autoclean'])
        subprocess.run(['sudo', 'apt-get', 'autoremove', '-y'])

    except subprocess.CalledProcessError:
        print(f'Failed in unstalling {args.uninstall[0]}.')
    else:
        print(f"{args.uninstall[0]} is uninstalled successfully.")


def apply(args):
    with open(args.apply[0], "r") as stream:
        try:
            print(yaml.safe_load(stream))
        except yaml.YAMLError as exc:
            print(exc)


def main():
    # create parser object
    parser = argparse.ArgumentParser(description="Welcome to use easy-config!")
    parser.add_argument("-i",
                        "--install",
                        type=str,
                        nargs=1,
                        metavar="package_name",
                        default=None,
                        help="Install the specified package.")

    parser.add_argument("-u",
                        "--uninstall",
                        type=str,
                        nargs=1,
                        metavar=('package_name'),
                        help="Uninstall the specified package.")

    parser.add_argument(
        "-a",
        "--apply",
        type=str,
        nargs=1,
        metavar=('file_name'),
        help=
        "Apply actions to specified targets. Actions can be creating, starting, configuring, etc."
    )

    # parse the arguments from standard input
    args = parser.parse_args()
    # calling functions depending on type of argument
    if args.install != None:
        install(args)
    if args.uninstall != None:
        uninstall(args)
    if args.apply != None:
        apply(args)


if __name__ == "__main__":
    # calling the main function
    main()