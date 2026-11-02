# Conditionals lab 2026

Work through this guide in order: recap, Part 1, Part 2, then homework.
Each exercise has a separate Python file containing the full task and sample
output. Open the file linked in its heading, then use the W3Schools links
for the concepts you need.

## How to work

1. Open your assignment repository in Codespaces or your Python editor.
2. Read the exercise, identify its inputs and choose the type of each value.
   `input()` returns text; convert numeric answers with `int()` or `float()`.
3. Write your solution below `YOUR CODE` or `Write your code here`, keeping
   the task comments. For exercise 5, repair the supplied code instead.
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
Use `if` statements for the conditionals exercises.

## Recap

Allow about **30 minutes**: 5 + 5 + 8 + 8 minutes for the four exercises,
then 4 minutes to review. Start here even if you did not finish the
[variables lab](https://github.com/AlexandruIonIonascu/Variables_lab_2026)
or its homework. Write these solutions yourself and ask the instructor
when stuck. You only need variables, input, output and simple arithmetic.

### R1. [Variables and reassignment](recap/01_variables.py)

A variable gives a name to a stored value. Practise creating variables,
displaying their values and assigning a new value to an existing name.

1. Store the fictional name and exercise count in separate variables.
2. Print the values with the required labels.
3. Change the count and print it again. Change the initial name and rerun
   to check that the output uses the variable.

Read: [Variables — creating and assigning values](https://www.w3schools.com/python/python_variables.asp)
and [print() — displaying labels and values](https://www.w3schools.com/python/ref_func_print.asp).

### R2. [Read and store text](recap/02_input.py)

`input()` waits for an answer and returns it as text. Keep each answer
in its own variable so that a later input does not overwrite an earlier one.

1. Ask for a fictional name and favourite subject.
2. Store the two answers separately and display both.
3. Rerun with different answers and check that both output lines change.

Read: [User input — prompts and storing replies](https://www.w3schools.com/python/python_user_input.asp).

### R3. [Add two numeric inputs](recap/03_integer_input.py)

Digits read with `input()` are still text. Convert each answer to `int`
before adding; otherwise `+` joins strings instead of adding numbers.

1. Read two whole numbers and convert both with `int()`.
2. Store their sum and print it with the label `Sum:`.
3. Check `3` and `7` → `10`, then `-2` and `5` → `3`.

Read: [User input — numeric input](https://www.w3schools.com/python/python_user_input.asp),
[Casting — int()](https://www.w3schools.com/python/python_casting.asp)
and [Arithmetic operators — addition](https://www.w3schools.com/python/python_operators_arithmetic.asp).

### R4. [A price and a quantity](recap/04_decimal_input.py)

Use `float` for a decimal price and `int` for a whole-number quantity.
This exercise connects reading input, choosing types and doing a calculation.

1. Read and convert the price and quantity, keeping both values.
2. Multiply them, store the total and display it.
3. Temporarily use `type()` to check the conversions. Remove the diagnostic
   output when comparing with the sample.
4. Check `2.5 × 4` → `10.0` and `1.25 × 2` → `2.5`.

Read: [Casting — int() and float()](https://www.w3schools.com/python/python_casting.asp),
[Data types — inspecting types](https://www.w3schools.com/python/python_datatypes.asp)
and [Arithmetic operators — multiplication](https://www.w3schools.com/python/python_operators_arithmetic.asp).

**Recap check:** explain what each variable stores, why `input()` returns
text and why the price needs `float()`. You can display text and numbers
together using commas in `print()`; f-strings are not required.

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

Read: [If — conditions and indentation](https://www.w3schools.com/python/python_conditions.asp)
and [Comparison operators — equality](https://www.w3schools.com/python/python_operators_comparison.asp).

### 2. [Absolute value](Part1/2_Absolute.py)

The absolute value is a number's distance from zero. Read an integer and
use a condition to change a negative value to its opposite; keep zero
and positive values as they are. Display the result in the sample format.
Use conditions rather than `abs()`.

Check `-7`, `0` and `7`, including the case where the value does not change.

Read: [If](https://www.w3schools.com/python/python_conditions.asp)
and [Else — the alternative branch](https://www.w3schools.com/python/python_if_else.asp).

### 3. [Order of magnitude](Part1/3_Order.py)

Several conditions can be true for the same number. Read an integer and
print **every** applicable size message, in the order shown in the file.
Always print `Thank you!` once at the end.

Check `9`, `10`, `99`, `100`, `999` and `1000`.
Consider why one exclusive `if/elif/else` chain would miss some messages.

Read: [If — when a block runs](https://www.w3schools.com/python/python_conditions.asp)
and [Comparison operators — less than](https://www.w3schools.com/python/python_operators_comparison.asp).

### 4. [Calculator](Part1/4_Calculator.py)

Choose a calculation by comparing text. Read two integers and an operation:
`add`, `multiply` or `subtract`. Calculate and display the corresponding
result in the format shown in the file. An unsupported operation should
produce no calculation or error message. Do not use `eval()`.

Test each supported operation and then `divide`. Keep the numbers numeric
and the operation as text.

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

Read: [If — syntax and indentation](https://www.w3schools.com/python/python_conditions.asp),
[Casting](https://www.w3schools.com/python/python_casting.asp)
and [print() — combining text and numbers](https://www.w3schools.com/python/ref_func_print.asp).

### 6. [Age](Part2_Copilot/6_Age.py)

Use two alternative branches to decide which message to print.
Read an integer age and use **18** as the age of maturity.

Check `17`, `18` and `19`; the boundary value belongs to the adult case.

Read: [Else — two alternatives](https://www.w3schools.com/python/python_if_else.asp)
and [Comparison operators — greater than or equal](https://www.w3schools.com/python/python_operators_comparison.asp).

### 7. [The greater number](Part2_Copilot/7_Greater.py)

There are three possible outcomes: the first number is greater, the second
is greater, or they are equal. Read two integers and display the required
message for each outcome. Use conditions rather than `max()`.

Run all three samples, then try `-2` and `-5`, and `0` and `0`.

Read: [Elif — multiple outcomes](https://www.w3schools.com/python/python_if_elif.asp)
and [Comparison operators](https://www.w3schools.com/python/python_operators_comparison.asp).

### 8. [The elder person](Part2_Copilot/8_Elder.py)

Combine text and numeric inputs. Keep the two names as strings and convert
the two ages to integers, using separate variables. Compare the ages and
print the elder person's name, or the equal-age message.

Test the first person being older, the second being older and equal ages.
Check that the displayed name still belongs to the correct age.

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
