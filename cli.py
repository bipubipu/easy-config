
import os
import argparse
import subprocess


def install(args):
    exit_code = os.system(f'sudo apt-get install {args[0]}')
    if (exit_code == 0):
        print(f'Install {args[0]} successfully.')
    else:
        print(f'Failed in installing {args[0]}.')


def unstall(args):
    package_list = subprocess.check_output('sudo apt-get --list')
    print(
        f'The packages that are installed on this server are as follows:\n {package_list}'
    )

    os.system(f'sudo apt-get remove {args[0]}')


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
                        "--unstall",
                        type=str,
                        nargs=1,
                        metavar=('package_name'),
                        help="Uninstall the specified package.")

    # parse the arguments from standard input
    args = parser.parse_args()
    # calling functions depending on type of argument
    if args.install != None:
        install(args)


if __name__ == "__main__":
    # calling the main function
    main()