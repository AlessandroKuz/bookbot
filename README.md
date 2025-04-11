# bookbot

BookBot is a python3 simple CLI tool that allows the user to get basic stats of a book, or any text file.

BookBot is my first [Boot.dev](https://www.boot.dev) project!

## Table of Contents

1. [Installation](#Installation)
2. [Usage](#Usage)
3. [Example](#Example)

## Installation

To run the tool you only need python (the version should be at least `python>=3.8` - due to the use of f-strings), which can be installed with your favourite package manager, or by visiting [Python.org downloads page](https://www.python.org/downloads), make sure to add it to your `$PATH` variable.
No packages or additional modules are needed.

After installing python, you can:
- Download the zip file and extract it
- Or if you have `git` installed (as with python you can download it with a package manager or the official website [Git-Scm downloads page](https://git-scm.com/downloads)), clone the repository (copy it to your desktop) with the following command:
    ```bash
    git clone https://github.com/AlessandroKuz/bookbot.git
    ```

## Usage

Once you have installed all the requirements, you're good to go!

Just access the directory with your shell/terminal via the following command:
```bash
cd bookbot
```
And then you can get the stats of any text file with the following command:
```bash
python3 main.py <text_filepath>
```

## Example

When running the script against any text file, for example:

```bash
python3 main.py book/frankenstein.txt
```

You should see something like this:

```text
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
p: 5952
g: 5795
b: 4868
v: 3737
k: 1661
x: 691
j: 497
q: 325
z: 235
æ: 28
â: 8
ê: 7
ë: 2
ô: 1
```

In the example the ["Frankenstein" book](https://www.gutenberg.org/cache/epub/41445/pg41445.txt) from ["Project Guthemberg"](https://www.gutenberg.org/) was used.

