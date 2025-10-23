# scanner-c
A C code token scanner implemented in python

# C Code Scanner

A Python-based lexical analyzer (scanner) for C programming language that tokenizes input code.

## Features
- Identifies keywords, identifiers, numbers, operators, and special characters
- Handles single-line and multi-line comments
- Simple command-line interface
  
##Example Input:
int main() {
    int x = 5;
    return 0;
}

##Supported Tokens

· KEYWORD: int, main, if, else, return, for, while
· IDENTIFIER: variable and function names
· NUMBER: integers and decimals
· OPERATOR: =, ==, +, -, *, /, etc.
· SPECIAL CHARACTER: (){};, etc.
· COMMENTS: // and /* */


## Usage
```bash
python code.py
