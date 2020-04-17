#!/usr/bin/python

"""
0
======
[[]]

1
======
[['rock'], ['paper'], ['scissors']]

2
=====
[['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'], 
['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'], 
['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]

3
====
 [['rock', 'rock', 'rock'], ['rock', 'rock', 'paper'], ['rock', 'rock', 'scissors'], 
 ['rock', 'paper', 'rock'], ['rock', 'paper', 'paper'], ['rock', 'paper', 'scissors'], 
 ['rock', 'scissors', 'rock'], ['rock', 'scissors', 'paper'], ['rock', 'scissors', 'scissors'], 
 ['paper', 'rock', 'rock'], ['paper', 'rock', 'paper'], ['paper', 'rock', 'scissors'], 
 ['paper', 'paper', 'rock'], ['paper', 'paper', 'paper'], ['paper', 'paper', 'scissors'], 
 ['paper', 'scissors', 'rock'], ['paper', 'scissors', 'paper'], ['paper', 'scissors', 'scissors'], 
 ['scissors', 'rock', 'rock'], ['scissors', 'rock', 'paper'], ['scissors', 'rock', 'scissors'], 
 ['scissors', 'paper', 'rock'], ['scissors', 'paper', 'paper'], ['scissors', 'paper', 'scissors'], 
 ['scissors', 'scissors', 'rock'], ['scissors', 'scissors', 'paper'], ['scissors', 'scissors', 'scissors']]
"""
import sys

def rock_paper_scissors(n, cached=None):
  if cached is None:
    cached = [None] * (n + 1)
  def inner(arr):
      rps=[]
      for i in [['rock'], ['paper'], ['scissors']]:
        for j in arr:
          rps.append(i+j)
      return rps
  if n <= 0:
    return [[]]
  
  if cached[n] is None:
    cached[n] = rock_paper_scissors(n-1)
  arr = inner(cached[n])   
  return arr


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')