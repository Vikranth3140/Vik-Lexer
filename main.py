from VikLang import lexer

def main():
    while True:
        print("\n=== VikLang Shell ===")
        print("1. Enter VikLang code")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            text = input("Enter VikLang code: ")
            tokens, error = lexer.run('<stdin>', text)
            if error:
                print(error.as_string())
            else:
                print(tokens)
        elif choice == "2":
            print("Exiting VikLang Shell. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()