"""
Name Sorter Module

This module provides functionality to sort names by last name, then by given names.
A name must have at least 1 given name and may have up to 3 given names.
"""

import re
from typing import List, Tuple


class NameSorter:
    """
    A class to sort names by last name first, then by given names.
    """
    
    @staticmethod
    def parse_name(full_name: str) -> Tuple[str, List[str]]:
        """
        Parse a full name into last name and given names.
        
        Args:
            full_name (str): The full name to parse (e.g., "John Michael Smith")
            
        Returns:
            Tuple[str, List[str]]: A tuple containing (last_name, given_names_list)
            
        Raises:
            ValueError: If the name doesn't have at least 1 given name or has more than 3 given names
        """
        # Clean and split the name
        name_parts = full_name.strip().split()
        
        if len(name_parts) < 2:
            raise ValueError(f"Name '{full_name}' must have at least 1 given name and 1 last name")
        
        if len(name_parts) > 4:
            raise ValueError(f"Name '{full_name}' cannot have more than 3 given names")
        
        # Last name is the last part, given names are all previous parts
        last_name = name_parts[-1]
        given_names = name_parts[:-1]
        
        return last_name, given_names
    
    @staticmethod
    def sort_names(names: List[str]) -> List[str]:
        """
        Sort a list of names by last name first, then by given names.
        
        Args:
            names (List[str]): List of full names to sort
            
        Returns:
            List[str]: Sorted list of names
            
        Raises:
            ValueError: If any name is invalid (wrong number of parts)
        """
        # Parse all names and create sorting tuples
        parsed_names = []
        
        for name in names:
            try:
                last_name, given_names = NameSorter.parse_name(name)
                # Create a sorting key: (last_name, given_name_1, given_name_2, given_name_3)
                # Pad given names with empty strings if fewer than 3
                sorting_key = [last_name.lower()] + [gn.lower() for gn in given_names] + [''] * (3 - len(given_names))
                parsed_names.append((sorting_key, name))
            except ValueError as e:
                raise ValueError(f"Invalid name format: {e}")
        
        # Sort by the sorting key
        parsed_names.sort(key=lambda x: x[0])
        
        # Return the original names in sorted order
        return [name for _, name in parsed_names]
    
    @staticmethod
    def read_names_from_file(file_path: str) -> List[str]:
        """
        Read names from a text file, one name per line.
        
        Args:
            file_path (str): Path to the input file
            
        Returns:
            List[str]: List of names from the file
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            IOError: If there's an error reading the file
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                names = [line.strip() for line in file if line.strip()]
            return names
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except IOError as e:
            raise IOError(f"Error reading file {file_path}: {e}")
    
    @staticmethod
    def write_names_to_file(names: List[str], file_path: str) -> None:
        """
        Write names to a text file, one name per line.
        
        Args:
            names (List[str]): List of names to write
            file_path (str): Path to the output file
            
        Raises:
            IOError: If there's an error writing the file
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                for name in names:
                    file.write(f"{name}\n")
        except IOError as e:
            raise IOError(f"Error writing to file {file_path}: {e}")