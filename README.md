# Prerequisite

Make sure that sudo and git packages are installed on your machine. Othewise, run the following commands:

- apt update & apt upgrade
- apt-get install sudo
- sudo apt-get update
- sudo apt-get install git

# Installation Guide

- sudo git clone https://github.com/bipubipu/easy-config.git
- cd easy-config
- bash bootstrap.sh

# Use Guide

You can start by running **python3 cli.py -h**.  
This is a configuration management tool to offer you a way to manage servers.
Current supporting functions include:

- Install packages
- Uninstall packages

Test folder contains an example and description of configuration file setup. Yaml is the only format that is accepted now.

# Devlopment Roadmap

- Further abstraction. Ideal command is like **easy-config -xx**
- Introduce the concept of role to have more strict permission control
- Restart the service when relevant files or packages are updated
- Allow user to specify file's content and metadata
- Invoke commands in the configuration
- Install dependencies in the configuration
- Support multiple versions of OS
