#=============functions and properties==========
import random
arr = [1, 2, 3, 4, 5, 6, 7, 8]
random.choice(arr)#5 or 8
random.choice(arr, 3)# [9, 2, 1]
random.shuffle(arr)# [2, 6, 3, 8, 5, 4, 7, 1]
random.randint(0, 10)#0..10



#===============================================



def drop_first_last(grades):
  first, *middle, last = grades
  return middle

arr = drop_first_last(['a', 'c', 'd', '...', 'z'])

print(arr)

#=======================================================

*trailing_qtrs, current_qtr = sales_record
trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
return avg_comparison(trailing_avg, current_qtr)

#=======================================================

prices = {
  'ACME': 45.23,
  'AAPL': 612.78,
  'IBM': 205.55,
  'HPQ': 37.20,
  'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
# min_price is (10.75, 'FB')

max_price = max(zip(prices.values(), prices.keys()))
# max_price is (612.78, 'AAPL')

prices_sorted = sorted(zip(prices.values(), prices.keys()))

print(min_price)
print(max_price)

print(prices_sorted)

print(min(prices))
print(max(prices))

print(prices.values())

#========================================================

a = {
   'x' : 1,
   'y' : 2,
   'z' : 3
}

b = {
   'w' : 10,
   'x' : 11,
   'y' : 2
}

# Find keys in common
print(a.keys() & b.keys())   # { 'x', 'y' }

# Find keys in a that are not in b
print(a.keys() - b.keys() )  # { 'z' }

# Find (key,value) pairs in common
print(a.items() & b.items()) # { ('y', 2) }

#========================================================

a = {
   'x' : 1,
   'y' : 2,
   'z' : 3
}

b = {
   'w' : 10,
   'x' : 11,
   'y' : 2
}


# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
# c is {'x': 1, 'y': 2}

print(c)

#=========================================================

a = [1, 1, 1, 1, 1, 1, 1, 2]


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

print(list(dedupe(a)))

#=========================================================

arr = [0, 1, 2, 3, 4, 5, 6]

a = slice(3, 5)

print(arr[a])#[3, 4]

arr[a] = [10, 11]

print(arr)#[0, 1, 2, 10, 11, 5, 6]

del arr[a]
print(arr)#[0, 1, 2, 5, 6]

#==========================================================

arr = [(2, 3), (2, 2), (3, 3)]

from operator import itemgetter


itemcount = itemgetter(0)

print(list(map(itemcount, arr)))
print(sorted(arr, key=itemcount))

#==========================================================

import math

arr = [1, -6, 9, 45, 0, 43, -5, -1, 'aasd', '6', '0', '-', '9']

def is_int(x):
  try:
    u = int(x)
    return True
  except:
    return False

parse = list(filter(is_int, arr))

data = []

for i in parse:
  data.append(int(i))

print(list(map(int, [math.sqrt(n) for n in data if n > 0])))#[1, 3, 6, 6, 2, 3]

#==========================================================

prices = {
  'ACME': 45.23,
  'AAPL': 612.78,
  'IBM': 205.55,
  'HPQ': 37.20,
  'FB': 10.75
}

p1 = {key:value for key, value in prices.items() if key.startswith('A')}

print(' '.join(list((str(value) for value in p1.values()))))#612.78 45.23