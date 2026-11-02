# Conditionals lab 2026

Practise Python variables and input, then make decisions with `if`, `else`
and `elif`. Each exercise has its own file; the task and examples are comments.

## This lab: 90 minutes

| Time | Activity |
| --- | --- |
| 0–30 min | [Recap](recap/README.md): four short exercises on variables, input and casting, followed by a quick review. |
| 30–45 min | Instructor demo: conditions, comparisons, indentation, `else` and `elif`. |
| 45–90 min | [Part1](Part1/README.md): start exercises 1–3, then attempt 4 if time allows. |

Continue unfinished conditionals exercises next lab, then move to
[Part2_Copilot](Part2_Copilot/README2.md), exercises 5–9.
[Exercise 10](Part3_Homework/10_Grading.py) is further practice/homework;
follow the instructor's deadline. You do not need to finish all ten today.

## How to solve an exercise

1. Open your assignment repository in Codespaces or your Python editor.
   Start with `recap/01_variables.py`, then follow numerical order within each folder.
2. Read the task and relevant W3Schools sections below or in the file.
   Identify the inputs, their types and the expected output.
3. Write your solution below `YOUR CODE` or `Write your code here`, keeping
   the task comments. In exercise 5, repair the supplied code instead.
4. Save and run **only that file**, from the repository root:

   ```bash
   python recap/01_variables.py
   python Part1/1_Orwell.py
   ```

   Run one command at a time. Enter answers in the terminal and press **Enter**.
   Use a decimal point, such as `2.5`.
5. Compare with every sample and try the extra checks in the file. For a
   condition, test both outcomes and the boundary value. Calculate results
   from the inputs instead of printing fixed sample answers.
6. Save All → Source Control → stage your changed files (+) → enter a message
   → Commit → Push. Refresh your assignment repo on GitHub and verify the files.

Work independently in recap and Part1; ask the instructor when stuck.
Use Copilot in Part2 as instructed there, and explain the code you keep.
Assume correctly typed numeric inputs; exception handling is not required.
Use `if` statements for the conditionals exercises.

## Demo: 15 minutes

Use a temperature example: read an integer and add an `if` (4 min), add
`else` (3 min), then `elif` for a third outcome (4 min).
Test values below, at and above a threshold (4 min). Highlight `=` versus
`==`, `:`, four-space indentation and code outside the conditional block.
Compare separate `if` statements with a single `if/elif/else` chain.

## W3Schools support

| Topic | Read for this lab |
| --- | --- |
| [Variables](https://www.w3schools.com/python/python_variables.asp) and [Data types](https://www.w3schools.com/python/python_datatypes.asp) | Assignment, reassignment, `str`, `int`, `float`, `type()`. |
| [User input](https://www.w3schools.com/python/python_user_input.asp) and [Casting](https://www.w3schools.com/python/python_casting.asp) | `input()` returns text; convert numeric inputs with `int()` or `float()`. |
| [print()](https://www.w3schools.com/python/ref_func_print.asp) | Print labels and variables, using commas if needed. |
| [Arithmetic operators](https://www.w3schools.com/python/python_operators_arithmetic.asp) | `+`, `-`, `*`. |
| [Comparison operators](https://www.w3schools.com/python/python_operators_comparison.asp) | `==`, `!=`, `<`, `<=`, `>`, `>=`. |
| [If](https://www.w3schools.com/python/python_conditions.asp), [Else](https://www.w3schools.com/python/python_if_else.asp) and [Elif](https://www.w3schools.com/python/python_if_elif.asp) | Conditions, indentation, alternative branches and their order. |

Exercises 1–10 are adapted from the [previous conditionals lab](https://github.com/AlexandruIonascu33/Conditionals).
The recap revisits the [variables lab](https://github.com/AlexandruIonIonascu/Variables_lab_2026);
it does not require completed homework.
