#!/usr/bin/python

"""
[1, 5, 10, 25, 50]
0
===== 1
0

1
===== 1
1

5
======= 2
5
1 1 1 1 1

10
======== 4
10
5 5
5 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1

15
======== 6
10 5
10 1 1 1 1 1
5 5 5
5 5 1 1 1 1 1
5 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1

20
======= 9
10 10
10 5 5
10 5 1 1 1 1 1
10 1 1 1 1 1 1 1 1 1 1
5 5 5 5
5 5 5 1 1 1 1 1 1 1 1 1 1
5 5 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
5 1 1 1 11 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 11
111 1 1 11 1 1 1 1 11 11 11  1111 11

25
====== 13
25
10 10 5
10 10 1 1 1 1 1
10 5 5 5
10 5 5 1 1 1 1 1
10 5 1 1 1 1 1 1 1 1 1 1
10 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
5 5 5 5 5
5 5 5 5 1 1 1 1 1 1 1 1 1 1
5 5 5 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
5 5 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
5 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1

"""
import sys

#reference https://www.youtube.com/watch?v=jaNZ83Q3QGc
def making_change(amount, denominations):
  comb = [0] * (amount + 1)
  
  comb[0] = 1
  for i in denominations:
    for j in range(1, len(comb)):
        if j >= i:
          comb[j] += comb[j - i]
    

  return comb[amount]



if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")