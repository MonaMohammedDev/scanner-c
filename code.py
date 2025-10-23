import sys 
import re

sys.stdout.reconfigure(encoding="utf-8")

keywords = ["int", "main", "if", "else", "return", "for", "while"]
specialChar = ["(", ")", "{", "}", ",", ";"]
operators = ["=", "<", ">", "*", "/", '+', '-', "==", "!=", "<=", ">=","++","--"]

def scan_code(line):
    tokens = []
    identifier_pattern = r'[a-zA-Z_][a-zA-Z0-9_]*'
    number_pattern = r'\d+\.?\d*'
    single_comment_pattern = r'//.*'
    multi_comment_pattern = r'/\*.*?\*/'  
  
    pos = 0
    while pos < len(line):
        if line[pos].isspace():
            pos += 1
            continue

        if line.startswith('//', pos):
            comment_match = re.match(single_comment_pattern, line[pos:])
            if comment_match:
                tokens.append(('SINGLE LINE COMMENT', comment_match.group()))
                pos += len(comment_match.group())
                continue
        
        if line.startswith('/*', pos):
            comment_match = re.match(multi_comment_pattern, line[pos:], re.DOTALL)
            if comment_match:
                tokens.append(('MULTIPLE LINE COMMENT', comment_match.group()))
                pos += len(comment_match.group())
                continue
        
        identifier_match = re.match(identifier_pattern, line[pos:])
        if identifier_match:
            identifier = identifier_match.group()
            if identifier in keywords:
                tokens.append(('KEYWORD', identifier))
            else:
                tokens.append(('IDENTIFIER', identifier))
            pos += len(identifier)
            continue
        
        number_match = re.match(number_pattern, line[pos:])
        if number_match:
            tokens.append(('NUMBER', number_match.group()))
            pos += len(number_match.group())
            continue
        
        found_operator = False
        for op in sorted(operators, key=len, reverse=True):
            if line.startswith(op, pos):
                tokens.append(('OPERATOR', op))
                pos += len(op)
                found_operator = True
                break
        
        if found_operator:
            continue
        
        found_special = False
        for sc in specialChar:
            if line.startswith(sc, pos):
                tokens.append(('SPECIAL CHARACTER', sc))
                pos += len(sc)
                found_special = True
                break
        
        if found_special:
            continue
        
        pos += 1
    
    return tokens

def main():
    print("=== C Code Scanner ===")
    print("Enter your C code (press Enter twice to finish): ")
    lines = []
    
    while True:
        try:
            line = input()
            if line == "" and lines:  
                break
            lines.append(line)
        except EOFError:
            break
    
    code = '\n'.join(lines)  
    
    if not code.strip():
        print("No code entered!")
        return
    
    tokens = scan_code(code)
    
    print("\n=== Results ===")  
    for token_type, token_value in tokens:
        print(f"<{token_type}, {token_value}>")

if __name__ == "__main__":
    main()