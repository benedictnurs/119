"""
Lecture 1: Introduction to data processing pipelines

=== Poll ===

Today's poll is to help me understand your background in Python and command line/Git.
(I will also ask about your background in HW0.)

https://forms.gle/h53wSrkeaM4R28Gu9
https://tinyurl.com/ypevcu9u

=== Following along ===

Try this!

1. You will need to have Git installed (typically installed with Xcode on Mac, or with Git for Windows). Follow the guide here:

    https://www.atlassian.com/git/tutorials/install-git

    Feel free to work on this as I am talking and to get help from your neighbors.
    I can help with any issues after class.

2. You will also need to create an account on GitHub and log in.

3. Go to: https://github.com/DavisPL-Teaching/119

4. If that's all set up, then click the green "Code" button, click "SSH", and click to copy the command:

    git@github.com:DavisPL-Teaching/119.git

5. Open a terminal and type:

    git clone git@github.com:DavisPL-Teaching/119.git

6. Type `ls`.

    You should see a new folder called "119" in your home folder. This contains the lecture notes and source files for the class.

7. Type `cd `119/lecture1`, then type `ls`.
   Lastly type `python3 lecture.py`. You should see the message below.
"""

# CUT -- moved to bottom
# print("Hello, ECS 119!")

"""
If some step above didn't work, you may be missing some of the software we
need installed. Please complete HW0 first and then let us know if you
are still having issues.

=== The basics ===

I will introduce the class through a basic overview, or "toy model"
of what a data procesisng pipeline is. Throughout, we will also see
some of the constraints that data processing pipelines have to satisfy,
how they interact with one another, and so on.
This will lead to an overview of topics covered in the class.

Recall "discussion scenarios" from the previous lecture.

EXAMPLE 1:
I have a spreadsheet containing 1000 movies I have seen or want to see,
dates watched, and movie ratings.
I built a Python application which loads the spreadsheet,
filters out movies based on a recently viewed or highest-rated sorting,
and allows me to mark a movie as seen or to edit any movie ratings.
It also collects statistics about all the movies.
All of this data is then saved back to the spreadsheet.

EXAMPLE 2:
I have written a website scraper that reads data from Wikipedia.
I re-run the scraper every week to get the latest data.
It opens up all Wikipedia sites that correspond to cities in the world,
extracts the population of each city, the area, and the country it is located
in. Once all of this data is collected, it stores it in a structured
format and saves it to a database, then queries the database for the
top 100 most population-dense cities and outputs these to a file
biggest_cities.txt.

What do these scenarios have in common?
Suggestions:
- Write the data to CSV
- ...

<<<<<<< Updated upstream
3 stages -- related to something called the "Extract, Transform, Load" model (ETL)

What are the components of a data processing pipeline?

0. Description of the task that you want to complete.
1. Input source -- get your input from somewhere
2. Processing stage -- do some transformations on your data,
    add additional data fields, modify fields, calculate summary
    statistics, etc.
3. Output -- save the results to a file or a database; display
    them to the user; etc.
=======
3 Stages:
ETL (Extract, Transform, Load)

1.Input
2.Processing
3.Output

>>>>>>> Stashed changes
"""

"""
Step 1: Getting a data source

Useful sites:
- https://ourworldindata.org/data
- sklearn
"""

# # Load the data from life-expectancy.csv into a pandas DataFrame
# # Pandas documentation:
# # https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
# import pandas as pd
# df = pd.read_csv("life-expectancy.csv")

# # Print the first 5 rows of the DataFrame
# print("Hello")
# print(df.head())

"""
Step 2: Do some processing
"""

# # Print keys
# print(df.keys())

# min_year = df["Year"].min()
# max_year = df["Year"].max()

# print("Minimum year: ", min_year)
# print("Maximum year: ", max_year)

# avg = df["Period life expectancy at birth - Sex: all - Age: 0"].mean()

# print("Average life expectancy: ", avg)

"""
Stage 3. Save the output
"""

# out = pd.DataFrame({"Min year": [min_year], "Max year": [max_year], "Average life expectancy": [avg]})
# out.to_csv("output.csv", index=False)

# # (Side note on gitignore)

