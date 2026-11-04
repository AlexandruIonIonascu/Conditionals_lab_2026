# Conditionals lab 2026

Work through this guide in order: recap, Part 1, Part 2, then homework.
Each Python file contains the task and, where needed, starter code.
This guide contains the explanations, working steps, examples and reading
links. Open each file from its exercise heading below.

## How to work

1. Open your assignment repository in Codespaces or your Python editor.
2. Read the exercise, identify its inputs and choose the type of each value.
   `input()` returns text; convert numeric answers with `int()` or `float()`.
3. Write your solution below the task comments. In recap R4 and conditionals
   exercise 5, repair the supplied code in place.
4. Save and run **one file at a time**, from the repository root. For example:

   ```bash
   python recap/01_variables.py
   ```

   For the first conditionals exercise, run:

   ```bash
   python Part1/1_Orwell.py
   ```

5. Type answers in the terminal and press **Enter**. Use a decimal point,
   such as `2.5`.
6. Compare your result with every sample. Try the additional checks below;
   for a condition, test both outcomes and the boundary value.
7. Save and submit your progress using the steps at the end of this guide.

Assume correctly typed numeric inputs; exception handling is not required.
Calculate results from the inputs rather than printing fixed sample answers.
Use `if` statements for the conditionals exercises. Inputs used as quantities,
prices or durations in the recap are nonnegative.

## Recap

Allow about **30 minutes**. The exercises gradually combine more concepts:
start with text, add input and numeric conversion, repair a program, then
use new arithmetic operators and formatted output. Work independently and
ask the instructor when stuck. No `if` statements or loops are needed here.

| Exercise | New practice | Suggested time |
| --- | --- | --- |
| R1 | Join strings with `+` and include spaces | 3 min |
| R2 | Combine two text inputs into an address | 4 min |
| R3 | Convert text to integers before adding | 5 min |
| R4 | Find and fix conversion and arithmetic mistakes | 5 min |
| R5 | Use `//` and `%` to split a duration | 5 min |
| R6 | Combine inputs, calculations and f-string formatting | 6 min |

