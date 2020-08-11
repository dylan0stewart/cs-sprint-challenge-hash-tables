# Sprint Challenge: Hash Tables

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This challenge allows you to practice the concepts and techniques learned over the past sprint and apply them in a concrete project. This sprint explored hash tables. During this sprint, you studied hash functions, collision resolution, complexity analysis of hash tables, load factor, resizing, and various use cases for hash tables. In your challenge this week, you will demonstrate mastery of these skills by solving five problems related to hash tables.

The sprint challenge is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the sprint challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your TL if you need direction.

_You have **three hours** to complete this challenge. Plan your time accordingly._

## Introduction

This challenge requires you to solve algorithm problems that are amenable to being solved efficiently with a hash table.

### Commits

Commit your code regularly and meaningfully. This practice helps both you (in case you ever need to return to old code for any number of reasons) and your Team Lead as they evaluate your solution.

## Interview Questions

Be prepared to demonstrate your understanding of this week's concepts by answering questions on the following topics. You might prepare by writing down your answers beforehand.

1. Hashing functions
    Hashing functions basically 'compress' data, and use a key to find it later. Essentially for a hash table to be worth it. They should be efficient computationally and should evenly distribute the keys; need to be efficient because otherwise why use one, and they need to evenly distribute keys so that they can/will still be distinct

2. Collision resolution
    Collision Resolution is simply an algorithmic approach to handle situations where two or more items should be kept in the same spot.
    An example: one method for conflict resolution is simply starting at the original hash value location, and moving sequentially through until an empty slot is found.

3. Performance of basic hash table operations
    Average is O(1 + a); this is because there is always the initial cost involved. If you can control the load factor,, you can keep operations at O(1)

4. Load factor
    Basically just how full a Hash table is. Number of inputs divided by number of slots. A good default can be something like 0.75, because of the trade-off between time and space costs. Basically you dont want to have a ton of unused slots, but you also dont want to accidentally max/cap, or it either breaks or is super inefficient.

5. Automatic resizing
    Essentially triggering a complete resize whenever the load factor passes the set threshold. A new table is made, everything is copied over, then the old one is emptied and returned to free storage.
    Incremental Resizing is a good way to deal with some of the issues that could come with needing to resize the entire thing at once(too much data, etc); basically its resizing in chunks so it can be making smaller changes consistently, rather than one full change all at once.

6. Various use cases for hash tables
    A great example I saw somehwere was coordinates for a map- huge amount of data, that would be much faster to search through if it was indexed instead.
    Another common one is any time you need to index items in an array or list.


We expect you to be able to answer questions in these areas. Your responses contribute to your Sprint Challenge grade.

## Instructions

### Task 1: Project Set-Up

- [ ] Create a forked copy of this project
- [ ] Add your team lead as a collaborator on Github
- [ ] Clone your OWN version of the repository (Not Lambda's by mistake!)
- [ ] Create a new branch: git checkout -b `<firstName-lastName>`.
- [ ] Implement the project on your newly created `<firstName-lastName>` branch, committing changes regularly
- [ ] Push commits: git push origin `<firstName-lastName>`

### Task 2: Project Requirements

Your finished project must include all of the following requirements:

- [ ] Solve any three of the five problems

For each problem that you choose to solve, complete the following:

- [ ] Navigate into each exercise's directory
- [ ] Read the instructions for the exercise in the README
- [ ] Implement your solution in the `.py` skeleton file
- [ ] Make sure your code passes the tests running the test script with make tests

*Note: For these exercises, we expect you to use Python's built-in `dict` as a hashtable. That said, if you wish, you can attempt to solve using your own hashtable implementation, as well. All solutions should utilize a `dict` or hashtable. You should not use Sets. (Though you can make a `dict` behave like a set if you wish.)*

### Task 3: Stretch Goals

After finishing your required elements, you can push your work further. These goals may or may not be things you have learned in this module, but they build on the material you just studied. Time allowing, stretch your limits, and see if you can deliver on the following optional goals:

- [ ] Solve any four of the five problems
- [ ] Solve all five problems

## Submission format

Follow these steps to complete your project.

- [ ] Submit a Pull-Request to merge <firstName-lastName> Branch into master (student's  Repo). **Please don't merge your own pull request**
- [ ] Add your team lead as a reviewer on the pull-request
- [ ] Your team lead will count the project as complete after receiving your pull-request