"""
Graphical view

We can view all of the above steps as something called
a directed acyclic graph (DAG).
What do I mean and how?

It's a flow chart of input sources,
processing stages (often called "operators"),
and outputs.

                       -> min ->
(life-expectancy.csv)  -> max ->  output.csv
                       -> avg ->

Why is this useful?

- We'll use this to think about parallelism
- We'll use this to think about performance.

=== Recap of what we covered today ===

- Any data processing pipeline can be thought of as having 3 stages:
    input source, processing, and output
- Data processing pipelines can be drawn as directed acyclic graphs (DAGs).

=======================================================================

=== Monday, September 30 ===

(See README.md for announcements and plan.)

=== Following along ===

Reminder to follow along:
https://github.com/DavisPL-Teaching/119

(I will go through the steps again in class)

Navigate to the directory you want:
- ls to show directories
- cd <directory> to move into the directory

If you already cloned the repo, then this time, you need to get any code updates.
Do the following:

- git status
- git stash
- git pull

=== A tangent on pacing ===

- The pacing might be a bit slow right now for some of you -- especially if you have prior experience
  with Python, pandas, Git, etc.
  (HW0 results so far: 100% have used Python, 80% Pandas, 75% Git)

- We do have varying levels of background including some who have not used some of these tools
  before. So please be patient with us for the first few lectures.

- 80% of you have only limited experience with command line in particular, so we will spend some additional
  time in Lecture 2 on software development tools.

- There will be a mid-quarter survey (around 4 weeks in) to see if we are going too slow or too fast
  and I will adjust things accordingly!

=== Poll ===

1. Which stage do you think is likely to be the most computationally intensive part of a data processing pipeline?

2. Which ostage do you think is likely to present the biggest opportunity for failure cases, including crashes, ethical concerns or bias, or unexpected/wrong/faulty data?

https://forms.gle/Kv39iq33KDjJy3ir6
https://tinyurl.com/3tthzry7

=== Data processing pipelines as software ===

Some of you may know about tools like Jupyter notebooks, Google Colab, or Excel.
(What is the most widely used data processing tool? Answer: Excel)

So why aren't we using those tools? :)

In this course, I want to encourage us to think about data processing pipelines as real software.
That means:
- Software *design* matters: structuring code into modules, classes, functions
- Software can be *tested*: validating functions, validating inputs, unit & integration tests
- Software can be *reused* and maintained (not just a one-off script)
- Software can be developed collaboratively (Git, GitHub)
- Software can be optimized for performance (parallelism, distributed computing, etc.)

It is a little more work to structure our code this way!
But it helps ensure that our work is reusable and integrates well with other teams, projects, etc.

Let's consider how to write the minimal data processing pipeline we saw last time
as a more structured software pipeline.

Useful tutorial on Pandas:
https://pandas.pydata.org/docs/user_guide/10min.html
https://pandas.pydata.org/docs/user_guide/indexing.html
"""

import pandas as pd

# Step 1: Getting a data source
# creating a DataFrame
# DataFrame is just a table: it has rows and columns, and importantly,
# each column has a type (all items in the column must share the same
# type, e.g., string, number, etc.)
# df = pd.read_csv("life-expectancy.csv")

def get_life_expectancy_data(filename):
    """
    This is called a docstring

    Take in CSV data from life-expectancy.csv
    Return a DataFrame of the data.
    """
    df = pd.read_csv(filename)
    return df

"""
Running the code

It can be useful to have open a Python shell while developing Python code.

There are two ways to run Python code from the command line:
- python3 lecture.py
- python3 -i lecture.py

Let's try both
"""

# Step 2: Do some processing
# min_year = df["Year"].min()
# max_year = df["Year"].max()
# print("Minimum year: ", min_year)
# print("Maximum year: ", max_year)
# avg = df["Period life expectancy at birth - Sex: all - Age: 0"].mean()
# print("Average life expectancy: ", avg)

class LifeExpectancyData:
    """
    Our data will include:
    - maximum year
    - minimum year
    - average of all the life expectancies
    """

    def __init__(self):
        """
        Initialize fields

        self keyword: refers to the object itself
        """
        self.min = None
        self.max = None
        self.avg = None

    def load_statistics(self, df):
        """
        Read in data from the DataFrame
        and store it in our clas
        """
        self.min = df["Year"].min()
        self.max = df["Year"].max()
        self.avg = df["Period life expectancy at birth - Sex: all - Age: 0"].mean()

    def save_to_file(self, filename):
        out = pd.DataFrame({
            "Min year": [self.min],
            "Max year": [self.max],
            "Average life expectancy": [self.avg],
        })
        out.to_csv(filename, index=False)

    def get_from_user(self):
        # Instead of loading from a file, get the data via user input.
        raise NotImplementedError

