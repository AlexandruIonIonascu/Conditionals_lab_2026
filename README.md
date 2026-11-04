# Conditionals lab 2026

Recap, individual conditionals, Copilot practice and homework.

## Recap

Six exercises in increasing difficulty. Allow about **30 minutes**.

### R1. [Concatenate a name](recap/01_variables.py)

Read: [String concatenation — joining strings and adding a space](https://www.w3schools.com/python/python_strings_concatenate.asp)
and [Variables — assigning values](https://www.w3schools.com/python/python_variables.asp).

With strings, `+` joins text. It does **not** insert spaces automatically.
Build a full name from two variables, rather than repeating a finished
string in `print()`.

1. Store `Ada` and `Lovelace` in separate variables.
2. Join the values with one space between them and store the full name.
3. Print the full name with the label `Full name:`.
4. Change just the first name to `Grace`; the output should use the new value.

Expected output for the original values:

```text
Full name: Ada Lovelace
```

### R2. [Build an address from input](recap/02_input.py)

Read: [User input — prompts and storing replies](https://www.w3schools.com/python/python_user_input.asp)
and [String concatenation](https://www.w3schools.com/python/python_strings_concatenate.asp).

Reuse concatenation with values supplied by the user. Keep the username
and domain in separate variables and insert the `@` character between them.
Use fictional details for this exercise.

1. Read a username and a domain using two `input()` calls.
2. Build and store the address with `+`.
3. Display it with the label `Address:`.
4. Rerun with `alex` and `example.net`; expect `alex@example.net`.

Sample transcript:

```text
Username: ada
Domain: example.org
Address: ada@example.org
```

### R3. [Add two numeric inputs](recap/03_integer_input.py)

Read: [User input — numeric input](https://www.w3schools.com/python/python_user_input.asp),
[Casting — int()](https://www.w3schools.com/python/python_casting.asp)
and [Arithmetic operators — addition](https://www.w3schools.com/python/python_operators_arithmetic.asp).

Digits read with `input()` are still text. The same `+` operator that joined
text in R1–R2 must now add numbers. Convert the values before calculating.

1. Read two whole numbers and convert each answer with `int()`.
2. Calculate their sum, store it in `total` and display it.
3. Check `3` and `7` → `10`, then `-2` and `5` → `3`.
4. If you get `37` or `-25`, inspect the values with `type()`.

Sample transcript:

```text
First number: 3
Second number: 7
Sum: 10
```

### R4. [Fix the total](recap/04_decimal_input.py)

Read: [Casting — int() and float()](https://www.w3schools.com/python/python_casting.asp),
[Data types — checking with type()](https://www.w3schools.com/python/python_datatypes.asp)
and [Arithmetic operators — multiplication](https://www.w3schools.com/python/python_operators_arithmetic.asp).

The supplied program runs, but its calculation is wrong. Repair the
existing code so that a decimal unit price and a whole-number quantity
produce the correct total.

1. Predict what the starter prints for `2.5` and `4`, then run it.
2. Inspect the types of the two input values.
3. Choose the conversion needed for each value and correct the arithmetic
   operator. Keep the prompts and the output label.
4. Rerun the sample, then try price `1.25` and quantity `2` → `2.5`.

Expected transcript **after fixing the code**:

```text
Unit price: 2.5
Quantity: 4
Total: 10.0
```

Be ready to explain both the conversion changes and the arithmetic change.

### R5. [Minutes left over](recap/05_minutes.py)

Read: [Arithmetic operators — modulus (%)](https://www.w3schools.com/python/python_operators_arithmetic.asp)
and [Casting — int()](https://www.w3schools.com/python/python_casting.asp).

The `%` operator gives the remainder of a division. With 60 minutes per
hour, use it to find the minutes left over after removing complete hours.

1. Read a nonnegative total number of minutes and convert it to `int`.
2. Calculate the remaining minutes using `%` and display them with the
   label `Minutes:`.

Check `59` → `59`, `60` → `0`, `135` → `15` and `0` → `0`.

Sample transcript:

```text
Total minutes: 135
Minutes: 15
```

### R6. [Print a receipt with f-strings](recap/06_fstrings.py)

Read: [Format strings — f-strings, placeholders and decimal formatting](https://www.w3schools.com/python/python_strings_format.asp)
and [Casting](https://www.w3schools.com/python/python_casting.asp).

Combine the earlier input and calculation skills with formatted output.
An f-string starts with `f` before the quote and places values inside
`{...}`. A format such as `{value:.2f}` displays a number with two decimal
places; it changes its display, not the value used in the calculation.

1. Read the item name, a whole-number quantity and a decimal unit price.
2. Keep the item as text, convert the numeric answers and calculate the total.
3. Use an f-string to produce the receipt line below. Display both the unit
   price and total with exactly two decimal places.
4. Test again with `Notebook`, `1` and `12.75`; expect
   `1 x Notebook at 12.75 lei = 12.75 lei`.
   With quantity `0`, the total must display as `0.00`.

Sample transcript:

```text
Item: Pen
Quantity: 4
Unit price: 2.5
4 x Pen at 2.50 lei = 10.00 lei
```

## Part 1

Work independently for about **45 minutes**. Start with exercises 1–3,
then attempt 4 if time allows. Continue unfinished work next lab.

Remember: `=` assigns a value and `==` compares values. End `if`, `elif`
and `else` lines with `:` and indent their blocks with four spaces.
Separate `if` statements can all run; an `if/elif/else` chain selects
only the first matching branch.

### 1. [Orwell](Part1/1_Orwell.py)

Read: [If — conditions and indentation](https://www.w3schools.com/python/python_conditions.asp)
and [Comparison operators — equality](https://www.w3schools.com/python/python_operators_comparison.asp).

Use a single condition to decide whether to print a message. Read an integer
and print `Orwell` only when it equals `1984`. For other inputs, the input
prompt still appears, but no result message should follow.

Check `1983`, `1984` and `1985`; only the middle case prints the message.

Sample transcripts:

```text
Please type in a number: 2020
```

```text
Please type in a number: 1984
Orwell
```

### 2. [Absolute value](Part1/2_Absolute.py)

Read: [If](https://www.w3schools.com/python/python_conditions.asp)
and [Else — the alternative branch](https://www.w3schools.com/python/python_if_else.asp).

The absolute value is a number's distance from zero. Read an integer and
use a condition to change a negative value to its opposite; keep zero
and positive values as they are. Display the result in the sample format.
Use conditions rather than `abs()`.

Check `-7`, `0` and `7`, including the case where the value does not change.

Sample transcripts:

```text
Please type in a number: -7
The absolute value of this number is 7
```

```text
Please type in a number: 1
The absolute value of this number is 1
```

```text
Please type in a number: -99
The absolute value of this number is 99
```

### 3. [Order of magnitude](Part1/3_Order.py)

Read: [If — when a block runs](https://www.w3schools.com/python/python_conditions.asp)
and [Comparison operators — less than](https://www.w3schools.com/python/python_operators_comparison.asp).

Several conditions can be true for the same number. Read an integer and
print **every** applicable size message, in the order shown below.
Always print `Thank you!` once at the end.

Check `9`, `10`, `99`, `100`, `999` and `1000`.
Consider why one exclusive `if/elif/else` chain would miss some messages.

Sample transcripts:

```text
Please type in a number: 950
This number is smaller than 1000
Thank you!
```

```text
Please type in a number: 59
This number is smaller than 1000
This number is smaller than 100
Thank you!
```

```text
Please type in a number: 2
This number is smaller than 1000
This number is smaller than 100
This number is smaller than 10
Thank you!
```

```text
Please type in a number: 1123
Thank you!
```

### 4. [Calculator](Part1/4_Calculator.py)

Read: [Elif — choosing among alternatives](https://www.w3schools.com/python/python_if_elif.asp)
and [Arithmetic operators](https://www.w3schools.com/python/python_operators_arithmetic.asp).

Choose a calculation by comparing text. Read two integers and an operation:
`add`, `multiply` or `subtract`. Calculate and display the corresponding
result in the format shown below. An unsupported operation should
produce no calculation or error message. Do not use `eval()`.

Test each supported operation and then `divide`. Keep the numbers numeric
and the operation as text.

Sample transcripts:

```text
Number 1: 10
Number 2: 17
Operation: add

10 + 17 = 27
```

```text
Number 1: 4
Number 2: 6
Operation: multiply

4 * 6 = 24
```

```text
Number 1: 4
Number 2: 6
Operation: subtract

4 - 6 = -2
```

## Part 2

Use Copilot for hints and explanations, then edit and test the Python file.
Be ready to explain the code you keep.

### 5. [Repair the syntax](Part2_Copilot/5_Sintax.py)

Read: [If — syntax and indentation](https://www.w3schools.com/python/python_conditions.asp),
[Casting](https://www.w3schools.com/python/python_casting.asp)
and [print() — combining text and numbers](https://www.w3schools.com/python/ref_func_print.asp).

The supplied program is **intentionally broken**. Ask Copilot to identify
the syntax and type errors, then fix them in place. Check the colons,
indentation, quotation marks, numeric conversion, reassignment and output.

Test `13`, `100` and `101`. Subtract 100 once only when the original
number is greater than 100. The lucky-number and farewell lines must
appear for every input.

Sample transcripts:

```text
Please type in a number: 13
13 must be my lucky number!
Have a nice day!
```

```text
Please type in a number: 101
The number was greater than one hundred
Now its value has decreased by one hundred
Its value is now 1
1 must be my lucky number!
Have a nice day!
```

### 6. [Age](Part2_Copilot/6_Age.py)

Read: [Else — two alternatives](https://www.w3schools.com/python/python_if_else.asp)
and [Comparison operators — greater than or equal](https://www.w3schools.com/python/python_operators_comparison.asp).

Use two alternative branches to decide which message to print.
Read an integer age and use **18** as the age of maturity.

Check `17`, `18` and `19`; the boundary value belongs to the adult case.

Sample transcripts:

```text
How old are you? 12
You are not of age!
```

```text
How old are you? 32
You are of age!
```

### 7. [The greater number](Part2_Copilot/7_Greater.py)

Read: [Elif — multiple outcomes](https://www.w3schools.com/python/python_if_elif.asp)
and [Comparison operators](https://www.w3schools.com/python/python_operators_comparison.asp).

There are three possible outcomes: the first number is greater, the second
is greater, or they are equal. Read two integers and display the required
message for each outcome. Use conditions rather than `max()`.

Run all three samples below, then try `-2` and `-5`, and `0` and `0`.

Sample transcripts:

```text
Please type in the first number: 5
Please type in another number: 3
The greater number was: 5
```

```text
Please type in the first number: 5
Please type in another number: 8
The greater number was: 8
```

```text
Please type in the first number: 5
Please type in another number: 5
The numbers are equal!
```

### 8. [The elder person](Part2_Copilot/8_Elder.py)

Read: [User input](https://www.w3schools.com/python/python_user_input.asp),
[Casting](https://www.w3schools.com/python/python_casting.asp)
and [Elif](https://www.w3schools.com/python/python_if_elif.asp).

Combine text and numeric inputs. Keep the two names as strings and convert
the two ages to integers, using separate variables. Compare the ages and
print the elder person's name, or the equal-age message.

Test the first person being older, the second being older and equal ages.
Check that the displayed name still belongs to the correct age.

Sample transcripts:

```text
Person 1:
Name: Alan
Age: 26
Person 2:
Name: Ada
Age: 27
The elder is Ada
```

```text
Person 1:
Name: Bill
Age: 1
Person 2:
Name: Jean
Age: 1
Bill and Jean are the same age
```

### 9. [Check an age](Part2_Copilot/9_Check.py)

Read: [Elif — the first matching branch](https://www.w3schools.com/python/python_if_elif.asp)
and [Comparison operators](https://www.w3schools.com/python/python_operators_comparison.asp).

The order of conditions matters when ranges overlap. Read an integer age
and use the exact rules below:

| Age | Message |
| --- | --- |
| Below 0 | `That must be a mistake` |
| 0 through 4 | `I suspect you can't write quite yet...` |
| 5 or more | `Ok, you're <age> years old`, replacing `<age>` with the input |

Test `-1`, `0`, `4` and `5`. For this task, do not add an upper-age limit.

Sample transcripts:

```text
What is your age? 13
Ok, you're 13 years old
```

```text
What is your age? 2
I suspect you can't write quite yet...
```

```text
What is your age? -4
That must be a mistake
```

## Part 3: Homework

Write your own solution and follow the instructor's deadline.

### 10. [Grading](Part3_Homework/10_Grading.py)

Read: [Elif — ordering several branches](https://www.w3schools.com/python/python_if_elif.asp)
and [Comparison operators — inclusive boundaries](https://www.w3schools.com/python/python_operators_comparison.asp).

Read a whole-number score from 0 to 100 and use ordered conditions to
choose its letter grade. No input validation is required. Print the letter
after the input prompt.

| Score | Grade |
| --- | --- |
| 90–100 | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| 0–59 | F |

Check `59/60`, `69/70`, `79/80` and `89/90`, then the endpoints
`0` and `100`. Each score must produce exactly one grade.

Sample transcript:

```text
Score: 85
B
```
