import unittest
import json
from main import json_to_xml

class TestJsonToXml(unittest.TestCase):
    """
    Test suite for the JSON to XML converter.
    This class contains various test cases to ensure the correct functionality
    of the json_to_xml function for different JSON structures.
    """

    def test_output_file(self):
        """
        Test the full conversion process including file I/O operations.
        This test runs the main function and compares the output file
        with the expected XML file.
        """
        import main
        main.main('examples/example_input.json', 'output.xml')

        with open('examples/expected_output.xml', 'r') as expected_file:
            expected_xml = expected_file.read()
        with open('output.xml', 'r') as actual_file:
            actual_xml = actual_file.read()
    
        self.assert_xml_equal(expected_xml.strip(), actual_xml.strip())

    def assert_xml_equal(self, expected_xml, actual_xml):
        """
        Helper method to assert equality of two XML strings.
        This method normalizes the XML strings by removing whitespace
        before comparison to avoid issues with formatting differences.
        """
        def normalize_xml(xml_string):
            return ' '.join(xml_string.split())

        expected_normalized = normalize_xml(expected_xml)
        actual_normalized = normalize_xml(actual_xml)
        self.assertEqual(expected_normalized, actual_normalized)

    def test_simple_object(self):
        """
        Test conversion of a simple JSON object with string and number values.
        """
        json_input = {"name": "John", "age": 30}
        expected_xml = """
        <object>
            <string name="name">John</string>
            <number name="age">30</number>
        </object>
        """
        actual_xml = "<object>\n" + json_to_xml(json_input, "\t") + "\n</object>"
        self.assert_xml_equal(expected_xml.strip(), actual_xml.strip())

    def test_nested_object(self):
        """
        Test conversion of a JSON object with a nested object.
        """
        json_input = {"person": {"name": "Alice", "age": 25}}
        expected_xml = """
        <object>
            <object name="person">
                <string name="name">Alice</string>
                <number name="age">25</number>
            </object>
        </object>
        """
        actual_xml = "<object>\n" + json_to_xml(json_input, "\t") + "\n</object>"
        self.assert_xml_equal(expected_xml.strip(), actual_xml.strip())

    def test_array(self):
        """
        Test conversion of a JSON object containing an array.
        """
        json_input = {"colors": ["red", "green", "blue"]}
        expected_xml = """
        <object>
            <array name="colors">
                <string>red</string>
                <string>green</string>
                <string>blue</string>
            </array>
        </object>
        """
        actual_xml = "<object>\n" + json_to_xml(json_input, "\t") + "\n</object>"
        self.assert_xml_equal(expected_xml.strip(), actual_xml.strip())

    def test_mixed_types(self):
        """
        Test conversion of a JSON object with mixed types including nested structures.
        """
        json_input = {
            "name": "Test",
            "values": [1, "two", True, None],
            "nested": {"a": 1, "b": [2, 3]}
        }
        expected_xml = """
        <object>
            <string name="name">Test</string>
            <array name="values">
                <number>1</number>
                <string>two</string>
                <boolean>true</boolean>
                <null />
            </array>
            <object name="nested">
                <number name="a">1</number>
                <array name="b">
                    <number>2</number>
                    <number>3</number>
                </array>
            </object>
        </object>
        """
        actual_xml = "<object>\n" + json_to_xml(json_input, "\t") + "\n</object>"
        self.assert_xml_equal(expected_xml.strip(), actual_xml.strip())

    def test_empty_object(self):
        """
        Test conversion of an empty JSON object.
        """
        json_input = {}
        expected_xml = "<object>\n</object>"
        actual_xml = "<object>\n" + json_to_xml(json_input, "\t") + "\n</object>"
        self.assert_xml_equal(expected_xml.strip(), actual_xml.strip())

    def test_empty_array(self):
        """
        Test conversion of a JSON object with an empty array.
        """
        json_input = {"empty": []}
        expected_xml = """
        <object>
            <array name="empty">
            </array>
        </object>
        """
        actual_xml = "<object>\n" + json_to_xml(json_input, "\t") + "\n</object>"
        self.assert_xml_equal(expected_xml.strip(), actual_xml.strip())

    def test_null_value(self):
        """
        Test conversion of a JSON object with a null value.
        """
        json_input = {"nullValue": None}
        expected_xml = """
        <object>
            <null name="nullValue" />
        </object>
        """
        actual_xml = "<object>\n" + json_to_xml(json_input, "\t") + "\n</object>"
        self.assert_xml_equal(expected_xml.strip(), actual_xml.strip())

    def test_file_conversion(self):
        """
        Test conversion of a JSON file to XML.
        This test reads from an example JSON file and compares the output
        with an expected XML file.
        """
        with open('examples/example_input.json', 'r') as json_file:
            json_input = json.load(json_file)
        with open('examples/expected_output.xml', 'r') as xml_file:
            expected_xml = xml_file.read()
        
        actual_xml = "<object>\n" + json_to_xml(json_input, "\t") + "\n</object>"
        self.assert_xml_equal(expected_xml.strip(), actual_xml.strip())

if __name__ == '__main__':
    unittest.main()