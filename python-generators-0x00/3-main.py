#!/usr/bin/python3
from itertools import islice
lp = __import__('2-lazy_paginate')

for page in islice(lp.lazy_paginate(5), 3): # Only grab 3 pages of 5 users