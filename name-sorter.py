#!/usr/bin/env python3
"""
Name Sorter Main Script

Command-line tool to sort names from a file by last name, then by given names.

Usage:
    python name-sorter.py <input_file>

Example:
    python name-sorter.py ./unsorted-names-list.txt

The program will:
1. Read names from the input file
2. Sort them by last name, then by given names
3. Print the sorted names to the console
4. Write the sorted names to 'sorted-names-list.txt'
"""

import sys
import os
from pathlib import Path

# Add the src directory to the Python path
script_dir = Path(__file__).parent
src_dir = script_dir / 'src'
sys.path.insert(0, str(src_dir))

from name_sorter import NameSorter


def main():
    """Main function to handle command-line execution."""
    
    # Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python name-sorter.py <input_file>", file=sys.stderr)
        print("Example: python name-sorter.py ./unsorted-names-list.txt", file=sys.stderr)
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = "sorted-names-list.txt"
    
    try:
        # Read names from input file
        print(f"Reading names from: {input_file}")
        names = NameSorter.read_names_from_file(input_file)
        
        if not names:
            print("No names found in the input file.", file=sys.stderr)
            sys.exit(1)
        
        print(f"Found {len(names)} names to sort")
        
        # Sort the names
        sorted_names = NameSorter.sort_names(names)
        
        # Print sorted names to console
        print("\nSorted names:")
        for name in sorted_names:
            print(name)
        
        # Write sorted names to output file
        NameSorter.write_names_to_file(sorted_names, output_file)
        print(f"\nSorted names written to: {output_file}")
        
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()