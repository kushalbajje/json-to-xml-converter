# JSON to XML Converter

## Table of Contents
1. [Project Overview](#project-overview)
2. [Project Structure](#project-structure)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Running Tests](#running-tests)
7. [JSON to XML Mapping Rules](#json-to-xml-mapping-rules)
8. [Example](#example)
9. [Libraries Used](#libraries-used)
10. [Troubleshooting](#troubleshooting)
11. [Distribution](#distribution)
12. [Setting up a Virtual Environment (Optional)](#setting-up-a-virtual-environment-optional)

## Project Overview
This Python project converts JSON data to XML format according to specific mapping rules.

## Project Structure
```
json-to-xml-converter/
├── main.py
├── test_json_to_xml.py
├── README.md
├── examples/
│   ├── example_input.json
│   └── expected_output.xml
└── output.xml
```

## Requirements
- Python 3.x

You can find the Python installation here: [https://www.python.org/downloads/](https://www.python.org/downloads/)

## Installation
1. Unzip the provided file to a directory of your choice.
2. Navigate to the extracted directory in your terminal or command prompt.
3. (Optional) Set up a virtual environment. While not strictly necessary for this project as it uses only standard libraries, it's a good practice for Python development. [See instructions below](#setting-up-a-virtual-environment-optional).

## Usage
To convert a JSON file to XML, use the following command:

```
python3 main.py <input_json_file> <output_xml_file>
```

For example:
```
python3 main.py examples/example_input.json output.xml
```

The script will validate the input file and permissions before processing. If any issues are found, an appropriate error message will be displayed.

## Running Tests
To run the test suite:

```
python3 test_json_to_xml.py
```

This will run all the tests defined in `test_json_to_xml.py`, including various scenarios like simple objects, nested objects, arrays, mixed types, empty objects/arrays, and null values.

## JSON to XML Mapping Rules
1. XML element names correspond to the type of the JSON value, not the name of the element.
2. The name of the JSON element in a JSON object is given as an attribute on the XML element.
3. Only JSON array and object values are supported at the top level of a file.
4. Numbers are represented by the `<number>` tag.
5. Strings are represented by the `<string>` tag.
6. Booleans are represented by the `<boolean>` tag with lowercase "true" or "false" as the value.
7. Arrays are represented by the `<array>` tag, with each element as a child node.
8. Objects are represented by the `<object>` tag, with each key-value pair as a child node.
9. Null values are represented by a self-closing `<null />` tag.

## Example
Input JSON (`examples/example_input.json`):
```json
{
    "organization" : {
        "name" : "Securin",
        "type" : "Inc",
        "building_number" : 4,
        "floating" : -17.4,
        "null_test": null
    },
    "security_related" : true,
    "array_example0" : ["red", "green", "blue", "black"],
    "array_example1" : [1, "red", [{ "nested" : true}], { "obj" : false}]
}
```

Run the converter:
```
python3 main.py examples/example_input.json output.xml
```

This will generate `output.xml` with the converted XML content.

## Libraries Used
This project uses only Python standard libraries:

- `json`: For parsing JSON data
- `sys`: For command-line arguments
- `os`: For file and directory operations
- `unittest`: For running tests

## Troubleshooting
If you encounter any issues:
1. Ensure you're using Python 3.x.
2. Check that the virtual environment is activated (if you're using one).
3. Check that the input JSON file exists, has a .json extension, and is properly formatted.
4. Make sure you have read permissions for the input file and write permissions for the output directory.
5. If you receive a "Invalid JSON" error, verify that your input file contains valid JSON data.
6. For any other errors, check the error message displayed by the script for specific details.

If problems persist, please check your input file and permissions, and ensure you're using the correct command format.

## Distribution
When sharing this project, it's important to create a zip file that includes only the necessary files and excludes any environment-specific or generated content. Here's a simple way to do this:

1. Ensure you're in the project root directory.
2. Include only the following files and directories in your zip:
   - main.py
   - test_json_to_xml.py
   - README.md
   - examples/ directory

3. You can create this zip file manually using your operating system's built-in zip functionality, or use a command line tool if you prefer.

4. Do not include:
   - The virtual environment directory (venv/)
   - Any *.pyc files or __pycache__/ directories
   - Any personal configuration files or directories

Remember, users of your project will create their own virtual environment following the instructions in this README.

## Setting up a Virtual Environment (Optional)
While this project doesn't require any additional packages, setting up a virtual environment is still a good practice for Python development. It keeps your project isolated from your system Python installation. Here's how to set it up:

1. Open a terminal/command prompt and navigate to the project directory.

2. Create a virtual environment:
   ```
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```
    If you encounter a "permission denied" error on macOS or Linux, use the following commands:
    ```
    chmod +x venv/bin/activate
    source venv/bin/activate
    ```
    
4. Your prompt should change to indicate that the virtual environment is active.

5. When you're done working on the project, you can deactivate the virtual environment:
   ```
   deactivate
   ```