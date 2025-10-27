"""
Unit tests for the Name Sorter module.

This module contains comprehensive tests for the NameSorter class,
including edge cases and error conditions.
"""

import unittest
import tempfile
import os
import sys
from pathlib import Path

# Add the src directory to the Python path for testing
script_dir = Path(__file__).parent.parent
src_dir = script_dir / 'src'
sys.path.insert(0, str(src_dir))

from name_sorter import NameSorter


class TestNameSorter(unittest.TestCase):
    """Test cases for the NameSorter class."""
    
    def test_parse_name_valid_cases(self):
        """Test parsing valid name formats."""
        # Test with 2 parts (1 given name + 1 last name)
        last_name, given_names = NameSorter.parse_name("John Smith")
        self.assertEqual(last_name, "Smith")
        self.assertEqual(given_names, ["John"])
        
        # Test with 3 parts (2 given names + 1 last name)
        last_name, given_names = NameSorter.parse_name("John Michael Smith")
        self.assertEqual(last_name, "Smith")
        self.assertEqual(given_names, ["John", "Michael"])
        
        # Test with 4 parts (3 given names + 1 last name)
        last_name, given_names = NameSorter.parse_name("John Michael David Smith")
        self.assertEqual(last_name, "Smith")
        self.assertEqual(given_names, ["John", "Michael", "David"])
        
        # Test with extra whitespace
        last_name, given_names = NameSorter.parse_name("  John   Smith  ")
        self.assertEqual(last_name, "Smith")
        self.assertEqual(given_names, ["John"])
    
    def test_parse_name_invalid_cases(self):
        """Test parsing invalid name formats."""
        # Test with only one name (no given name)
        with self.assertRaises(ValueError):
            NameSorter.parse_name("Smith")
        
        # Test with too many names (more than 3 given names)
        with self.assertRaises(ValueError):
            NameSorter.parse_name("John Michael David Robert Smith")
        
        # Test with empty string
        with self.assertRaises(ValueError):
            NameSorter.parse_name("")
        
        # Test with only whitespace
        with self.assertRaises(ValueError):
            NameSorter.parse_name("   ")
    
    def test_sort_names_basic(self):
        """Test basic name sorting functionality."""
        names = [
            "Janet Parsons",
            "Vaughn Lewis", 
            "Adonis Julius Archer"
        ]
        
        expected = [
            "Adonis Julius Archer",
            "Vaughn Lewis",
            "Janet Parsons"
        ]
        
        result = NameSorter.sort_names(names)
        self.assertEqual(result, expected)
    
    def test_sort_names_complete_example(self):
        """Test sorting with the complete example from the requirements."""
        names = [
            "Janet Parsons",
            "Vaughn Lewis",
            "Adonis Julius Archer",
            "Shelby Nathan Yoder",
            "Marin Alvarez",
            "London Lindsey",
            "Beau Tristan Bentley",
            "Leo Gardner",
            "Hunter Uriah Mathew Clarke",
            "Mikayla Lopez",
            "Frankie Conner Ritter"
        ]
        
        expected = [
            "Marin Alvarez",
            "Adonis Julius Archer",
            "Beau Tristan Bentley",
            "Hunter Uriah Mathew Clarke",
            "Leo Gardner",
            "Vaughn Lewis",
            "London Lindsey",
            "Mikayla Lopez",
            "Janet Parsons",
            "Frankie Conner Ritter",
            "Shelby Nathan Yoder"
        ]
        
        result = NameSorter.sort_names(names)
        self.assertEqual(result, expected)
    
    def test_sort_names_same_last_name(self):
        """Test sorting when multiple people have the same last name."""
        names = [
            "John Smith",
            "Alice Smith", 
            "Bob Smith"
        ]
        
        expected = [
            "Alice Smith",
            "Bob Smith", 
            "John Smith"
        ]
        
        result = NameSorter.sort_names(names)
        self.assertEqual(result, expected)
    
    def test_sort_names_same_last_and_first_name(self):
        """Test sorting when people have same last name and same first given name."""
        names = [
            "John Michael Smith",
            "John Adam Smith",
            "John Smith"
        ]
        
        expected = [
            "John Smith",          # Fewer given names come first
            "John Adam Smith", 
            "John Michael Smith"
        ]
        
        result = NameSorter.sort_names(names)
        self.assertEqual(result, expected)
    
    def test_sort_names_case_insensitive(self):
        """Test that sorting is case-insensitive."""
        names = [
            "john smith",
            "Alice JONES", 
            "Bob Anderson"
        ]
        
        expected = [
            "Bob Anderson",
            "Alice JONES",
            "john smith"
        ]
        
        result = NameSorter.sort_names(names)
        self.assertEqual(result, expected)
    
    def test_sort_names_empty_list(self):
        """Test sorting an empty list."""
        result = NameSorter.sort_names([])
        self.assertEqual(result, [])
    
    def test_sort_names_single_name(self):
        """Test sorting a list with a single name."""
        names = ["John Smith"]
        result = NameSorter.sort_names(names)
        self.assertEqual(result, names)
    
    def test_read_names_from_file_valid(self):
        """Test reading names from a valid file."""
        # Create a temporary file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("John Smith\n")
            f.write("Alice Jones\n")
            f.write("Bob Anderson\n")
            temp_file = f.name
        
        try:
            names = NameSorter.read_names_from_file(temp_file)
            expected = ["John Smith", "Alice Jones", "Bob Anderson"]
            self.assertEqual(names, expected)
        finally:
            os.unlink(temp_file)
    
    def test_read_names_from_file_with_empty_lines(self):
        """Test reading names from a file with empty lines."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("John Smith\n")
            f.write("\n")  # Empty line
            f.write("Alice Jones\n")
            f.write("   \n")  # Whitespace only
            f.write("Bob Anderson\n")
            temp_file = f.name
        
        try:
            names = NameSorter.read_names_from_file(temp_file)
            expected = ["John Smith", "Alice Jones", "Bob Anderson"]
            self.assertEqual(names, expected)
        finally:
            os.unlink(temp_file)
    
    def test_read_names_from_nonexistent_file(self):
        """Test reading from a file that doesn't exist."""
        with self.assertRaises(FileNotFoundError):
            NameSorter.read_names_from_file("nonexistent_file.txt")
    
    def test_write_names_to_file(self):
        """Test writing names to a file."""
        names = ["John Smith", "Alice Jones", "Bob Anderson"]
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            temp_file = f.name
        
        try:
            NameSorter.write_names_to_file(names, temp_file)
            
            # Read back and verify
            with open(temp_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            expected_content = "John Smith\nAlice Jones\nBob Anderson\n"
            self.assertEqual(content, expected_content)
        finally:
            os.unlink(temp_file)
    
    def test_write_names_empty_list(self):
        """Test writing an empty list to a file."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            temp_file = f.name
        
        try:
            NameSorter.write_names_to_file([], temp_file)
            
            # Read back and verify
            with open(temp_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            self.assertEqual(content, "")
        finally:
            os.unlink(temp_file)


class TestNameSorterIntegration(unittest.TestCase):
    """Integration tests for the complete name sorting workflow."""
    
    def test_full_workflow(self):
        """Test the complete workflow: read -> sort -> write."""
        # Create input file
        input_names = [
            "Janet Parsons",
            "Vaughn Lewis",
            "Adonis Julius Archer",
            "Shelby Nathan Yoder",
            "Marin Alvarez"
        ]
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            for name in input_names:
                f.write(f"{name}\n")
            input_file = f.name
        
        with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as f:
            output_file = f.name
        
        try:
            # Read names
            names = NameSorter.read_names_from_file(input_file)
            
            # Sort names
            sorted_names = NameSorter.sort_names(names)
            
            # Write sorted names
            NameSorter.write_names_to_file(sorted_names, output_file)
            
            # Verify the result
            result_names = NameSorter.read_names_from_file(output_file)
            
            expected = [
                "Marin Alvarez",
                "Adonis Julius Archer",
                "Vaughn Lewis",
                "Janet Parsons",
                "Shelby Nathan Yoder"
            ]
            
            self.assertEqual(result_names, expected)
            
        finally:
            os.unlink(input_file)
            os.unlink(output_file)


if __name__ == '__main__':
    unittest.main()