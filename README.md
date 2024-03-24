Vik Lexer
=======

VikLang is a simple programming language designed for basic operations such as arithmetic calculations, variable assignment, and string manipulation. This project includes a lexer module that tokenizes VikLang code into meaningful tokens for further processing.

File Structure
--------------

    Vik-Lexer
    │
    ├── VikLang
    │   └── lexer.py
    │
    ├── main.py
    ├── requirements.txt
    ├── LICENSE
    ├── README.md
    ├── .gitignore

Examples
--------

### Example Input

```bash
a = 10 + 20 * 5
```

### Expected Output (Tokens)

```bash
[<STRING: a>, <EQUALS>, <INT: 10>, <PLUS>, <INT: 20>, <MUL>, <INT: 5>]
```

This output represents the tokens generated from the input code. Each token type is enclosed in angle brackets.

How to Use
----------

1.  Clone the repository.

    ```bash
    git clone https://github.com/Vikranth3140/Vik-Lexer.git
    ```

2. Install required dependencies.

    ```bash
    pip install -r requirements.txt
    ```

4.  Run the VikLang Shell.

    ```bash
    python main.py
    ```

    This will start an interactive shell where you can test out your code or use it for writing programs in VikLang.

5.  Choose option 1 to enter VikLang code and see tokenized output.

6.  Choose option 2 to view the usage instructions and examples.

How to Contribute
----------

Contributions to VikLang are welcome! If you'd like to contribute, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature-new-feature`).
3.  Make your changes and commit them (`git commit -am 'Add new feature'`).
4.  Push to the branch (`git push origin feature-new-feature`).
5.  Create a new Pull Request.

License
-------

This project is licensed under the [MIT License](LICENSE).