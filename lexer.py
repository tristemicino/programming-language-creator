def lexer(code):
    tokens = []
    words = code.split()

    for word in words:
        if word == "print":
            tokens.append(("COMMAND", "print"))
        elif word.isdigit():
            tokens.append(("NUMBER", int(word)))
        else:
            tokens.append(("TEXT", word))
    
    return tokens

# Test
code = "print hello 123"
result = lexer(code)
print(result)