# Tangent:
# We can do all of the above with df.describe()

# Step 3: save the output
# out = pd.DataFrame({"Min year": [min_year], "Max year": [max_year], "Average life expectancy": [avg]})
# out.to_csv("output.csv", index=False)
# Do this above

"""
Let's revisit our criteria from before. How does this help?
"""

# - Software design

# Exercise 1: Revise the class above so that the input is taken from an argument, instead of
# provided as a hardcoded filename

# - Software testing

# Exercise 2: Validate the the input has the correct number of countries.
# (Q: What is the correct number? A: More on this in a bit)

# We can use pytest for testing
# conda list pytest
# conda install pytest
import pytest

# How pytest works:
# Any function with the prefix test_ is considered
# a test.
# We can run all tests with pytest lecture.py
# We can use @pytest.mark.skip decorator to skip
# tests -- nskip to run test
# @pytest.mark.skip
def test_get_life_expectancy_data():
    data = get_life_expectancy_data("life-expectancy.csv")
    countries = data["Entity"].unique()
    assert len(countries) == 261

# 261 countries!
# (This is a property of our dataset -- which countries
# get included or not is a geopolitical and ethical question)

# - Software reuse

# Exercise 3:
# Reuse the class to get input in a different way: from the user
# TODO try this exercise.

"""
Recap of what we covered today:

- Data processing pipelines as software

- Software design best practices, modularity, and reuse

- A little bit about data validation -- i.e. determining whether
  whatever assumptions we have about the data may actually be
  correct.

===============================================================

=== Wednesday, Oct 2 ===

Once again, to follow along: git stash, git pull

=== Poll ===

Which of the following is a good reason to structure data processing software using well-abstracted modules, functions, and classes? (select all that apply)

- (options cut)

https://forms.gle/q33kY95XQjUNGk8A6
https://tinyurl.com/4x7pvkr6
"""

# (Finishing up)
# Reasons to think of data processing pipelines as software:

# - Collaborative development
#   Why is the above code design better for collaborative development?

# - Performance optimization
#   (More on this shortly)

# - In general: anticipating things that could go wrong
#   (this point is a good transition to the next section)

"""
=== Main function ===

Last time, we used python3 -i lecture.py to run
the code interactively.

Let's look at another common way to test out our Python code
by putting a basic pipeline into a main function at the
bottom of the file.
"""

"""
=== Failures and risks ===

Recall that we talked on the first lecture about software components + design constraints.

More specifically, we are most worried about failures and risks
which might invalidate our pipeline (wrong results)
or cause it to misbehave (crash or worse).

What could go wrong in our toy pipeline above?
Let's go through each stage at a time:

1. Input stage

What could go wrong here?

- Malformed data and type mismatches
- Wrong data
- Missing data
- Private data
"""

"""
Problem: input data could be malformed
"""

# Exercise 4: Insert a syntax error by adding an extra comma into the CSV file. What happens?

# A: that row gets shifted over by one
# All data in each column is now misaligned;
# some columns contain a mix of year and life expectancy data.

# Exercise 5: Insert a row with a value that is not a number. What happens?

# A: changing the year on just one entry to a string,
# the "Year" field turned into a string field.

# Reminder about dataframes: every column has a uniform
# type. (Integer, string, real/float value, etc.)

# Take home point: even a single mislabeled or
# malformed row can mess up the entire DataFrame

# Solutions?

# - be careful about input data (get your data from
# a good source and ensure that it's well formed)

# - validation: write and run unit tests to check
#   check that the input data has the properties we
#   want.

# e.g.: write a test_year function that goes through
# the year column and checks that we have integers.

"""
Problem: input data could be wrong
"""

# Example:
# Code with correct input data:
# avg. 61.61799192059744
# Code with incorrect input data:
# avg.: 48242.7791579047

# Exercise 6: Delete a country or add a new country. What happens?

# Deleting a country:
# 61.67449487559832 instead of 61.61799192059744
# (very slightly different)

# Solutions?

# Put extra effort into validating your data!

