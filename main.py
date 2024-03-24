from VikLang import lexer

def main():
    text = input("Enter VikLang code: ")
    tokens, error = lexer.run('<stdin>', text)
    if error:
        print(error.as_string())
    else:
        print(tokens)

if __name__ == "__main__":
    main()