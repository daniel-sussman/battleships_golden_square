# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

    As a player
    So that I can prepare for the game
    I would like to place a ship in a board location

    As a player
    So that I can play a more interesting game
    I would like to have a range of ship sizes to choose from

    As a player
    So the game is more fun to play
    I would like a nice command line interface that lets me enter ship positions and
    shots using commands.

    As a player
    So that I can create a layout of ships to outwit my opponent
    I would like to be able to choose the directions my ships face in

    As a player
    So that I can have a coherent game
    I would like ships to be constrained to be on the board

    As a player
    So that I can have a coherent game
    I would like ships to be constrained not to overlap

    As a player
    So that I can win the game
    I would like to be able to fire at my opponent's board

    As a player
    So that I can refine my strategy
    I would like to know when I have sunk an opponent's ship

    As a player
    So that I know when to finish playing
    I would like to know when I have won or lost

    As a player
    So that I can consider my next shot
    I would like to be able to see my hits and misses so far

    As a player
    So that I can play against a human opponent
    I would like to play a two-player game

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Reminder:
    # User-facing properties:
    #   name: string

    def __init__(self, name):
        # Parameters:
        #   name: string
        # Side effects:
        #   Sets the name property of the self object
        pass # No code here yet

    def remind_me_to(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass # No code here yet

    def remind(self):
        # Returns:
        #   A string reminding the user to do the task
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a name and a task
#remind reminds the user to do the task
"""
reminder = Reminder("Kay")
reminder.remind_me_to("Walk the dog")
reminder.remind() # => "Walk the dog, Kay!"

"""
Given a name and no task
#remind raises an exception
"""
reminder = Reminder("Kay")
reminder.remind() # raises an error with the message "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
