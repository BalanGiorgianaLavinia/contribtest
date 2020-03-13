import unittest
import generate


class Tests(unittest.TestCase):

    def test_reading_correctly(self):
        expected = ({"title": "Contact us!", "layout": "base.html"}, 
                    "\nWrite an email to contact@example.com.\n")
        code_result = generate.read_file('test/source/contact.rst')

        self.assertEqual(code_result, expected)

    def test_reading_no_metadata(self):
        expected_meta = {}
        expected_content = "CONTENT"

        empty_file = open('emptyFile.rst', 'w')
        empty_file.write("{}\n---\nCONTENT")
        empty_file.close()

        metadata, content = generate.read_file('emptyFile.rst')
        
        self.assertEqual(metadata, expected_meta)
        self.assertEqual(content, expected_content)

if __name__ == '__main__':
    unittest.main()