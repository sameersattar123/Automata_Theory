import re

# Define token patterns using regular expressions
TOKEN_REGEX = [
    ('INTEGER', r'\d+'),
    ('IDENTIFIER', r'_[a-zA-Z_]\w*'),
    ('PLUS', r'\+'),
    ('MINUS', r'-'),
    ('TIMES', r'\*'),
    ('DIVIDE', r'/'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('ASSIGN', r'='),
    ('SEMICOLON', r';'),
]

# Lexical analyzer function
def tokenize(code):
    tokens = []
    code = code.strip()  # Remove leading/trailing whitespace
    while code:
        match = None
        for token_type, pattern in TOKEN_REGEX:
            regex = re.compile(pattern)
            match = regex.match(code)
            if match:
                value = match.group(0)
                tokens.append((token_type, value))
                code = code[len(value):].strip()
                break
        if not match:
            raise SyntaxError("Invalid syntax near: {}".format(code))
    return tokens

# Example usage
code = "_x = 10 - _y + 20 / _z * _r;"
tokens = tokenize(code)
print(tokens)
