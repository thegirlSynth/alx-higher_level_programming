# Python - if/else, loops, functions

## Prototypes
`def islower(c):`

`def uppercase(str):`

`def print_last_digit(number):`

`def add(a, b):`

`def pow(a, b):`

`def fizzbuzz():`

`def remove_char_at(str, n):`

`def magic_calculation(a, b, c):`

`listint_t *insert_node(listint_t **head, int number);`

## Description
* `0-positive_or_negative.py` assigns a random signed number to the variable `number` each time it is executed.
It prints whether the number stored in the variable `number` is positive or negative.

* `1-last_digit.py` assigns a random signed number to the variable `number` each time it is executed.
It prints the last digit of the number stored in the variable `number`.

* `2-print_alphabet.py` prints the ASCII alphabet, in lowercase, not followed by a new line.

* `3-print_alphabt.py` prints the ASCII alphabet, in lowercase, not followed by a new line, except `q` and `e`

* `4-print_hexa.py` prints all numbers from `0` to `98` in decimal and in hexadecimal (as in the following example)
  ```
   0 = 0x0
   1 = 0x1
   2 = 0x2
   3 = 0x3
   4 = 0x4
   5 = 0x5
   6 = 0x6
   7 = 0x7
   8 = 0x8
   9 = 0x9
  10 = 0xa
    ...
  
* `5-print_comb2.py` prints numbers from `0` to `99`.
  * Numbers are separated by `,`, followed by a space
  * Numbers are printed in ascending order, with two digits
  * The last number is followed by a new line

* `6-print_comb3.py` prints all possible different combinations of two digits.
  * Numbers are separated by `,`, followed by a space
  * The two digits are different and only the smallest combination of two digits is printed.
  * `01` and `10` are considered the same combination of the two digits `0` and `1`
  * The last number is followed by a new line

* `7-islower.py` checks for lowercase character.
  * Returns `True` if `c` is lowercase
  * Returns `False` otherwise

* `8-uppercase.py` prints a string in uppercase followed by a new line.

* `9-print_last_digit.py` prints the last digit of a number.

* `10-add.py` adds two integers and returns the result.

* `11-pow.py` computes `a` to the power of `b` and return the value.

* `12-fizzbuzz.py` prints the numbers from `1` to `100` separated by a space.
  * For multiples of three, `Fizz` is printed instead of the number and for multiples of five `Buzz` is printed.
  * For numbers which are multiples of both three and five `FizzBuzz` is printed.

* `13-insert_number.c` is  a function in C that inserts a number into a sorted singly linked list.

* `100-print_tebahpla.py` prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (`z`in lowercase and `Y` in uppercase) , not followed by a new line.

* `101-remove_char_at.py` creates a copy of the string, removing the character at the position `n` (not the Python way, the “C array index”).

* `102-magic_calculation.py` is a Python function that does exactly the same as the following Python bytecode:
  ```
  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE

     ``` 

* `lists.h` is the header file for [13-insert_number.c](./13-insert_number.c).