Use the remaining 2 minutes to review the types and explain one mistake.
This recap does not require completed homework from the
[variables lab](https://github.com/AlexandruIonIonascu/Variables_lab_2026).

### R1. [Concatenate a name](recap/01_variables.py)

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

Read: [String concatenation — joining strings and adding a space](https://www.w3schools.com/python/python_strings_concatenate.asp)
and [Variables — assigning values](https://www.w3schools.com/python/python_variables.asp).

### R2. [Build an address from input](recap/02_input.py)

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

Read: [User input — prompts and storing replies](https://www.w3schools.com/python/python_user_input.asp)
and [String concatenation](https://www.w3schools.com/python/python_strings_concatenate.asp).

### R3. [Add two numeric inputs](recap/03_integer_input.py)

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

Read: [User input — numeric input](https://www.w3schools.com/python/python_user_input.asp),
[Casting — int()](https://www.w3schools.com/python/python_casting.asp)
and [Arithmetic operators — addition](https://www.w3schools.com/python/python_operators_arithmetic.asp).

### R4. [Fix the total](recap/04_decimal_input.py)

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

Read: [Casting — int() and float()](https://www.w3schools.com/python/python_casting.asp),
[Data types — checking with type()](https://www.w3schools.com/python/python_datatypes.asp)
and [Arithmetic operators — multiplication](https://www.w3schools.com/python/python_operators_arithmetic.asp).

### R5. [Split minutes into hours and minutes](recap/05_minutes.py)

For nonnegative integers, `//` gives the number of complete groups and
`%` gives the remainder. These operators let you split a duration without
a loop. Ordinary `/` gives a division result that can include a fraction.

1. Read a nonnegative total number of minutes and convert it to `int`.
2. Calculate the complete hours and the minutes left over, using 60 minutes
   per hour. Store the two results separately.
3. Display the results with the labels `Hours:` and `Minutes:`.
4. Check `59` → 0 hours and 59 minutes, `60` → 1 hour and 0 minutes,
   and `0` → 0 hours and 0 minutes.

Sample transcript:

```text
Total minutes: 135
Hours: 2
Minutes: 15
```

Read: [Arithmetic operators — floor division (//) and modulus (%)](https://www.w3schools.com/python/python_operators_arithmetic.asp)
and [Casting — int()](https://www.w3schools.com/python/python_casting.asp).

### R6. [Print a receipt with f-strings](recap/06_fstrings.py)

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

Read: [Format strings — f-strings, placeholders and decimal formatting](https://www.w3schools.com/python/python_strings_format.asp)
and [Casting](https://www.w3schools.com/python/python_casting.asp).

**Recap check:** explain why `+` joins strings but adds numbers, which
conversions R4 needed, how `//` differs from `%`, and what `:.2f` does.

## Part 1

Write these solutions yourself. Allow about **45 minutes**: start with
exercises 1–3, then attempt 4 if time allows. Continue unfinished work
in the next lab; you do not need to complete all ten conditionals exercises today.

Remember: `=` assigns a value and `==` compares values. End `if`, `elif`
and `else` lines with `:` and indent their blocks with four spaces.
Separate `if` statements can all run; an `if/elif/else` chain selects
only the first matching branch.

### 1. [Orwell](Part1/1_Orwell.py)

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

Read: [If — conditions and indentation](https://www.w3schools.com/python/python_conditions.asp)
and [Comparison operators — equality](https://www.w3schools.com/python/python_operators_comparison.asp).

### 2. [Absolute value](Part1/2_Absolute.py)

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

Read: [If](https://www.w3schools.com/python/python_conditions.asp)
and [Else — the alternative branch](https://www.w3schools.com/python/python_if_else.asp).

### 3. [Order of magnitude](Part1/3_Order.py)

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

Read: [If — when a block runs](https://www.w3schools.com/python/python_conditions.asp)
and [Comparison operators — less than](https://www.w3schools.com/python/python_operators_comparison.asp).

### 4. [Calculator](Part1/4_Calculator.py)

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

Read: [Elif — choosing among alternatives](https://www.w3schools.com/python/python_if_elif.asp)
and [Arithmetic operators](https://www.w3schools.com/python/python_operators_arithmetic.asp).

## Part 2

Continue here once Part 1 is complete, including in the next lab if needed.
Use **Copilot** to help you understand and improve your work:

1. Read the task, predict an output and make an initial attempt yourself.
2. Include the current file as context in Copilot Chat.
3. Ask for an explanation or a hint about one problem at a time.
4. Write or revise the code in the Python file and explain every change you keep.
5. Run all samples and additional checks. A reply in Chat alone does not
   complete an exercise.

### 5. [Repair the syntax](Part2_Copilot/5_Sintax.py)

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

Read: [If — syntax and indentation](https://www.w3schools.com/python/python_conditions.asp),
[Casting](https://www.w3schools.com/python/python_casting.asp)
and [print() — combining text and numbers](https://www.w3schools.com/python/ref_func_print.asp).

### 6. [Age](Part2_Copilot/6_Age.py)

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

Read: [Else — two alternatives](https://www.w3schools.com/python/python_if_else.asp)
and [Comparison operators — greater than or equal](https://www.w3schools.com/python/python_operators_comparison.asp).

### 7. [The greater number](Part2_Copilot/7_Greater.py)

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

Read: [Elif — multiple outcomes](https://www.w3schools.com/python/python_if_elif.asp)
and [Comparison operators](https://www.w3schools.com/python/python_operators_comparison.asp).

### 8. [The elder person](Part2_Copilot/8_Elder.py)

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

Read: [User input](https://www.w3schools.com/python/python_user_input.asp),
[Casting](https://www.w3schools.com/python/python_casting.asp)
and [Elif](https://www.w3schools.com/python/python_if_elif.asp).

### 9. [Check an age](Part2_Copilot/9_Check.py)

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

Read: [Elif — the first matching branch](https://www.w3schools.com/python/python_if_elif.asp)
and [Comparison operators](https://www.w3schools.com/python/python_operators_comparison.asp).

## Part 3: Homework

Start when you are ready and follow the instructor's deadline.
Attempt the solution yourself; you may ask Copilot for explanations or
hints, but write and explain your own code.

### 10. [Grading](Part3_Homework/10_Grading.py)

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

Read: [Elif — ordering several branches](https://www.w3schools.com/python/python_if_elif.asp)
and [Comparison operators — inclusive boundaries](https://www.w3schools.com/python/python_operators_comparison.asp).

## Save and submit

1. Click **File → Save All**.
2. Open **Source Control**, review the changes and stage the files with **+**.
3. Enter a short commit message and click **Commit**.
4. Choose **Push** from the Source Control menu.
5. Refresh your assignment repository on GitHub and open the changed files
   to confirm that your latest code was uploaded.

Repeat as you make progress, and verify your work on GitHub before stopping
your Codespace. Keep the existing exercise filenames and folders.

Exercises 1–10 are adapted from the
[previous conditionals lab](https://github.com/AlexandruIonascu33/Conditionals).
