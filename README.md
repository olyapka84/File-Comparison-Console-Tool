### Badges:
[![Actions Status](https://github.com/Olyapka84/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Olyapka84/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/29efa26f9a5d179835d0/maintainability)](https://codeclimate.com/github/Olyapka84/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/29efa26f9a5d179835d0/test_coverage)](https://codeclimate.com/github/Olyapka84/python-project-50/test_coverage)

## Description

Hi! This is another project in my Python learning journey. This application is a **file comparison console tool** that identifies differences between two configuration files and displays them in a visually clear format. 

### Key features:
- **File Comparison**: Compare two files and see what has changed.
- **Multiple Output Formats**:
  - **Stylish**: Default format that displays differences in a tree-like structure. Each change is marked with symbols: "+" for added items, "-" for removed items, unchanged items are displayed without symbols.
  - **Plain**: Human-readable textual representation of the differences.
  - **JSON**: Structured format suitable for further processing.

## Demonstration:

### Stylish format:

[![asciicast](https://asciinema.org/a/ke06TCMpcjqfpMbqt4dZdBAXW.svg)](https://asciinema.org/a/ke06TCMpcjqfpMbqt4dZdBAXW)

### Plain format:

[![asciicast](https://asciinema.org/a/kEpZ3fiAv363DBbQhw3EzFi5m.svg)](https://asciinema.org/a/kEpZ3fiAv363DBbQhw3EzFi5m)

### JSON format:

[![asciicast](https://asciinema.org/a/XJQgVJvFlWk84wLEPPjHF7sEU.svg)](https://asciinema.org/a/XJQgVJvFlWk84wLEPPjHF7sEU)

## How to install

1. **Clone the repository**:

    - Using HTTPS:
      ```bash
      git clone https://github.com/Olyapka84/python-project-50.git
      ```

    - Using SSH:
      ```bash
      git clone git@github.com:Olyapka84/python-project-50.git
      ```

    Navigate to the project directory:
    ```bash
    cd python-project-50
    ```

2. **Install the app** in one command using Makefile:

    ```bash
    make install
    ```

3. **Build the app**:

    ```bash
    make build
    ```

4. **Run the app**:

    After installation, you can compare files using the following command:
    ```bash
    gendiff path/to/first_file path/to/second_file
    ```
    You can also specify the output format using the -f or --format option (stylish is default):
    ```bash
    gendiff path/to/first_file path/to/second_file -f [stylish|plain|json]
    ```

5. **View Help**:

    To see usage instructions and available options, use the `-h` or `--help` flag:
    ```bash
    gendiff -h
    ```