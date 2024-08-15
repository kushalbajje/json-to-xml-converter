import json
import sys
import os

def json_to_xml(json_obj, line_padding=""):
    """
    Recursively convert a JSON object to an XML string.
    
    Args:
    json_obj: The JSON object to convert.
    line_padding: The padding to use for indentation (default is empty string).
    
    Returns:
    A string containing the XML representation of the JSON object.
    """
    result_list = []

    if isinstance(json_obj, dict):
        for tag_name, sub_obj in json_obj.items():
            if isinstance(sub_obj, dict):
                # Handle nested objects
                result_list.append(f"{line_padding}<object name=\"{tag_name}\">")
                result_list.append(json_to_xml(sub_obj, line_padding + "\t"))
                result_list.append(f"{line_padding}</object>")
            elif isinstance(sub_obj, list):
                # Handle arrays
                result_list.append(f"{line_padding}<array name=\"{tag_name}\">")
                result_list.append(json_to_xml(sub_obj, line_padding + "\t"))
                result_list.append(f"{line_padding}</array>")
            elif sub_obj is None:
                # Handle null values
                result_list.append(f"{line_padding}<null name=\"{tag_name}\" />")
            else:
                # Handle primitive types (string, number, boolean)
                result_list.append(f"{line_padding}<{type_to_tag(sub_obj)} name=\"{tag_name}\">{str(sub_obj).lower() if isinstance(sub_obj, bool) else sub_obj}</{type_to_tag(sub_obj)}>")
    
    elif isinstance(json_obj, list):
        for sub_obj in json_obj:
            if isinstance(sub_obj, dict):
                result_list.append(f"{line_padding}<object>")
                result_list.append(json_to_xml(sub_obj, line_padding + "\t"))
                result_list.append(f"{line_padding}</object>")
            elif isinstance(sub_obj, list):
                # Handle nested arrays
                result_list.append(f"{line_padding}<array>")
                result_list.append(json_to_xml(sub_obj, line_padding + "\t"))
                result_list.append(f"{line_padding}</array>")
            elif sub_obj is None:
                result_list.append(f"{line_padding}<null />")
            else:
                result_list.append(f"{line_padding}<{type_to_tag(sub_obj)}>{str(sub_obj).lower() if isinstance(sub_obj, bool) else sub_obj}</{type_to_tag(sub_obj)}>")

    return "\n".join(result_list)

def type_to_tag(value):
    """
    Convert Python types to corresponding XML tags.
    
    Args:
    value: The value to determine the type for.
    
    Returns:
    A string representing the XML tag for the given type.
    
    Raises:
    TypeError: If an unsupported type is encountered.
    """
    if isinstance(value, str):
        return "string"
    elif isinstance(value, bool):
        return "boolean"
    elif isinstance(value, (int, float)):
        return "number"
    elif value is None:
        return "null"
    else:
        raise TypeError(f"Unsupported JSON type: {type(value)}")

def main(json_input_path, xml_output_path):
    """
    Main function to handle the JSON to XML conversion process.
    
    Args:
    json_input_path: Path to the input JSON file.
    xml_output_path: Path where the output XML file will be saved.

    Raises:
    FileNotFoundError: If the input JSON file doesn't exist.
    json.JSONDecodeError: If the input file is not valid JSON.
    PermissionError: If there's no write permission for the output file.
    """
    # Check if input file exists
    if not os.path.exists(json_input_path):
        raise FileNotFoundError(f"Input file not found: {json_input_path}")

    # Check if input file has .json extension
    if not json_input_path.lower().endswith('.json'):
        raise ValueError("Input file must have a .json extension")

    # Check if we have read permissions for the input file
    if not os.access(json_input_path, os.R_OK):
        raise PermissionError(f"No read permission for input file: {json_input_path}")

    # Check if we have write permissions for the output file directory
    output_dir = os.path.dirname(xml_output_path)
    if output_dir and not os.access(output_dir, os.W_OK):
        raise PermissionError(f"No write permission for output directory: {output_dir}")

    try:
        # Read and parse the JSON file
        with open(json_input_path, 'r') as json_file:
            json_data = json.load(json_file)
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON in input file: {e}", e.doc, e.pos)

    # Convert JSON to XML
    xml_str = "<object>\n" + json_to_xml(json_data, "\t") + "\n</object>"
    
    # Write the XML to file
    try:
        with open(xml_output_path, 'w') as xml_file:
            xml_file.write(xml_str)
    except PermissionError:
        raise PermissionError(f"No write permission for output file: {xml_output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("\nIncorrect number of arguments. Please use the format below to run the application:\n")
        print("Usage: python main.py <input_json_file> <output_xml_file>\n")
        sys.exit(1)

    json_input_path = sys.argv[1]
    xml_output_path = sys.argv[2]
    
    try:
        main(json_input_path, xml_output_path)
        print(f"Conversion successful. XML output saved to {xml_output_path}")
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)