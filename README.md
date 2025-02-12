### Badges:
[![Actions Status](https://github.com/Olyapka84/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Olyapka84/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/29efa26f9a5d179835d0/maintainability)](https://codeclimate.com/github/Olyapka84/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/29efa26f9a5d179835d0/test_coverage)](https://codeclimate.com/github/Olyapka84/python-project-50/test_coverage)

## Description

Hi there! This is another exciting project in my Python learning journey. This application is a **file comparison tool** that identifies differences between two configuration files and displays them in a visually clear format. The project aims to make configuration management easier by quickly spotting discrepancies. 

### Key Features:
- **File Comparison**: Easily compare two files and see what has changed.
- **Multiple Output Formats**:
  - **Plain**: Human-readable textual representation of the differences.
  - **JSON**: Structured format suitable for further processing or integration.
- **Beginner-Friendly**: Simple and intuitive command-line interface.

## Demonstration:

[![asciicast](https://asciinema.org/a/ke06TCMpcjqfpMbqt4dZdBAXW.svg)](https://asciinema.org/a/ke06TCMpcjqfpMbqt4dZdBAXW)

## How to Install This App

1. **Clone the repository** (choose one of the following):

    - Using HTTPS:
      ```bash
      git clone https://github.com/Olyapka84/python-project-50.git
      ```

    - Using SSH:
      ```bash
      git clone git@github.com:Olyapka84/python-project-50.git
      ```

    Then navigate to the project directory:
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

5. **View Help**:

    To see usage instructions and available options, use the `-h` or `--help` flag:
    ```bash
    gendiff -h
    ```

    ### Optional Arguments:
    - Use the `-f` or `--format` flag to specify the output format:
      - `plain` (default)
      - `json`
    - Example:
      ```bash
      gendiff file1.json file2.json -f json
      ```

Good luck and happy coding! 😊