from VikLang import lexer

def main():
    while True:
        print("\n=== VikLang Shell ===")
        print("1. Enter VikLang code")
        print("2. Help / How to Use")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            text = input("Enter VikLang code: ")
            tokens, error = lexer.run('<stdin>', text)
            if error:
                print(error.as_string())
            else:
                print(tokens)
        elif choice == "2":
            print("\n=== How to Use VikLang Shell ===")
            print("VikLang Shell allows you to input VikLang code and tokenize it.")
            print("\nYou can enter alphanumeric characters, numbers, and the following symbols:")
            print("   + - * / ( ) = ; , '")
            print("\nExample Input:")
            print("If you enter 'a = 10 + 20 * 5'")
            print("\nExpected Output:")
            print("[<STRING: 'a'>, <EQUALS>, <INT: 10>, <PLUS>, <INT: 20>, <MUL>, <INT: 5>]")
            print("\nThis output represents the tokens generated from the input code.")
            print("Each token is represented by its type and value (if applicable), enclosed in angle brackets.")
        elif choice == "3":
            print("Exiting VikLang Shell. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()