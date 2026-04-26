# Day 05 — For Loops, range() & Password Generator

> **Course:** 100 Days of Code — The Complete Python Pro Bootcamp (Angela Yu)
> **Date:** April 2026
> **Topics:** `for` loops, `range()`, `sum()`, `max()`, modulo, FizzBuzz, `random.shuffle()`, `''.join()`, list comprehension

---

## Table of Contents
- [For Loops](#for-loops)
- [Looping with range()](#looping-with-range)
- [sum() and Manual Totals](#sum-and-manual-totals)
- [Replicating max()](#replicating-max)
- [FizzBuzz](#fizzbuzz)
- [List Comprehension](#list-comprehension)
- [Project — Password Generator](#project--password-generator)
- [Built-in Names — Never Use as Variables](#built-in-names--never-use-as-variables)
- [Key Rules](#key-rules)
- [Day 5 Quick Reference](#day-5-quick-reference)

---

## For Loops

A `for` loop runs a block of code once for every item in a sequence.

```python
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
```

**Output:**
```
Apple
Apple pie
Peach
Peach pie
Pear
Pear pie
```

**How it works:**
1. `fruit` is assigned the first item: `"Apple"`
2. The indented block runs
3. `fruit` updates to the next item: `"Peach"`
4. The block runs again
5. Repeat until the list is exhausted

After the loop ends, `fruit` still holds the last value (`"Pear"`).

### The loop variable name is arbitrary

```python
for item in fruits:     # works
for x in fruits:        # works
for banana in fruits:   # works — confusing, but works
for fruit in fruits:    # best — matches what's in the list
```

Use a name that describes the item, not the collection.

### `_` for loops where you don't need the variable

When you just need to run something N times and don't care about the index:

```python
# Bad — the variable i is never used inside the block
for i in range(5):
    print("hello")

# Good — _ signals "I don't need this variable"
for _ in range(5):
    print("hello")
```

---

## Looping with `range()`

`range()` generates a sequence of integers without creating a full list in memory.

```python
# range(stop) — starts at 0 by default
for n in range(5):
    print(n)      # prints 0, 1, 2, 3, 4  (not 5)

# range(start, stop) — stop is EXCLUDED
for n in range(1, 6):
    print(n)      # prints 1, 2, 3, 4, 5

# range(start, stop, step) — count by step
for n in range(0, 10, 2):
    print(n)      # prints 0, 2, 4, 6, 8

# Counting down
for n in range(10, 0, -1):
    print(n)      # prints 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

> **The stop value is always excluded.** `range(1, 101)` gives you 1 to 100, not 1 to 101. This is intentional — the count of items is `stop - start`.

### Sum 1 to 100

```python
total = 0
for number in range(1, 101):
    total += number
print(total)   # → 5050
```

**Why 5050?** Gauss's trick: pair numbers from both ends.
- 1 + 100 = 101
- 2 + 99 = 101
- 3 + 98 = 101
- ...50 pairs total

50 × 101 = **5050**

---

## `sum()` and Manual Totals

```python
scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199]

# Built-in — always prefer this
total = sum(scores)

# Manual version — how sum() works under the hood
total = 0
for score in scores:
    total += score
```

In real code, use `sum()`. The manual version exists to understand the pattern — you'll use it when the built-in doesn't fit.

---

## Replicating `max()`

```python
scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199]

# Built-in — use this in real code
print(max(scores))   # → 199

# Manual version — how max() works under the hood
max_score = scores[0]        # start with the first item, not 0
for score in scores:
    if score > max_score:
        max_score = score
print(max_score)             # → 199
```

### Why start with `scores[0]` instead of `0`?

```python
temperatures = [-10, -5, -20, -3]

# BAD — starts at 0, which is higher than all values
max_temp = 0
for t in temperatures:
    if t > max_temp:
        max_temp = t
print(max_temp)   # → 0  (WRONG — the actual highest is -3)

# GOOD — start with the first real item
max_temp = temperatures[0]
for t in temperatures:
    if t > max_temp:
        max_temp = t
print(max_temp)   # → -3  (correct)
```

---

## FizzBuzz

A classic programming exercise. For numbers 1 to 100:
- If divisible by both 3 and 5 → print "FizzBuzz"
- If divisible by 3 only → print "Fizz"
- If divisible by 5 only → print "Buzz"
- Otherwise → print the number

```python
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
```

### The modulo operator `%`

Returns the **remainder** after integer division:

```python
10 % 3    # → 1   (10 ÷ 3 = 3 remainder 1)
15 % 3    # → 0   (15 ÷ 3 = 5 remainder 0 — exactly divisible)
15 % 5    # → 0   (15 ÷ 5 = 3 remainder 0 — exactly divisible)
7 % 2     # → 1   (odd number check: odd numbers always have remainder 1)
8 % 2     # → 0   (even number check)
```

**"Is divisible by N"** = `number % N == 0`

### Why the FizzBuzz check order matters

```python
# WRONG — checks % 3 first
for number in range(1, 101):
    if number % 3 == 0:         # 15 matches here → prints "Fizz"
        print("Fizz")
    elif number % 5 == 0:       # never reached for 15
        print("Buzz")
    elif number % 3 == 0 and number % 5 == 0:  # also never reached
        print("FizzBuzz")
```

The combined check must come **first**. Python stops at the first matching condition — if you check `% 3` first, numbers like 15 will match it before ever reaching the `FizzBuzz` branch.

---

## List Comprehension

A compact way to build a list from a loop. Not required at this stage — just know it exists.

```python
fruits = ["Apple", "Peach", "Pear"]

# Standard loop version
results = []
for fruit in fruits:
    results.append(fruit + " pie")

# List comprehension — same result in one line
results = [fruit + " pie" for fruit in fruits]
```

Read it as: *"give me `fruit + ' pie'` for each `fruit` in `fruits`."*

---

## Project — Password Generator

Ask the user how many letters, symbols, and numbers they want. Generate a random password from those characters and shuffle them.

```python
import random
import string

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters?\n"))
nr_symbols = int(input("How many symbols?\n"))
nr_numbers = int(input("How many numbers?\n"))

password_list = []

for _ in range(nr_letters):
    password_list.append(random.choice(string.ascii_letters))

for _ in range(nr_symbols):
    password_list.append(random.choice("!#$%&()*+"))

for _ in range(nr_numbers):
    password_list.append(random.choice(string.digits))

random.shuffle(password_list)
password = "".join(password_list)
print(f"Your password is: {password}")
```

### Key functions used

| Function | What it does |
|----------|-------------|
| `string.ascii_letters` | All letters a–z + A–Z built into Python — no need to type them |
| `string.digits` | All digits `0–9` built into Python |
| `random.choice(list)` | Returns one random item from a list |
| `random.shuffle(list)` | Shuffles the list **in place** — modifies the original, returns `None` |
| `list(string)` | Splits a string into individual characters — `list("abc")` → `['a', 'b', 'c']` |
| `"".join(list)` | Joins a list of strings/chars back into one string — `"".join(['a','b','c'])` → `'abc'` |

### Why shuffle?

Without shuffling, the output is always in a predictable order: all letters, then all symbols, then all numbers (e.g. `aBcX!#14`). That's a recognizable pattern, which weakens the password. Shuffling randomizes the order so the structure isn't guessable.

### Common mistakes in the password generator

```python
# BAD — loop variable is declared but never used inside the block
for i in range(nr_letters):
    password_list.append(random.choice(string.ascii_letters))

# GOOD — _ signals you don't need the variable
for _ in range(nr_letters):
    password_list.append(random.choice(string.ascii_letters))

# BAD — result goes nowhere, nothing is stored or added
random.choice(string.digits)

# GOOD — store the result
password_list.append(random.choice(string.digits))

# BAD — shuffle returns None, not the shuffled list
shuffled = random.shuffle(password_list)    # shuffled is None
print(shuffled)                              # prints None

# GOOD — shuffle modifies in place, use the original list
random.shuffle(password_list)
print("".join(password_list))               # correct
```

---

## Built-in Names — Never Use as Variables

Python has built-in functions and types with reserved names. Naming a variable after any of them **silently overwrites it** for the rest of your script:

```python
# This overwrites Python's built-in sum() function
sum = 0
for score in scores:
    sum += score

# Now this crashes with TypeError because sum is an integer, not a function
print(sum([1, 2, 3]))
```

**Names to never use as variables:**

`sum` `max` `min` `list` `dict` `set` `tuple` `input` `print` `type` `id` `len` `range` `open` `zip` `map` `filter` `sorted` `reversed` `str` `int` `float` `bool`

Instead use: `total`, `maximum`, `result`, `my_list`, `count`, etc.

---

## Key Rules

| Rule | Why it matters |
|------|---------------|
| `range()` excludes the stop value | `range(1, 101)` → 1 to 100, not 101 |
| Start `max()` logic with `list[0]`, not `0` | Starting at `0` gives wrong results for all-negative lists |
| FizzBuzz combined check comes first | `if/elif` stops at first match — specific cases before general |
| `random.shuffle()` returns `None` | Shuffle in place, then use the original list variable |
| `"".join(list)` converts list back to string | `list()` splits strings; `join()` reassembles them |
| Never shadow built-in names | `sum = 0` silently breaks `sum()` for the rest of the file |
| Use `_` when loop variable is unused | Signals intent — "I'm looping N times, I don't need the counter" |

---

## Day 5 Quick Reference

| Concept | Syntax | Example |
|---------|--------|---------|
| For loop | `for x in list:` | `for fruit in fruits:` |
| Range (stop only) | `range(n)` | `range(5)` → 0–4 |
| Range (start, stop) | `range(a, b)` | `range(1, 6)` → 1–5 |
| Range (with step) | `range(a, b, step)` | `range(0, 10, 2)` → 0,2,4,6,8 |
| Add to total | `total += x` | `total += score` |
| Modulo | `a % b` | `15 % 3` → `0` |
| Random pick | `random.choice(list)` | `random.choice(fruits)` |
| Shuffle in place | `random.shuffle(list)` | `random.shuffle(pw_list)` |
| Join list to string | `"sep".join(list)` | `"".join(['a','b'])` → `'ab'` |
| All letters | `string.ascii_letters` | `'abcde...XYZ'` |
| All digits | `string.digits` | `'0123456789'` |
| List comprehension | `[expr for x in list]` | `[x*2 for x in nums]` |

---

*Day 5 of 100 — April 2026*