"""
Discussion questions:
- If we download multiple versions of this data
  from different sources (for example, from Wikipedia, from GitHub,
  etc.) are they likely to have the same countries? Why or why not?

- What can be done to help validate our data has the right set
  of countries?

- How might choosing a different set of countries affect the
  app we are using?

Recap from today:

- Python main functions (ways to run code: python3 lecture.py (main function), python3 -i lecture.py (main function + interactive), pytest lecture.py to run unit tests)
- what can go wrong in a pipeline?
- input data issues & validation.

===============================================================

=== Friday, Oct 4 ===

Following along: git stash, git pull

=== Poll ===

1. Which of the following are common problems with input data that you might encounter in the real world and in industry?

- (poll options cut)

(Just for fun:)
2. How many countries are there in the world?

https://forms.gle/QRbiL3cJm6iKkxsW6
https://tinyurl.com/5n95yyku

Common answers:

- 193: UN Members
- 195: UN Members + Observers
- 197: UN Members + Observers + Widely recognized
- 200-300something: if including all partially recognized countries or territories.

As we saw before, our dataset happens to have 261.
- e.g.: our dataset did not include all countries with some form of
  limited recognition, e.g. Somaliland
  but it would include the 193, 195, or 197 above.

Further resources:

- https://en.wikipedia.org/wiki/List_of_states_with_limited_recognition

- CGP Grey: How many countries are there? https://www.youtube.com/watch?v=4AivEQmfPpk

In any dataset in the real world, it is common for there to be some
subjective inclusion criteria or measurement choices.

"""

"""
2. Processing stage

What could go wrong here?

- Software bugs -- pipeline is not correct (gives the wrong answer)
- Performance bugs -- pipeline is correct but is slow
- Nondeterminism -- pipelines to produce different answers on different runs

    This is actually very common in the data processing world!
    - e.g.: your pipeline may be a stream of data and every time you run
    it you are running on a different snapshot, or "window" of the data
    - e.g.: your pipeline measures something in real time, such as timing
    - a calculation that requires a random subset of the data (e.g.,
      statistical random sample)
    - Neural network?
    - Running a neural network or large language model with different versions
      (e.g., different version of GPT every time you call the GPT API)
    - ML model with stochastic components
    - Due to parallel and distributed computing
        If you decide to parallelize your pipeline, and you do it incorrectly,
        depending on the order in which different operations complete you
        might get a different answer.

"""

"""
3. Output stage

What could go wrong here?

- System errors and exceptions
- Output formatting
- Readability
- Usability

Often output might be: saving to a file or saving to a database, or even
saving data to a cloud framework or cloud provider;
and all of three of these cases could fail.
e.g. error: you don't have permissions to the file; file already exists;
not enough memory on the machine/cloud instance; etc.

Summary: whenever saving output, there is the possibility that the save operation
might fail

Output formatting: make sure to use a good library!
Things like Pandas will help here -- formatting requirements already solved

When displaying output directly to the user:
- Are you displaying the most relevant information?
- Are you displaying too much information?
- Are you displaying too little information?
- Are you displaying confusing/incomprehensible information?

e.g.: displaying 10 items we might have a different strategy than if
we want to display 10,000

example: review dataframe display function
    - dataframe: display header row, first 5 rows, last 5 rows
    - shrink the window size ==> fields get replaced by "..."

There are some exercises at the bottom of the file.

=== Rewriting our pipeline one more time ===

Before we continue, let's rewrite our pipeline one last time as a function
(I will explain why in a moment -- this is so we can easily measure its performance).

"""

# Rewriting our pipeline one last time, as a single function
def pipeline(input_file, output_file):
    # 1. Input stage
    df = get_life_expectancy_data(input_file)

    # 2. Processing stage
    stats_summary = LifeExpectancyData()
    stats_summary.load_statistics(df)

    # 3. Output stage
    stats_summary.save_to_file(output_file)

"""
=== Performance ===

In the second stage, we said that one thing that could
go wrong was performance bugs.
How do we measure performance?

Three key performance metrics:

- Throughput

    What is throughput?
    How fast the pipeline runs, measured per input row or input item.

    Running time almost always varies depending on the size of the input
    dataset!
    Often linear: the more input items, the longer it will take to run
    So it's useful to think about the time per input item.

    Throughput is the inverse of this:
    Definition / formula:
        (Number of input items) / (Total running time).

Let's take our pipeline and measure the total running time & the throughput.
"""

# Use the timeit library -- library that allows us to measure the running
# time of a Python function
import timeit

def f():
    pipeline("life-expectancy.csv", "output.csv")

# timeit.timeit(f, number=100)
# We see a linear behavior!
# 100 times: 0.35s
# 1000 times: 3.28s
# 10000 times: 33.4s
# Running time is roughly linear in the size of the input!

