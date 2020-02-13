#!/usr/bin/python

"""
Python Core object Types
"""

import math

def numbers_and_strings():
    """
    This is to review numbers and strings and basic operations.
    """
    # Assign a string "EE551" to a variable x
    x = "EE551"

    # Assign a string "Stevens" to a variable y
    y = "Stevens"

    # Repeat variable y 5 times
    z = y * 5

    # What is the length of z?
    length = len(z)

    # Concatenate variable y with string " is good"
    m = y + " is good"

    # Replace "good" with "awesome" in variable m and assign it to a new variable n
    n = m[:11] + "awesome"

    return x, y, z, length, m, n

(x, y, z, length, m, n) = numbers_and_strings()
print(x, y, z, length, m, n)

def lists():
    """
    This is to review basic operations with lists.
    """
    n = "Stevens is awesome"

    # Split variable n on a delimiter space into a list of substrings
    p = n.split(' ')
    # Get all the items past the first of the third substring
    r = p[2][1:]
    # Create a 3 x 3 matrix as nested list such that
    #   first row is [1, 4, 5]
    #   second row is [6, 10, 11]
    #   third row is [12, 17, 38]
    fr = [1, 4, 5]
    sr = [6, 10, 11]
    tr = [12, 17, 38]
    A = [fr, sr, tr]
    # Collect the items in the last column of matrix A using list comprehension
    c = A[2]
    # Collect only the even items of the diagonal of matrix A using list comprehension
    diagnal = []
    for i in range(len(A)):
        diagnal.append(A[i][i])
    d = []
    for i in diagnal:
        if i % 2 == 0:
            d.append(i)
    # We can convert a single character to its underlying integer code (e.g., its ASCII byte value)
    # by passing it to the built-in ord function. Generate a list of these integers to represent
    # each character of the string "Stevens" using list comprehension.
    raw = "Stevens"
    o = []
    for item in raw:
        o.append(ord(item))
    return p, r, c, d, o

(p, r, c, d, o) = lists()
print(p, r, c, d, o)

def dictionaries():
    """
    This is to review basic operations with dictionaries.
    """
    # Create a dictionary that maps:
    #   fruit => "apple"
    #   quantity => 4
    #   color => "green"
    my_dict = {'fruit': 'apple', 'quantity': 4, 'color': "green"}
    # Get the item in dictionary f that the key "fruit" maps to
    a = my_dict['fruit']
    # Increase the quantity of f by 1
    # IMPLEMENT IT HERE
    my_dict['quantity'] += 1
    f = my_dict['quantity']
    # Create a nested dictionary where:
    #   name => {first_name => "Grace", last_name => "Hopper"} (a dictionary)
    #   jobs => ["scientist", "engineer"] (a list)
    #   age => 85
    n_dict = {'name': {'first_name': 'Grace', 'last_name': 'Hopper'}, 'jobs': ['scientist', 'engineer'], 'age': 85}
    # Add "programmer" to the list of jobs Grace has
    # IMPLEMENT IT HERE
    n_dict['jobs'].append('programmer')
    # Get the third job Grace has that you recently added
    p = n_dict['jobs'][2]
    # Use the sort() function to get sorted keys of amazing_grace in alphabetically ascending order
    key = 'amazing_graze'
    k = list(key)
    #k = list(n_dict.keys())
    k.sort()
    return a, f, p, k

(a, f, p, k) = dictionaries()
print(a, f, p, k)





