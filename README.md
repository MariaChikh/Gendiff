### Hexlet tests and linter status:
[![Actions Status](https://github.com/MariaChikh/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/MariaChikh/python-project-50/actions)

[![hexlet-check](https://github.com/MariaChikh/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/MariaChikh/python-project-50/actions/workflows/hexlet-check.yml)

[![Maintainability](https://api.codeclimate.com/v1/badges/a4d0ceab80c0aaffeef0/maintainability)](https://codeclimate.com/github/MariaChikh/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/a4d0ceab80c0aaffeef0/test_coverage)](https://codeclimate.com/github/MariaChikh/python-project-50/test_coverage)

## Gendiff

## Description:

This is the difference calculator - a command line utility which can find differences between two files. It supports .json and yaml. formats.

## Installation:

Install using pip:
pip install git+https://github.com/MariaChikh/python-project-50.git

Install using poetry:
Clone the repository https://github.com/MariaChikh/python-project-50.git
cd gendiff
poetry install

## Usage:
To find differences between two files:

gendiff <file_path1><file_path2>

Sample output:

{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}

## Options:
-h, --help 
-f, --format - set the output format (supported formats: `plain`, `json`, `stylish`). Default format 'stylish'

stylish - shows differences as a tree
plain - shows differences in following format 'Property 'common.follow' was added with value: false'
json - showa differences in json

## Dependencies:
python = "^3.10"
pyyaml = "^6.0.2"


How it works:
With .json files without nested structures

[![asciicast](https://asciinema.org/a/YYcms1mAnpB120WXLK1K5tuhQ.svg)](https://asciinema.org/a/YYcms1mAnpB120WXLK1K5tuhQ)

With .yaml files without nested structures

[![asciicast](https://asciinema.org/a/hvpR8g0d8HdNp5E6nujktr3VZ.svg)](https://asciinema.org/a/hvpR8g0d8HdNp5E6nujktr3VZ)

Stylish formatter

[![asciicast](https://asciinema.org/a/AarLLQMvkb5uvMHn13opZOYqh.svg)](https://asciinema.org/a/AarLLQMvkb5uvMHn13opZOYqh)

Plain formatter

[![asciicast](https://asciinema.org/a/mBYJp9CJTJ6z9HZQhRZn7GziY.svg)](https://asciinema.org/a/mBYJp9CJTJ6z9HZQhRZn7GziY)

JSON formatter

[![asciicast](https://asciinema.org/a/6QXjceor5YUbu2TbiFZBNqZtg.svg)](https://asciinema.org/a/6QXjceor5YUbu2TbiFZBNqZtg)
