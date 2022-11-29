# Python - Hello, World

## Description:
* `0-run` is a Shell script that runs a Python script.

* `1-run_inline` is a a Shell script that runs Python code.

* `2-print.py` is a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.

* `3-print_number.py` prints the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.

* `4-print_float.py` prints the float stored in the variable `number` with a precision of 2 digits.

* `5-print_string.py` prints 3 times a string stored in the variable `str`, followed by its first 9 characters.

* `6-concat.py` prints `Welcome to Holberton School!`

* `7-edges.py:`
  * `word_first_3` contains the first 3 letters of the variable `word`
  * `word_last_2` contains the last 2 letters of the variable `word`
  * `middle_word` contains the value of the variable `word` without the first and last letters

* `8-concat_edges.py` prints `object-oriented programming with Python`, followed by a new line.

* `9-easter_egg.py` prints “The Zen of Python”, by TimPeters, followed by a new line.

* `10-check_cycle.c:` Technical Interview Preparation
  * is  a function in C that checks if a singly linked list has a cycle in it.
  * Prototype: `int check_cycle(listint_t *list);`
  * Return: `0` if there is no cycle, `1` if there is a cycle
  
* `100-write.py` is  a Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.
  * It uses the function `write` from the `sys` module
  * It prints to `stderr`
  * It exits with the status code `1`
  
* `101-compile` compiles a Python script file.
  * The Python file is stored in the environment variable `$PYFILE`
  * The output filename has to be `$PYFILEc` (ex: `export PYFILE=my_main.py` => output filename: `my_main.pyc`)

* `102-magic_calculation.py` contains the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:
  ```
   3          0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
 
* `lists.h` is the header file for [10-check_cycle.c](./10-check_cycle.c)

### The Zen of Python
```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
