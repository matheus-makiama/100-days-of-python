# Day 02 — Data Types, Math & String Formatting

> **Course:** 100 Days of Code — The Complete Python Pro Bootcamp (Angela Yu)
> **Date:** April 23, 2026
> **Topics:** Data types, type conversion, math operators, `round()`, f-strings, augmented assignment

---

## Table of Contents
- [The Four Core Data Types](#the-four-core-data-types)
- [Checking Types](#checking-types)
- [String Indexing](#string-indexing)
- [Type Conversion](#type-conversion)
- [Math Operators](#math-operators)
- [Operator Precedence](#operator-precedence)
- [round()](#round)
- [Augmented Assignment](#augmented-assignment)
- [f-strings](#f-strings)
- [Project — BMI Calculator](#project--bmi-calculator)
- [Project — Life in Weeks](#project--life-in-weeks)
- [Key Rules](#key-rules)

---

## The Four Core Data Types

| Type | Keyword | Example | Notes |
|------|---------|---------|-------|
| String | `str` | `"hello"` | Text — always in quotes |
| Integer | `int` | `42` | Whole numbers, no decimal |
| Float | `float` | `3.14` | Numbers with a decimal point |
| Boolean | `bool` | `True` / `False` | Exactly two values, capital first letter |

---

## Checking Types

```python
print(type("hello"))   # <class 'str'>
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type(True))      # <class 'bool'>
```

Useful when a variable behaves unexpectedly — check what type it actually is.

---

## String Indexing

Strings are sequences. Each character has a numbered position starting from `0`.

```python
word = "hello"
#       01234    (positive indexes)
#      -54321    (negative indexes)

word[0]    # → "h"  (first character)
word[4]    # → "o"  (last character)
word[-1]   # → "o"  (last character, counting from the end)
word[-2]   # → "l"  (second to last)
```

> Negative indexes let you access the end of a string without knowing its length.

---

## Type Conversion

Type conversion functions **return** a new value — they don't modify the original. You must assign the result back.

```python
number = "123"        # this is a string
number = int(number)  # now it's an integer
```

| Function | Converts to | Example |
|----------|-------------|---------|
| `int(x)` | Integer | `int("42")` → `42` |
| `float(x)` | Float | `float("3.14")` → `3.14` |
| `str(x)` | String | `str(42)` → `"42"` |
| `bool(x)` | Boolean | `bool(0)` → `False`, `bool(1)` → `True` |

### Why this matters

```python
age = input("How old are you? ")   # input() returns "25" (string)

# This crashes:
print(age + 1)                     # TypeError: can't add str and int

# This works:
age = int(input("How old are you? "))
print(age + 1)                     # → 26
```

```python
# You also can't mix str and int in concatenation:
print("My age is " + 25)           # TypeError
print("My age is " + str(25))      # works → "My age is 25"
print(f"My age is {25}")           # works (f-string, covered below)
```

---

## Math Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `+` | Addition | `3 + 2` | `5` |
| `-` | Subtraction | `7 - 3` | `4` |
| `*` | Multiplication | `4 * 3` | `12` |
| `/` | Division | `7 / 2` | `3.5` |
| `//` | Floor division (round down) | `7 // 2` | `3` |
| `**` | Exponent (power) | `2 ** 3` | `8` |
| `%` | Modulo (remainder) | `10 % 3` | `1` |

### The `/` always returns float rule

In Python 3, regular division **always** returns a float, even when the result is a whole number:

```python
6 / 3     # → 2.0  (float, not 2)
10 / 2    # → 5.0
```

Use `//` (floor division) if you want an integer result:

```python
7 // 2      # → 3   (int)
7.0 // 2    # → 3.0 (float — one input was float, so output is float)
-7 // 2     # → -4  (rounds DOWN, toward negative infinity — not toward zero)
```

> Floor division always rounds **down**, not toward zero. `-7 // 2` is `-4`, not `-3`.

---

## Operator Precedence

Python follows the same order as math (PEMDAS):

1. `()` — Parentheses — evaluated first
2. `**` — Exponents
3. `*` `/` `//` `%` — Multiplication, division, floor division, modulo
4. `+` `-` — Addition, subtraction

Within the same level: **left to right**.

```python
2 + 3 * 4      # → 14  (* before +)
(2 + 3) * 4    # → 20  (parentheses first)
2 ** 3 ** 2    # → 512  (** is right-to-left: 3**2=9, then 2**9=512)
```

> Don't trust head-math on complex expressions. Run the code and verify.

---

## `round()`

Rounds a number to a given number of decimal places.

```python
round(3.14159)      # → 3      (rounds to nearest integer)
round(3.14159, 2)   # → 3.14   (rounds to 2 decimal places)
round(3.14159, 4)   # → 3.1416
```

### Banker's rounding (Python's behavior at exactly 0.5)

Python doesn't always round 0.5 up. It rounds to the **nearest even number**:

```python
round(0.5)   # → 0  (0 is even)
round(1.5)   # → 2  (2 is even)
round(2.5)   # → 2  (2 is even)
round(3.5)   # → 4  (4 is even)
```

This is called **banker's rounding**. It's rare to run into it, but it exists.

---

## Augmented Assignment

Shorthand for "apply an operation and store the result back into the same variable."

```python
score = 0
score += 1    # same as: score = score + 1
score -= 5    # same as: score = score - 5
score *= 2    # same as: score = score * 2
score /= 4    # same as: score = score / 4
```

Full set: `+=` `-=` `*=` `/=` `//=` `%=` `**=`

---

## f-strings

The modern, clean way to embed variables inside strings.

```python
name = "Angela"
age = 25
height = 1.65

# Old way — clunky, error-prone
print("Name: " + name + ", Age: " + str(age))

# f-string — prefix with f, variables go inside {}
print(f"Name: {name}, Age: {age}, Height: {height}")
```

- Any type works inside `{}` — no `str()` conversion needed.
- You can put expressions inside the braces: `f"Next year I'll be {age + 1}"`
- You can format numbers: `f"{3.14159:.2f}"` → `"3.14"`

---

## Project — BMI Calculator

BMI = weight (kg) / height (m)²

```python
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / height ** 2, 2)
print(f"Your BMI is {bmi}")
```

**What this exercises:**
- `float()` conversion on input
- Math operators (`/` and `**`)
- `round()` to clean up the result
- f-string to format the output

---

## Project — Life in Weeks

Given your age, calculate how many weeks, days, and months you might have left (assuming 90-year lifespan).

```python
age = int(input("What is your current age? "))
years_left = 90 - age

months = years_left * 12
weeks = years_left * 52
days = years_left * 365

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
```

---

## Key Rules

| Rule | Why it matters |
|------|---------------|
| `/` always returns float | `6 / 3` is `2.0`, not `2` |
| `//` rounds toward negative infinity | `-7 // 2` is `-4`, not `-3` |
| `input()` always returns string | Convert before math |
| Type conversion is return-and-reassign | `int(x)` doesn't change `x` — you must write `x = int(x)` |
| f-strings are the modern standard | Prefer over `str()` + concatenation |
| Don't trust head-math | Run the code to verify |

---

*Day 2 of 100 — April 2026*
