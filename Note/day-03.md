# Day 03 — Conditionals & Logical Operators

> **Course:** 100 Days of Code — The Complete Python Pro Bootcamp (Angela Yu)
> **Date:** April 24–25, 2026
> **Topics:** `if/elif/else`, comparison operators, logical operators, `.lower()`, nesting, raw strings

---

## Table of Contents
- [if / elif / else](#if--elif--else)
- [Comparison Operators](#comparison-operators)
- [Logical Operators](#logical-operators)
- [Truthy and Falsy](#truthy-and-falsy)
- [.lower() and .upper()](#lower-and-upper)
- [Nested Conditionals](#nested-conditionals)
- [Raw Strings and Quote Escaping](#raw-strings-and-quote-escaping)
- [Mistakes I Made](#mistakes-i-made)
- [Project — Pizza Order Calculator](#project--pizza-order-calculator)
- [Project — Treasure Island](#project--treasure-island)
- [Key Rules](#key-rules)

---

## `if / elif / else`

A conditional runs a block of code only when a condition is true.

```python
age = int(input("How old are you? "))

if age < 12:
    print("Child ticket: $5")
elif age < 18:
    print("Youth ticket: $10")
elif age >= 65:
    print("Senior ticket: $10")
else:
    print("Adult ticket: $15")
```

**How it works:**
- Python checks each condition top-to-bottom.
- The **first** condition that is `True` runs — the rest are skipped entirely.
- `else` is the fallback — runs only if nothing above matched.
- Only ONE branch executes per `if/elif/else` chain.

> **Critical:** Order matters. If you put a broad condition before a specific one, the specific one will never be reached.

---

## Comparison Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `7 > 3` | `True` |
| `<` | Less than | `2 < 8` | `True` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal | `4 <= 6` | `True` |

```python
# = is assignment (stores a value)
name = "Angela"

# == is comparison (checks if two things are equal)
if name == "Angela":
    print("Hello Angela")
```

> Never confuse `=` and `==`. One stores, one compares. Python won't always warn you if you get it wrong.

---

## Logical Operators

Combine multiple conditions into one.

### `and` — both must be true

```python
if age >= 18 and age <= 65:
    print("Standard rate applies")
```

- Returns `True` only when **every** condition is true.
- Short-circuits: stops at the **first `False`** (no point checking the rest).

### `or` — at least one must be true

```python
if day == "Saturday" or day == "Sunday":
    print("Weekend!")
```

- Returns `True` when **any** condition is true.
- Short-circuits: stops at the **first `True`**.

### `not` — flips the result

```python
if not is_raining:
    print("Go outside")
```

---

## Truthy and Falsy

Python treats some values as `True` and others as `False` without explicit comparison:

| Falsy (treated as `False`) | Truthy (treated as `True`) |
|----------------------------|----------------------------|
| `0` | Any non-zero number |
| `""` (empty string) | Any non-empty string |
| `[]` (empty list) | Any non-empty list |
| `None` | Almost everything else |
| `False` | `True` |

```python
name = ""
if name:                    # same as: if name != ""
    print(f"Hello {name}")
else:
    print("No name given")
```

---

## `.lower()` and `.upper()`

String methods that return a modified copy of the string (they don't change the original).

```python
choice = input("Left or Right? ").lower()
# If user types "LEFT", "Left", or "left", they all become "left"

if choice == "left":
    print("You went left")
```

This is the standard way to handle case-insensitive input — convert first, compare once.

```python
# Without .lower() you'd need:
if choice == "left" or choice == "Left" or choice == "LEFT":
    ...

# With .lower() — clean:
choice = input("...").lower()
if choice == "left":
    ...
```

---

## Nested Conditionals

A conditional inside another conditional. Used when one decision depends on a previous one.

```python
choice = input("Go left or right? ").lower()

if choice == "left":
    # Only reach this point if they went left
    next_choice = input("Swim or wait? ").lower()
    if next_choice == "wait":
        print("You made it!")
    else:
        print("Attacked by trout. Game over.")
else:
    print("Fall into a hole. Game over.")
```

### When to nest vs. when to keep separate

| Pattern | When to use |
|---------|-------------|
| **Nested** `if` | Decision B only matters if decision A succeeded — sequential |
| **Separate** `if` | Decisions A and B are independent — both always checked |

```python
# WRONG — two independent ifs that should be nested
if choice == "left":
    print("You went left")
if next_choice == "wait":       # runs regardless of the first choice
    print("You waited")

# CORRECT — nest it
if choice == "left":
    print("You went left")
    if next_choice == "wait":   # only reached if they went left
        print("You waited")
```

> Tip: when logic gets 3+ levels deep, sketch the decision tree on paper before coding. It prevents tangled branches.

---

## Raw Strings and Quote Escaping

### Quote escaping — two options

When a string contains the same quote character that wraps it:

```python
# Option A: swap quote types
print("You're here.")        # double outside, apostrophe inside — fine
print('Say "hi" to her.')    # single outside, double inside — fine

# Option B: backslash escape
print('You\'re here.')       # \' = literal apostrophe
print("She said \"hi\".")    # \" = literal double-quote
```

Most programmers default to double-outside, since apostrophes appear more in English text than literal double-quotes.

### Raw strings — prefix with `r`

A raw string treats backslashes as literal characters — no escape processing.

```python
# Normal string — \n becomes a newline
print("C:\new_folder")     # prints: C:
                           #         ew_folder   (oops)

# Raw string — \n is kept as-is
print(r"C:\new_folder")    # prints: C:\new_folder
```

Use raw strings for:
- File paths on Windows (`r"C:\Users\folder"`)
- Regular expressions (covered much later)

---

## Mistakes I Made

### Mistake 1 — The `or` trap

```python
# WRONG — looks like it checks for "Left" too, but it doesn't
if choice == "left" or "Left":
    ...
```

This is a logic bug. Python reads it as:
```python
if (choice == "left") or ("Left"):
```

`"Left"` is a non-empty string → it's always truthy → the whole condition is **always `True`**, no matter what the user types.

```python
# CORRECT — each side of or must be a full comparison
if choice == "left" or choice == "Left":
    ...

# BETTER — just use .lower()
if choice.lower() == "left":
    ...
```

> **Rule:** each operand of `or` and `and` must be a **complete expression**. `x == 1 or 2` is broken. `x == 1 or x == 2` is correct.

---

### Mistake 2 — Redundant condition

```python
# WRONG — both conditions say the same thing
elif age <= 18 and age <= 25:
    ...
```

Anyone who is `<= 18` is automatically `<= 25`. The second condition adds nothing — the `and` collapses to just `age <= 18`.

```python
# CORRECT — if you want a range, both bounds must be meaningful
elif age >= 12 and age <= 18:    # "between 12 and 18"
    ...
```

> **Rule:** with `and`, both conditions must actually constrain. Read it out loud — does each condition filter something out?

---

### Mistake 3 — Two parallel `if`s instead of nested

```python
# WRONG — both ifs run independently
if choice == "left":
    print("You went left")
if next_choice == "wait":
    print("You waited")
# If user chose "right", they'd hit BOTH else branches and lose twice
```

```python
# CORRECT — nest when one decision depends on the previous
if choice == "left":
    print("You went left")
    if next_choice == "wait":
        print("You waited")
    else:
        print("Attacked by trout. Game over.")
else:
    print("Fall into a hole. Game over.")
```

---

## Project — Pizza Order Calculator

```python
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza? S, M, or L: ")
pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill += 2
elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill += 3
elif size == "L":
    bill = 25
    if pepperoni == "Y":
        bill += 3
else:
    print("Invalid size. Please try again.")
    bill = 0

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
```

**What this exercises:**
- Nested `if` — pepperoni price depends on size
- `+=` to build up a total
- f-string for the final output
- `else` to catch invalid input

---

## Project — Treasure Island

A branching text adventure using nested conditionals.

```python
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice = input("Go left or right?\n: ").lower()

if choice == "left":
    choice = input("Swim or wait?\n: ").lower()
    if choice == "wait":
        choice = input("Pick a door — Red, Blue, or Yellow\n: ").lower()
        if choice == "yellow":
            print("You win! You found the treasure.")
        elif choice == "red":
            print("Burned by fire. Game over.")
        elif choice == "blue":
            print("Eaten by beasts. Game over.")
        else:
            print("Invalid door. Game over.")
    else:
        print("Attacked by trout. Game over.")
else:
    print("Fell into a hole. Game over.")
```

**Lesson from this project:** Nested conditionals deeper than 3 levels are hard to read as plain code. Sketch the decision tree first, then translate it to `if/elif/else`.

---

## Key Rules

| Rule | Why it matters |
|------|---------------|
| `=` is assignment, `==` is comparison | Mixing them up causes silent bugs |
| `if/elif/else` — only ONE branch runs | First match wins, rest skipped |
| Separate `if`s run independently | Both get checked every time, no matter what |
| `or`/`and` — each operand needs a full expression | `x == 1 or 2` is always True; `x == 1 or x == 2` is correct |
| Non-empty strings are truthy | `"Left"` alone is always `True` — common trap |
| Use `.lower()` on input | Handle case-insensitive input in one line |
| "Runs without error" ≠ "is correct" | Always test with bad inputs, not just good ones |

---

*Day 3 of 100 — April 2026*
