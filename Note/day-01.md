# Day 01 — Output, Input & Variables

> **Course:** 100 Days of Code — The Complete Python Pro Bootcamp (Angela Yu)
> **Date:** April 21, 2026
> **Topics:** `print()`, `input()`, variables, `len()`, escape characters, debugging

---

## Table of Contents
- [print()](#print)
- [Escape Characters](#escape-characters)
- [input()](#input)
- [Variables](#variables)
- [len()](#len)
- [Comments](#comments)
- [Common Errors](#common-errors)
- [Project — Band Name Generator](#project--band-name-generator)
- [Key Rules](#key-rules)

---

## `print()`

Outputs text to the screen.

```python
print("Hello, World!")
print("Hello" + " " + "Angela")   # concatenation with +
```

**Things to know:**
- Python is case-sensitive. `print` works. `Print` throws a `NameError`.
- `+` joins strings together — this is called **concatenation**.
- Spaces don't appear automatically. Add them manually inside the string.

---

## Escape Characters

The backslash `\` tells Python: *"the next character means something special."*

| Sequence | Meaning |
|----------|---------|
| `\n` | New line |
| `\t` | Tab |
| `\\` | Literal backslash |
| `\"` | Literal double-quote inside a double-quoted string |
| `\'` | Literal apostrophe inside a single-quoted string |

```python
print("Line one\nLine two")
print("Name:\tAngela")
```

> **Note:** Backslash `\`, not forward slash `/`. On a Japanese keyboard, `\` is typed with the `¥` key.

---

## `input()`

Displays a prompt and waits for the user to type something.

```python
# Inline — works, but harder to read
print("Hello " + input("What is your name? ") + "!")

# Saved to a variable — cleaner
name = input("What is your name? ")
print("Hello " + name + "!")
```

**Critical rule: `input()` always returns a string.**

Even if the user types `25`, Python stores it as `"25"` (text), not `25` (number). You must convert it if you want to do math:

```python
age = int(input("How old are you? "))   # convert to int immediately
```

---

## Variables

A variable is a **label** attached to a value in memory — like a sticky note on an object.

```python
name = "Jack"       # label "name" points to the string "Jack"
name = "Angela"     # label moves — now points to "Angela"
```

Reassignment doesn't change the old value, it moves the label.

### Naming rules

| Rule | Example |
|------|---------|
| Can't start with a number | `1user` → invalid |
| No spaces or most symbols | `user name` → invalid |
| Letters, numbers, underscores OK | `user_name` → valid |
| Case-sensitive | `Name` ≠ `name` |
| Convention: all lowercase + underscores | `user_name`, not `UserName` |

### Variable swap — a foundational pattern

```python
glass1 = "milk"
glass2 = "juice"

# You need a temp variable to hold one value during the swap
temp = glass1
glass1 = glass2
glass2 = temp

# Without temp, you'd lose "milk" before moving it:
# glass1 = glass2   →  glass1 is now "juice", "milk" is gone
# glass2 = glass1   →  glass2 is "juice" (wrong)
```

Python shortcut (understand the manual way first):

```python
glass1, glass2 = glass2, glass1
```

---

## `len()`

Returns the number of characters in a string.

```python
len("hello")           # → 5
len("hello world")     # → 11  (space counts)

# Can be nested — Python evaluates from the inside out
print(len(input("Enter your name: ")))
# 1. input() runs → waits for the user → returns a string
# 2. len() counts the characters
# 3. print() displays the result
```

---

## Comments

```python
# This is a comment — Python ignores this line entirely
name = "Angela"  # you can also comment at the end of a line
```

Use comments to explain *why* you're doing something, not just *what*.

---

## Common Errors

| Error | Cause | Example |
|-------|-------|---------|
| `SyntaxError` | Malformed code — missing quote, parenthesis, or typo | `print("hello"` |
| `NameError` | Used a name that doesn't exist — often capitalization | `Print("hi")` |
| `IndentationError` | Wrong whitespace at the start of a line | Indented when you shouldn't be |

---

## Project — Band Name Generator

Ask for a city and a pet's name, combine them into a "band name."

```python
print("Welcome to the Band Name Generator.")
city = input("What city did you grow up in? ")
pet = input("What is the name of your pet? ")
print("Your band name could be " + city + " " + pet)
```

**What this exercises:**
- `input()` to collect data
- Variable assignment to store it
- String concatenation with `+` to combine it

---

## Key Rules

| Rule | Why it matters |
|------|---------------|
| Python is case-sensitive | `print` ≠ `Print` — one works, one crashes |
| `input()` always returns a string | Must convert before doing math |
| Variables are labels, not boxes | Moving the label doesn't delete the value elsewhere |
| `=` is assignment | `name = "Jack"` — this stores a value |
| `==` is comparison | `name == "Jack"` — this checks if it's true (Day 3) |
| Spaces inside strings must be explicit | `"Hello" + "World"` → `"HelloWorld"` not `"Hello World"` |

---

*Day 1 of 100 — April 2026*
