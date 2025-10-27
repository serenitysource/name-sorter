# Name Sorter

A Python command-line tool that sorts names by last name, then by given names. Names must have at least 1 given name and may have up to 3 given names.

## Features

- Sort names by last name first, then by given names
- Read names from text files
- Output sorted names to console and file
- Robust error handling and validation
- Comprehensive unit tests
- Support for 1-3 given names per person

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```
4. (Optional) Install development dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

```bash
python name-sorter.py <input_file>
```

### Example

```bash
python name-sorter.py ./unsorted-names-list.txt
```

This will:
1. Read names from `unsorted-names-list.txt`
2. Sort them by last name, then by given names
3. Print the sorted names to the console
4. Write the sorted names to `sorted-names-list.txt`

### Input File Format

The input file should contain one name per line. Each name should have:
- At least 1 given name and 1 last name (minimum 2 parts)
- At most 3 given names and 1 last name (maximum 4 parts)

Example input file:
```
Janet Parsons
Vaughn Lewis
Adonis Julius Archer
Shelby Nathan Yoder
Marin Alvarez
London Lindsey
Beau Tristan Bentley
Leo Gardner
Hunter Uriah Mathew Clarke
Mikayla Lopez
Frankie Conner Ritter
```

### Expected Output

The program will output the sorted names to both console and file:
```
Marin Alvarez
Adonis Julius Archer
Beau Tristan Bentley
Hunter Uriah Mathew Clarke
Leo Gardner
Vaughn Lewis
London Lindsey
Mikayla Lopez
Janet Parsons
Frankie Conner Ritter
Shelby Nathan Yoder
```

## Sorting Rules

Names are sorted using the following priority:

1. **Last name** (case-insensitive alphabetical order)
2. **First given name** (case-insensitive alphabetical order)
3. **Second given name** (case-insensitive alphabetical order)
4. **Third given name** (case-insensitive alphabetical order)

Names with fewer given names will appear before names with more given names when all other parts are equal.

## Running Tests

Run the unit tests using Python's built-in unittest module:

```bash
python -m unittest tests.test_name_sorter -v
```

Or using pytest (if installed):

```bash
pytest tests/ -v
```

## Project Structure

```
name-sorter/
├── src/
│   ├── __init__.py
│   └── name_sorter.py          # Core sorting functionality
├── tests/
│   ├── __init__.py
│   └── test_name_sorter.py     # Comprehensive unit tests
├── name-sorter.py              # Main executable script
├── unsorted-names-list.txt     # Example input file
├── requirements.txt            # Dependencies (for testing)
├── .gitignore                  # Git ignore rules
└── README.md                   # This file
```

## API Reference

### NameSorter Class

The core functionality is provided by the `NameSorter` class in `src/name_sorter.py`.

#### Methods

- `parse_name(full_name: str)` - Parse a full name into last name and given names
- `sort_names(names: List[str])` - Sort a list of names
- `read_names_from_file(file_path: str)` - Read names from a text file
- `write_names_to_file(names: List[str], file_path: str)` - Write names to a text file

## Error Handling

The program handles various error conditions:

- **File not found**: Clear error message if input file doesn't exist
- **Invalid name format**: Error if names don't have 2-4 parts
- **Empty input**: Error if no valid names found in input file
- **IO errors**: Proper error handling for file read/write operations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## License

This project is provided as-is for educational and demonstration purposes.