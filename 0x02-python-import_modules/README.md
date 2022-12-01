# Python - import & modules

## Prototypes
`def add(a, b):`

`def sub(a, b):`

`def mul(a, b):`

`def div(a, b):`

`def magic_calculation(a, b):`

## Description
* `0-add.py` imports the function `def add(a, b):` from the file `add_0.py1` and prints the result of the addition `1 + 2 = 3`
* `1-calculation.py`  imports functions from the file `calculator_1.py`, does some Maths, and prints the result.
* `2-args.py`prints the number of and the list of its arguments.
* `3-infinite_add.py` prints the result of the addition of all arguments
* `4-hidden_discovery.py` prints all the names defined by the compiled module `hidden_4.pyc`.
* `5-variable_load.py` imports the variable `a` from the file `variable_load_5.py` and prints its value.
* `100-my_calculator.py`  imports all functions from the file `calculator_1.py` and handles basic operations.
  * Usage: `./100-my_calculator.py a operator b`
  * If the number of arguments is not 3, the program:
    * prints `Usage: ./100-my_calculator.py <a> <operator> <b>` followed with a new line
    * exits with the value `1`
  * `operator` can be:
    * `+` for addition
    * `-` for subtraction
    * `*` for multiplication
    * `/` for division
  * If the operator is not one of the above:
    * it prints `Unknown operator. Available operators: +, -, * and /` followed with a new line
    * exits with the value `1`
  * The result is printed like this: `<a> <operator> <b> = <result>`, followed by a new line

* `101-easy_print.py` prints `#pythoniscool`, followed by a new line, in the standard output.
* `102-magic_calculation.py` is a Python function that does exactly the same as the following Python bytecode:
  ```
   3           0 LOAD_CONST               1 (0)
               3 LOAD_CONST               2 (('add', 'sub'))
               6 IMPORT_NAME              0 (magic_calculation_102)
               9 IMPORT_FROM              1 (add)
              12 STORE_FAST               2 (add)
              15 IMPORT_FROM              2 (sub)
              18 STORE_FAST               3 (sub)
              21 POP_TOP

   4          22 LOAD_FAST                0 (a)
              25 LOAD_FAST                1 (b)
              28 COMPARE_OP               0 (<)
              31 POP_JUMP_IF_FALSE       94

   5          34 LOAD_FAST                2 (add)
              37 LOAD_FAST                0 (a)
              40 LOAD_FAST                1 (b)
              43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
              46 STORE_FAST               4 (c)

   6          49 SETUP_LOOP              38 (to 90)
              52 LOAD_GLOBAL              3 (range)
              55 LOAD_CONST               3 (4)
              58 LOAD_CONST               4 (6)
              61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
              64 GET_ITER
         >>   65 FOR_ITER                21 (to 89)
              68 STORE_FAST               5 (i)

   7          71 LOAD_FAST                2 (add)
              74 LOAD_FAST                4 (c)
              77 LOAD_FAST                5 (i)
              80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
              83 STORE_FAST               4 (c)
              86 JUMP_ABSOLUTE           65
         >>   89 POP_BLOCK

   8     >>   90 LOAD_FAST                4 (c)
              93 RETURN_VALUE
 
  10     >>   94 LOAD_FAST                3 (sub)
              97 LOAD_FAST                0 (a)
             100 LOAD_FAST                1 (b)
             103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             106 RETURN_VALUE
             107 LOAD_CONST               0 (None)
             110 RETURN_VALUE
  

* `103-fast_alphabet.py` prints the alphabet in uppercase, followed by a new line.
