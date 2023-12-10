<h1>REFACTORING</h1>

<div class="quote with-image">
To Write is Human. To Edit is Divine."
<div class="author">&mdash;Stephen King, On Writing: A Memoir of the Craft</div>
<br>

![refactoring.webp](refactoring.webp)

</div>


[//]: # (#### INFO #########################################################)

<div class='info box'>

###### ℹ️  Shorter Labels for Exercises

Up until this now, lab exercises were marked as '🧑‍💻 **Lab Exercise: Some topic**'. 
To eliminate repetition and increase readability (e.g., in the 'Structure' tool 
pane), they will be labeled as '🧑‍💻 **Some Topic**'. That is, please watch the '🧑‍💻' icon; 
it is used uniquely for lab exercises.

</div>

[//]: # (----------------------------------------------------------------------)





# EDITING OPERATIONS

## Keyboard Shortcuts

**Actions**

| Operation                         | MacOS Shortcut | Windows / Linux Shortcut    | Keybinding Name                                         |
|-----------------------------------|----------------|-----------------------------|---------------------------------------------------------|
| Duplicate line or selection       | ⌘ D            | Ctrl + D                    | Duplicate selection                                     |
| Move line or selection up / down  | ⌘⇧ ↑/↓         | Alt + Shift + ↑/↓           | Move statement up / down                                |
| Extend / shrink selection         | ⌥ ↑/↓          | Ctrl + W / Ctrl + Shift + W | Extend / shrink selection                               |
|                                   |                |                             |                                                         |
| Select / deselect next occurrence | ^G / ^⇧G       | Alt + J / Alt + Shift + G   | Add selection via next occurrence / unselect occurrence |
| Select all occurrences in file    | ⌘^G            | Ctrl + Alt + Shift + G      | Select all occurrences                                  |
| Toggle column selection mode      | ⌘⇧8            | Ctrl + Shift + 8            | Column selection mode                                   |
| Add cursor at clicked location    | ⌥ Left Click   | Alt + Left Click            | -                                                       |

**Helpers**

| Operation                                                                  | MacOS Shortcut | Windows / Linux Shortcut | Keybinding Name     |
|----------------------------------------------------------------------------|----------------|--------------------------|---------------------|
| Code completion                                                            | ^ Space        | Ctrl + Space             | Code completion     |
| Parameter descriptions popup (function signature)                          | ⌘ P            | Ctrl + P                 | Parameter info      |
| Quick documentation popup (works when caret is on a function, class, etc.) | F1             | Ctrl + Q                 | Quick documentation |

<br>

[//]: # (#### EXERCISE #########################################################)


<div class="exercise box">

## 🧑‍💻 Extraction

To improve the code, please follow these steps using PyCharm's refactoring facilities:

1. Start by extracting the components of if statements into explanatory variables for better readability and understanding.
2. Next, extract the if statements, along with their explanatory variables, into separate private functions. This will help to modularize the code and improve its maintainability.
3. Finally, review the code and delete any comments that may have become unnecessary after the refactoring process.

```python
import re  # Regex


class UserProfileException(Exception):
    pass


def is_valid_name(name):
    return len(name) >= 3 and re.match("^[A-Za-z]*$", name)


def is_valid_age(age):
    return str(age).isnumeric() and 18 <= int(age) <= 120


def is_logged_in(login_status):
    return login_status


def check_name(name):
    if not is_valid_name(name):
        raise UserProfileException(f"Invalid name: {name}. Name should be at least 3 characters long and should only contain alphabetic characters.")


def check_age(age):
    if not is_valid_age(age):
        raise UserProfileException(f"Invalid age: {age}. Age should be a numeric value between 18 and 120.")


def check_country(country):
    countries = ["Germany", "Netherlands", "Austria", "Sweden"]
    in_valid_countries = country in countries

    if not in_valid_countries:
        raise UserProfileException(f"Invalid country: {country}. Our service is only available in {', '.join(countries)}.")


def check_login_status(login_status):
    if not is_logged_in(login_status):
        raise UserProfileException(f"User is not logged in. Cannot process.")


def check_user_profile(name, age, country, login_status):
    check_name(name)
    check_age(age)
    check_country(country)
    check_login_status(login_status)

    # If all conditions are met, return a success message.
    return f"User {name}'s profile is valid."


# Test the function with some sample data, and handle potential exceptions
try:
    print(check_user_profile("John", 34, "USA", True))
except UserProfileException as e:
    print(e)

try:
    print(check_user_profile("Ana", 15, "USA", False))
except UserProfileException as e:
    print(e)

try:
    print(check_user_profile("", '52', "USA", True))
except UserProfileException as e:
    print(e)

try:
    print(check_user_profile("Carlos", 30, "Spain", True))
except UserProfileException as e:
    print(e)

try:
    print(check_user_profile("Emma", 22, "UK", False))
except UserProfileException as e:
    print(e)

try:
    print(check_user_profile("Rob3rt", 22, "UK", True))
except UserProfileException as e:
    print(e)

```

</div>

[//]: # (----------------------------------------------------------------------)



[//]: # (#### EXERCISE #########################################################)

<div class="exercise box">

## 🧑‍💻 Multiple Cursors

Keyboard shortcut to use during this exercise:
⌘G (MacOS), Alt + J (Windows / Linux)

<h4>Exercise A</h4>

Please use multiple cursors to turn the string below into a list of fruits:

```python
fruits = "Apple, Banana, Cherry, Date, Elderberry, Fig, Guava"
fruits_list = [cursor_selection.strip() for cursor_selection in fruits.split(',')]
```

<h4>Exercise B</h4>

In the below code, use multiple cursors to...

1. Change the `type` parameter into `kind` (do <u>not</u> use the refactoring
   helper [⇧ F6 or Shift + F6] this time).
2. Change 'Star' to 'star'.
3. Remove the part 'Creating a' from the comments.
4. Distribute each parameter into separate lines in usages of the create_star
   function.
5. Remove spaces around the equal signs.

```python
def create_star(kind, 
                size, 
                color, 
                temperature, 
                life_expectancy, 
                galaxy):
    pass


# star in Milky Way
create_star(kind="Red Dwarf", 
            size="Small", 
            color="Red", 
            temperature=3500, 
            life_expectancy="Long", 
            galaxy="Milky Way")

# star in Andromeda
create_star(kind="Blue Giant", 
            size="Large", 
            color="Blue", 
            temperature=25000, 
            life_expectancy="Short", 
            galaxy="Andromeda")

# star (like our Sun) in Milky Way
create_star(kind="Yellow Dwarf", 
            size="Medium", 
            color="Yellow", 
            temperature=5500, 
            life_expectancy="Medium", 
            galaxy="Milky Way")

# star in Whirlpool Galaxy
create_star(kind="White Dwarf", 
            size="Small", 
            color="White", 
            temperature=8000, 
            life_expectancy="Very Long", 
            galaxy="Whirlpool")

# star in Triangulum Galaxy
create_star(kind="Neutron Star", 
            size="Very Small", 
            color="Colorless", 
            temperature=1000000, 
            life_expectancy="Very Long", 
            galaxy="Triangulum")

# star in Pinwheel Galaxy
create_star(kind="Hypergiant", 
            size="Very Large", 
            color="Red", 
            temperature=4000,
            life_expectancy="Short",
            galaxy="Pinwheel")
```

</div>

[//]: # (----------------------------------------------------------------------)




[//]: # (#### EXERCISE #########################################################)

<div class="exercise box">

## 🧑‍💻 Automatic Formatting

While the following table and the text appear OK in rendered Markdown, they are
badly formatted in source code. Can you fix them?

1. Please format this table automatically using the 'quick fixes' helper menu.
   You can activate the quick fixes menu by hovering over underlined code with
   your
   mouse or via the keyboard shortcut ⌥ Enter (Mac) or Alt + Enter (
   Windows/Linus)
   while your caret is blinking within an underlined code segment:

| Name | Age | Occupation | Favorite Color |
|------|-----|------------|----------------|
| John | 32  | Programmer | DodgerBlue     |
| Sue  | 54  | Accountant | Green          
| Jim  | 41  | Teacher    | Red            


2. Please automatically fix the formatting issues in the code below using the 
menu option 'Code > Re-Format Code' (a.k.a., 'Lint') or the keyboard shortcut: 
⌘⌥ L (MacOS) or Ctrl + Alt + L (Windows/Linux).

```python
# Overall, bad vertical spacing
def my_func(my_par = 12) : # Spaces around default parameter equal sign
    x=5           # No spaces around variable assignment equal sign
def my_other_func ( ) : # Spaces around and within parenthesis
 x=5           # Indentation error
my_func ()       # Space before parenthesis
for i in range(10):
  print(i)   # Inconsistent indentation (should be 4 spaces)
a = 1+1  # No spaces around operator
l = [1,2,3] # No spaces after commas
```

3. Please automatically wrap the below text using the same method as in above item.

```md 
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Cras pulvinar mattis nunc sed blandit. Nunc vel risus commodo viverra maecenas. Eget magna fermentum iaculis eu. Vehicula ipsum a arcu cursus vitae congue mauris rhoncus. Nunc eget lorem dolor sed viverra ipsum. Porttitor rhoncus dolor purus non enim praesent. Amet venenatis urna cursus eget nunc scelerisque viverra mauris in. In iaculis nunc sed augue lacus. Suspendisse faucibus interdum posuere lorem. Sit amet facilisis magna etiam tempor orci eu. Quis ipsum suspendisse ultrices gravida dictum fusce ut placerat orci. Magna sit amet purus gravida quis blandit. Risus pretium quam vulputate dignissim suspendisse in est.§
``` 

</div>  

[//]: # (----------------------------------------------------------------------)


# REFACTORING OPERATIONS

## Keyboard Shortcuts

| Operation                                     | MacOS Shortcut | Windows / Linux Shortcut | Keybinding Name      |
|-----------------------------------------------|----------------|--------------------------|----------------------|
| 'Refactor This'                               | ^T             | Ctrl + Alt + Shift + T   | Refactor this        |
| Rename                                        | ⇧ F6           | Shift + F6               | Rename...            |
| Extract method                                | ⌘⌥ M           | Ctrl + Alt + M           | Extract method       |
| Extract variable                              | ⌘⌥ V           | Ctrl + Alt + V           | Introduce variable   |
|                                               |                |                          |                      |
| Contextual actions (suggestions; quick fixes) | ⌥ Enter        | Alt + Enter              | Show context actions |
| Reformat code                                 | ⌘⌥ L           | Ctrl + Alt + L           | Reformat code        |


<br>

[//]: # (#### EXERCISE #########################################################)

<div class="exercise box">

## 🧑‍💻 Safe Rename

Below, the same image file is displayed two times. Please...

1. Begin by locating the image in the project pane. You can accomplish this by 
following these steps:
   - Hover your mouse over the file name below (in the source code, not in the 
     Markdown preview). This action should trigger a popup displaying the file path.
   - Utilize the information in the popup to locate the file path in the project pane.

2. Proceed to change the file name of the first image in the editor (not in the
project pane) to 'refactoring-s.webp'. Remember to use the refactoring features 
(⇧ F6 or Shift + F6) rather than manually altering the name. As you modify the 
file name, take note of how the name also updates in both the next line of code 
and the project pane.


![](img.webp)
![](img.webp)

Once you have made the necessary changes to the file name in the editor, proceed with the following steps:

- Focus on the Project pane and modify the file name to 'refactoring-small.webp'
from there. As you carry out this action, take note of how the file names in 
the code editor also automatically update to reflect the change.



</div>

[//]: # (----------------------------------------------------------------------)



[//]: # (#### EXERCISE #########################################################)

<div class="exercise box">

## 🧑‍💻 Safe Move

Here is the same image file once again:

![img](img.webp)

Can you create an 'images' directory and move the image file to this new
directory? In the move dialog, be sure to select the option 'Search for 
references'.

After you moved the file:

1. What do you see in the image file's path?
2. What about the previous instances where this image file was used?

</div>

[//]: # (----------------------------------------------------------------------)



[//]: # (#### EXERCISE #########################################################)

<div class="exercise box">

## 🧑‍💻 Find Usages and Safe Delete

There is an older version of the file in project directory: 'old_img.jpg'. Imagine
that you want to delete it but not sure if it is uses by any part of the code.

To check for this, you can...

A. Show usages

B. Safe delete (via the relevant checkbox in dialog that appears when you try to
delete a file.)

So, please...

1. Try both methods and delete the file 'img.jpg'.
2. Try the same on 'img.webp'. Please...
    - Show its usages
    - Safe delete the file
3. Imagine you realized you had made a mistake by deleting this file. Can you
   undo?

</div>

[//]: # (----------------------------------------------------------------------)




# SEPARATE REFACTORS ON COMMIT

[//]: # (#### EXERCISE #########################################################)

<div class="exercise box">

## 🧑‍💻 Cherrypick Changes

To proceed with committing changes to this file, please follow these steps:

1. Begin by opening the commit pane.
2. Ensure that all changes are unselected.
3. Double-click on this file (REFACTORING.MD) to open a 'diff' tab.
4. In the diff tab, carefully select the changes that you intend to commit. 
It is important to ensure that these changes are logically related and can be 
grouped together in a commit. For instance, you can group operations such as 
file move and rename operations under a commit named 'restructured directory'.
5. Once you have reviewed and selected the changes, close the diff tab.
6. Finally, commit the changes with an appropriate message to provide a clear 
explanation of the modifications made to the project.

</div>

[//]: # (----------------------------------------------------------------------)




<h1>APPENDIX</h1>

[Notebook Style]

<style>

    :root {
        --lineHeight: 20px;
        --max-width: 510px;
    }

    img {
        border-radius: 6px;
    }

    /* ----- VARIOUS BOXES -------------------------------------------------- */


    .box {
        margin-top: 15px;
        padding: 5px 20px 5px 20px;
        border-width: 1.5px;
        border-style: solid;
        border-radius: 6px;
        line-height: var(--lineHeight);
        max-width: var(--max-width);
    }

    /* Placeholders are for instructions such as `Enter your answer here' */
    .placeholder, .answer-container {  /* gray, dashed*/
        max-width: var(--max-width);
        color: rgb(130, 130, 130);
        padding: 16px 10px;
        border: 1px dashed rgb(130, 130, 130);
        border-radius: 6px;
        font-family: "Courier New", Courier, monospace;
        line-height: var(--lineHeight);
    }

    /* Code placeholders are pre-filled */
    .placeholder-code {  /* gray, dashed*/
        max-width: var(--max-width);
        color: rgb(130, 130, 130);
        padding: 16px 10px;
        border: 1px dashed rgb(130, 130, 130);
        border-radius: 6px;
        font-family: "Courier New", Courier, monospace;
        line-height: var(--lineHeight);
    }
    .placeholder-code::before {
        content: "Your code here."
    }

    .exercise {  /* green */
        background-color: rgb(225, 241, 223);
        border-color: rgba(91, 116, 127, 0.25);
    }

   .exercise * {
      color: rgb(91, 127, 116);
   }

    .student-entry {
        max-width: var(--max-width);
        padding: 16px 10px;
        border: 1px solid;
        border-radius: 6px;
        line-height: var(--lineHeight);

    }

   .exercise > .student-entry, .exercise > * > li > .student-entry {
        background-color: rgb(205, 221, 203);
        border-color: rgba(91, 116, 127, 0.25);
   }

    .info {  /* blue */
        background-color: rgb(210, 234, 244);
        border-color: rgba(91, 116, 127, 0.25);
    }
       .info * {
        color: rgb(91, 116, 127);
    }

    
    .assignment {  /* yellow */
        background-color: #FBE3BB;
        border-color: #EBDDBF;
    }
   .assignment * {
     color: #AF704D;
   }

    .assignment > .student-entry, .assignment > * > li > .student-entry {
        background-color: rgba( 150, 0, 0, 0.1);
        border-color: #AF704D;
    }

    .warning {  /* red */
        color: rgb(139, 83, 88);
        background-color: rgb(238, 213, 217);
        border-color: rgba(139, 83, 88, 0.25);
    }


    .addendum {
        background-color: DarkSalmon;
        color: White;
        font-size: 20px;
        font-weight: bold;
        height: 60px;
        padding-left: 20px;  
        padding-top: 55px !important;      
    }


    .todo {
        background-color: GoldenRod;
        color: DarkRed;
        font-size: 30px;
        font-weight: bold;
        padding-left: 20px;
        padding-bottom: 55px !important;      
        padding-top: 55px !important;      
    }

    .todo-next-year {
        background-color: Gray;
        color: Black;
        font-size: 30px;
        font-weight: bold;
        padding-bottom: 27px !important;      
        padding-left: 20px;  
        padding-top: 27px !important;      
    }
   
    .todo-description {
        font-size:12pt; 
        font-weight: normal;
    }


    /* Code fences */
    pre code {
    
    }

    /* Code block */
    .code {
        color: rgb(18, 18, 18);
        background-color: rgba(250, 250, 250, 0.75); /* gray background */
        border: 1px solid #ddd;
        border-radius: 4px;
        font-family: "Courier New", Courier, monospace;
        white-space: pre-wrap; /* Instead of using break tags for every individual line break, you can simply use newline characters. (However, for double line breaks, a break tag is still necessary, although a single one would suffice.) */
    }

    .codebox {
        padding-top: 0px;
        padding-bottom: 20px;
        padding-left: 15px;
        padding-right: 15px;
        color: rgb(18, 18, 18);
        background-color: rgba(250, 250, 250, 0.75); /* gray background */
        border: 1px solid #ddd;
        border-radius: 4px;
        font-family: "Courier New", Courier, monospace;
        white-space: pre-wrap; /* Instead of using break tags for every individual line break, you can simply use newline characters. (However, for double line breaks, a break tag is still necessary, although a single one would suffice.) */
    }



    details > div {
        padding-left: 15px;
        background-color: rgba(0, 0, 0, 0.05);
        padding: 15px;
        border-radius: 6px;
    }

    details > summary {
        cursor: pointer;
    }

    .quote {
        background: rgba(203, 195, 227);
        padding: 0.8em 10px;
        font-size: 1.05em;
        /*font-style: italic;*/
        line-height: 1.5em;
        color: rgb(123, 115, 147);
        border: 0 solid rgba(203, 195, 227, 0.8);  /* Width is overwritten via border-with */
        border-width: 1.5px 1.5px 1.5px 10px;
        border-radius: 4px;
        color: rgb(108, 60, 128);
        max-width: 500px;

    }

    .quote:before {
        content: "\“";
        font-size: 4em;
        line-height: 0.1em;
        margin-right: 0.25em;
        vertical-align: -0.4em;
        color: rgb(183, 175, 207);
    }

    .quote p {
        display: inline; 
    }


    .author {
        margin-top: 0.5em;
        color: rgb(123, 115, 147);
        font-style: normal;
        font-size: 0.8em;
    }


    /* ----- TEXT ----------------------------------------------------------- */

    p, li, h1, h2, h3, h4, h5, h6, pre {
      max-width: var(--max-width);
    }

    .rule-code{
        color:lightgray;
        font-size:11pt;
    }


    /* ----- TABLE -----------------------------------------------------------*/

    table {
        border-collapse: collapse;
        width: 100%;
    }

    th, td {
        border: 1px solid #000;
        padding: 8px;
        text-align: left;
    }

    .clean-code {
        color: OliveDrab;
    }

    .dirty-code {
        color: IndianRed;
    }

</style>