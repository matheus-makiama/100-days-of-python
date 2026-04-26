# Day 04 — Randomization & Lists

> **Course:** 100 Days of Code — The Complete Python Pro Bootcamp (Angela Yu)
> **Date:** April 2026
> **Topics:** Modules, `random`, lists, indexing, nested lists, rock-paper-scissors logic

---

## Table of Contents
- [Modules](#modules)
- [The random Module](#the-random-module)
- [Lists](#lists)
- [List Methods](#list-methods)
- [Accessing Elements](#accessing-elements)
- [Nested Lists](#nested-lists)
- [Project — Rock Paper Scissors](#project--rock-paper-scissors)
- [Key Rules](#key-rules)

---

## Modules

A module is just another `.py` file you can import into your code to reuse its functions and variables.

```python
# my_module.py
my_favorite_number = 3.1415
```

```python
# main.py
import random
import my_module

print(random.randint(1, 10))           # uses random module
print(my_module.my_favorite_number)   # uses your custom module
```

The dot `.` means "look inside this module and grab what's after the dot."

You don't need to write everything yourself — Python ships with a huge standard library of modules. Use them.

---

## The `random` Module

```python
import random
```

| Function | Returns | Range |
|----------|---------|-------|
| `random.randint(a, b)` | Integer | `a` to `b` — **both endpoints included** |
| `random.random()` | Float | `[0.0, 1.0)` — 0 included, 1 excluded |
| `random.uniform(a, b)` | Float | `a` to `b` — can include both ends due to float rounding |
| `random.choice(list)` | One element | Randomly picked from the list |
| `random.shuffle(list)` | Nothing | Shuffles the list **in place** |

```python
random.randint(1, 10)   # → any integer from 1 to 10 (including 1 and 10)
random.random()         # → e.g. 0.7293...  (never exactly 1.0)
random.uniform(0, 10)   # → e.g. 7.42...
random.choice(["red", "blue", "green"])   # → one of the three
```

### Coin flip example

```python
import random

result = random.randint(0, 1)
if result == 0:
    print("Heads")
else:
    print("Tails")
```

---

## Lists

A list stores multiple values in a single variable, in order.

```python
fruits = ["Apple", "Peach", "Pear"]
states = ["Delaware", "Pennsylvania", "New Jersey"]
mixed  = [42, "hello", True, 3.14]   # lists can hold different types
```

Lists are **ordered** — the items stay in the order you put them, and each has a numbered position (index) starting from `0`.

```
fruits = ["Apple", "Peach", "Pear"]
index:     0        1        2
```

---

## List Methods

```python
fruits = ["Apple", "Peach"]

fruits.append("Pear")                    # add one item to the end
fruits.extend(["Mango", "Strawberry"])   # add multiple items to the end
fruits[0] = "Banana"                     # replace item at index 0
```

| Method | What it does | Returns |
|--------|-------------|---------|
| `.append(item)` | Adds one item to the end | Nothing (`None`) |
| `.extend([items])` | Adds multiple items to the end | Nothing (`None`) |
| `.remove(item)` | Removes the first occurrence of item | Nothing |
| `.pop()` | Removes and returns the last item | The removed item |
| `.sort()` | Sorts the list in place | Nothing |
| `.reverse()` | Reverses the list in place | Nothing |
| `len(list)` | Returns number of items | Integer |

---

## Accessing Elements

```python
fruits = ["Apple", "Peach", "Pear", "Mango"]

# Positive indexing — from the front
fruits[0]    # → "Apple"
fruits[2]    # → "Pear"

# Negative indexing — from the back
fruits[-1]   # → "Mango"  (last item)
fruits[-2]   # → "Pear"   (second to last)

# Getting the last index safely
last = fruits[len(fruits) - 1]   # → "Mango"
last = fruits[-1]                 # same result, cleaner
```

### Off-by-one — the classic mistake

```python
fruits = ["Apple", "Peach", "Pear"]
# Length is 3, but indexes are 0, 1, 2 — NOT 0, 1, 2, 3

fruits[3]   # IndexError: list index out of range
fruits[2]   # → "Pear" (correct last index = length - 1)
```

### Picking a random element — two approaches

```python
friends = ["Alice", "Bob", "Charlie", "David"]

# Manual — fragile: if you add a friend, the hardcoded 3 is now wrong
print(friends[random.randint(0, 3)])

# Better — random.choice handles it automatically
print(random.choice(friends))
```

> Always prefer `random.choice()`. The manual version creates an invisible bug every time you change the list.

---

## Nested Lists

A list can contain other lists. Access them with chained indexes.

```python
fruits = ["Strawberries", "Apples", "Peaches"]
veggies = ["Spinach", "Kale", "Tomatoes"]

produce = [fruits, veggies]

produce[0]      # → ["Strawberries", "Apples", "Peaches"]  (first list)
produce[1]      # → ["Spinach", "Kale", "Tomatoes"]        (second list)
produce[1][1]   # → "Kale"  (second list → second item)
```

Read left to right: `[1]` picks the second list, `[1]` picks the second item inside it.

---

## Project — Rock Paper Scissors

### The number mapping

```
rock     → 0
paper    → 1
scissors → 2
```

### Why the if-chain is ordered the way it is

Most outcomes follow one rule: **higher number wins**.
- paper(1) beats rock(0) ✓
- scissors(2) beats paper(1) ✓

But the game is a **cycle** — rock(0) beats scissors(2), even though 0 is the smaller number. That wrap-around case must be handled **before** the general rule, or it will never match.

```python
import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("Invalid input. You lose!")

else:
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print(f"Computer chose:\n{game_images[computer_choice]}")

    if user_choice == 0 and computer_choice == 2:
        print("You win!")                        # rock beats scissors (wrap-around)
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")                       # scissors loses to rock (wrap-around)
    elif computer_choice > user_choice:
        print("You lose!")                       # general rule: higher wins
    elif user_choice > computer_choice:
        print("You win!")                        # general rule: higher wins
    elif user_choice == computer_choice:
        print("It's a draw!")
```

### Logic flow

```
user_choice
    ↓
Invalid (< 0 or >= 3)? → lose immediately
    ↓ no
user=rock(0) and computer=scissors(2)? → win  ← wrap-around case
    ↓ no
computer=rock(0) and user=scissors(2)? → lose ← wrap-around case
    ↓ no
computer > user? → lose  ← general rule
    ↓ no
user > computer? → win   ← general rule
    ↓ no
draw
```

**Why order matters:** Python checks `if/elif` top-down and stops at the first match. If you put the general "higher wins" rule first, scissors(2) would always beat rock(0) because `2 > 0` — which is wrong. The wrap-around exceptions must come first.

### The smarter version (spoiler — uses modulo)

```python
result = (user_choice - computer_choice) % 3
# 0 → draw
# 1 → user wins
# 2 → user loses
```

Works because the cycle is exactly 3 long. Not introduced until Day 5 — just know it exists.

---

## Key Rules

| Rule | Why it matters |
|------|---------------|
| Lists are 0-indexed | Length 3 → indexes 0, 1, 2 — never index 3 |
| Last index = `len(list) - 1` or use `-1` | Accessing `list[len]` crashes with `IndexError` |
| Use `random.choice()` not `random.randint(0, n)` | Hardcoded index breaks when list size changes |
| `random.shuffle()` modifies in place, returns `None` | `result = random.shuffle(x)` stores `None`, not the shuffled list |
| `if/elif` order determines which case wins | Specific exceptions must come before general rules |
| Import modules at the top of the file | Convention — makes dependencies visible immediately |

---

*Day 4 of 100 — April 2026*