def measure_throughput():

    # Get the number of input items
    # Hardcoded
    num_input_items = 20755

    # Get the number of runs
    # Hardcoded
    num_runs = 1000

    execution_time = timeit.timeit(f, number=num_runs)

    print(f"Execution time for {num_runs}: {execution_time}")

    print(f"Execution time per input run: {execution_time / num_runs}")

    ans = execution_time / (num_runs * num_input_items)
    print(f"Execution time per input run, per input data item (1/throughput): {ans}")

    # The actual number we want: throughput
    print(f"Throughput: {1 / ans} items/second")

    # Answer: about 6,000,000 items (or rows) per second!
    # Pandas is very fast.

"""
- Latency

- Memory usage

Let's measure the performance of our toy pipeline.

Timeit:
https://docs.python.org/3/library/timeit.html

Example syntax:
timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
"""

def measure_latency(pipeline):
    raise NotImplementedError

def measure_memory_usage(pipeline):
    # There are ways to do this in Python through external libraries.
    # We will cover this later.

    raise NotImplementedError

"""
=== Additional exercises (skip depending on time) ===
"""

"""
Problem: input data could be missing
"""

# Exercise 7: Insert a row with a missing value. What happens?

# Solutions?

"""
Problem: input data could be private
"""

# Exercise 8: Insert private data into the CSV file. What happens?

# Solutions?

"""
Problem: software bugs
"""

# Exercise 9: Introduce a software bug

# Solutions?

"""
Problem: performance bugs
"""

# Exercise 10: Introduce a performance bug

# Solutions?

"""
Problem: order-dependent and non-deterministic behavior
"""

# Exercise 11: Introduce order-dependent behavior into the pipeline

# Exercise 12: Introduce non-deterministic behavior into the pipeline

# Solutions?

"""
Problem: output errors and exceptions
"""

# Exercise 13: Save the output to a file that already exists. What happens?

# Exercise 14: Call the program from a different working directory (CWD)
# (Note: CWD)

# Exercise 15: Save the output to a file that is read-only. What happens?

# Exercise 16: Save the output to a file outside the current directory. What happens?

# (other issues: symlinks, read permissions, busy/conflicting writes, etc.)

# Solutions?

"""
Problem: output formatting

Applications must agree on a common format for data exchange.
"""

# Exercise 17: save data to a CSV file with a wrong delimiter

# Exercise 18: save data to a CSV file without escaping commas

# Solutions?

"""
Problem: readability and usability concerns --
    too much information, too little information, unhelpful information
"""

# Exercise 19: Provide too much information as output

# Exercise 20: Provide too little information as output

# Exercise 21: Provide unhelpful information as output

# Solutions?

"""
=== Overview of the rest of the course ===

Overview of the schedule (tentative), posted at:
https://github.com/DavisPL-Teaching/119/blob/main/schedule.md

=== Closing quotes ===

From Patrice Koehl:
https://www.cs.ucdavis.edu/~koehl/:

    "Where is the wisdom we have lost in knowledge?
    Where is the knowledge we have lost in information?
    Where is the information we have lost in data?"

    With apologies to T.S. Eliot.

Data processing is all about extracting wisdom from data.
But each of these steps can go wrong!

From Edsgar Dijkstra:

    "Simplicity is a great virtue but it requires hard work to achieve it and education to appreciate it. And to make matters worse: complexity sells better."

I'd like to encourage us to think about how to build pipelines that are as *simple* as possible
-- organized into careful components, with helpful abstractions -- rather than having
expanding components and needless complexity.

Why? Simpler pipelines are more reliable, easier to develop, easier to understand, and easier to maintain.

Tools are adopted not just because of what they can do, but because of how much they can do in the most
intuitive and direct way possible.

The tools we see in this class will help us achieve the right abstractions to achieve this simplicity.

"""

# What a main function is: the default thing that you run when
# running a program.
# Sometimes called an "entrypoint"
# __name__: a variable that stores the name of the module being run

# print("Hello from outside of main function")

if __name__ == "__main__":
    # Insert code here that we want to be run by default when the
    # program is executed.

    # print("Hello from inside of main function")

    print("Hello, ECS 119!")

    # What we can do: add additional code here
    # to test various functions.
    # Simple & convenient way to test out your code.

    # Call our pipeline
    pipeline("life-expectancy.csv", "output.csv")

# Test file: main_test.py

# What have we found? If importing lecture.py as
# a library, the main function (above) doesn't get run.
# If running it directly from the terminal,
# the main function does get run.
