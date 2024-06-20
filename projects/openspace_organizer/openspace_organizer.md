# Challenge: OOP in python to organize the training room

- Repository: `openspace-organizer`
- Type of Challenge: `Consolidation`
- Duration: `2 days`
- Deadline: `14/06/24 5:00 PM`
- Team challenge : team

## Mission objectives

Create an algorithm that randomly assigns people to a spot in the openspace.

![Musical Chairs!](https://i.gifer.com/8OFn.gif)

## Learning Objectives

- Make a good usage of classes.
- Use Object-Oriented-Programming (OOP).
- Use imports in a clean way.
- Use a clean architecture.
- Read data from a xls file
- Structure a project.
- Use git as a team with trello
  - split functionnalities into tasks
  - assign tasks to people
  - develop functionalities on proper branch
  - use PR to merge branches

## The Mission

Your company moved to a new office. Its an openspace with 6 tables of 4 seats. 
As many of you are new colleagues, you come up with the idea of changing seats everyday and get to know each other better by working side by side with your new colleagues.

You will create a program that runs everyday to re-assign everybody to a new seat. 

### Must-have features

You want to build a program that allows you to get a list of colleagues from an excel file and place them ***randomly*** on the different tables of the open space.

#### the default setup of the open space is 6 tables of 4 seats → 24 seats ####

- The program can take a filepath as an argument to load the list of colleagues. 
- The program distributes randomly the people on the existing tables and says how much seats are left.
- The program can deal with the possibility of having to much people in the room.

### Nice-to-have features

Now you have a basic working program but you want to make it more interactive and more configurable.

- Allow the possibility to define the room setup from a config.json file. Allow the possibility to change dynamically the setup and re-run the program.
- Make the program more dynamic and interactive by adding the possibilty to add someone in the room (a new colleague arriving or someone being late) and the possibilty to add a table if the room is full.
- Improve the algorithm to avoid having someone alone at a table
- Allow the possibility of which list (or black list) in the excel file → _X wants to be seated beside Y_ or _X doesn't want to be seated beside Y_
- Allow the possibility to ask : 
  - how much seats are in the room
  - how much people are in the room
  - how much seats are left
- Create an HTML page to interact with your program that : 
  - allows you to choose the excel file from your computer
  - allows you to interact with the different features of the program and execute it.

### Constraints

#### Imports

```python
# You CAN'T import like this:
import whatever_file
# You CAN'T import like this:
import .whatever_file
# You CAN'T import like this:
from .whatever_file.whatever_function
# You CAN'T import like this:
from .whatever_function
# You CAN'T import like this:
from whatever_file
```

```python
# You CAN import like this:
from whatever_file import whatever_function_or_class
```

#### Code style

- Each **class** should have a [`__str__()` method](https://medium.com/swlh/understanding-repr-and-str-in-python-65dd41538943).
- Each **function or class** has to be **typed**
- Each **function or class** has to contain a **docstring** formatted like this:

```python
def add(number_one: int, number_two: int) -> int:
    """
    Function that will perform the add operation between two numbers (in params).

    :param number_one: An int that will be added to the second parameter.
    :param number_two: An int that will be added to the fist parameter.
    :return: An int that is the result of the two params being added to each other.
    """
    result = number_one + number_two
    return result
```

- Your code should be **formatted** with [black](https://pypi.org/project/black/).
- Your code should be **commented**.
- Your code should be **cleaned of any commented unused code**.

#### Repo

- Your repo should only contain the files specified.
- Your README should be nice and complete (see the #Deliverables section below). Feel free to add more information.

Please keep the must-have version separate from the nice-to-have version by using a different branch on GitHub. Please specify that in your README too.

### Steps

It goes without saying, but please, **read through all of this before starting.**

Make sure that you understand the concept of OOP, as this project will make intensive use of it.


_How to program a python project ?_
Until now, you've mostly been working on `.ipynb` files, so called _Jupyter Notebooks_ or `IPython notebooks`.
For a project like this, notebooks are really not a good idea. You'll notice the `.py` file extension in the coming files. These are **python** source files.
Unlike notebooks, which get read using `jupyter` or `jupyter-lab`,
editing python source files is done in an [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment) or a text editor.

Here are a list of popular IDEs or text editors to choose from:

- [vscode](https://code.visualstudio.com/) (IDE/Text editor)
- [PyCharm](https://www.jetbrains.com/pycharm/) (IDE)
- [Atom](https://atom.io/) (Text editor)
- [Sublime Text](https://www.sublimetext.com/) (Text editor)
- [vim](https://www.vim.org/) (Text editor)

Now, let's get to the heart of it!
And I repeat, **read through all of this before starting.**

#### 0. preparation

Create a GitHub repo called `challenge-openspace-classifier` and share it with your team if needed. In this repository create 2 files:

- `README.md`
- `main.py`

And a folder:

- `utils`

In the `utils` folder create 3 files:

- `file_utils.py`
- `table.py`
- `openspace.py`

You're ready to go!

If you're doing it as a team  →  split the work between the members in a Trello board (Kanban like setup) and let each member create a feature branch to develop his own features

#### 1. A table

We define a table with how many seats it encompasses and we define the object in the `table.py` file

##### 1.1 Seat

In `table.py`:

Create a class called `Seat` with two attributes:

- `free` which is a boolean.
- `occupant` which is a string.

and 2 functions : 

- `set_occupant(name)` which allows the program to assign someone a seat if it's free
- `remove_occupant()` which  remove someone from a seat and return the name of the person occupying the seat before

##### 1.2 Table

In the same file, create a class `Table` with ? attributes:

- `capacity` which is an integer
- `seats` which is a list of `Seat` objects (size = `capacity`)

and 3 functions : 
- `has_free_spot()` that returns a boolean (True if a spot is available)
- `assign_seat(name)` that places someone at the table
- `left_capacity()` that returns an integer

#### 2. An openspace

In `openspace.py` create a class `Openspace` that contains these attributes:

- `tables` which is a list of `Table`. _(you will need to import `Table` from `table.py`)_. 
- `number_of_tables` which is an integer.

And some methods:

- `organize(names)` that will:
  - **randomly** assign people to `Seat` objects in the different `Table` objects.
- `display()` display the different tables and there occupants in a nice and readable way
- `store(filename)` store the repartition in an excel file

#### 3. Starting point

In `main.py`:

- Import everything you need to launch the organizer
- load the colleagues from the excel file defined in the config file
- Launch the organizer. Display the results

## Deliverables

1. Publish your source code on the GitHub repository.
2. Pimp up the README file:
   - Description
   - Installation
   - Usage
   - (Visuals)
   - (Contributors)
   - (Timeline)
   - (Personal situation)
3. Clone repo locally as zip file to upload on moodle for friday night **5 PM deadline**

## Evaluation criteria

| Criteria       | Indicator                                                    | Yes/No |
| -------------- | ------------------------------------------------------------ | ------ |
| 1. Is complete | The student has realized all must-have features.             |        |
|                | There is a published GitHub repo available.                  |        |
|                | The program runs until the end without any error.               |        |
|                | The program starts by running `python main.py` in the terminal. |        |
| 2. Is correct  | The code is well typed.                                      |        |
|                | There is a docstring for every function/method/class.        |        |
|                | All the constraints are respected.                           |        |
| 3. Is great    | There is an interaction with the user.                       |        |
|                | The algorithm doesn't create table with alone people.                    |        |
|                | The result is nicely displayed and can be saved in a file. |     |
|                | The program has been developped has a team using proper git flow and management system

## Final note

![You've got this!](https://media.giphy.com/media/BcCoMy2A0eYELrRZ6O/giphy.gif)
