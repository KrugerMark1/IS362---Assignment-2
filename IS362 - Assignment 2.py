
#!/usr/bin/env python
# coding: utf-8

# Week 2 - One aspect of data structures that I find challenging is slicing.
# Array slicing allows you to access several values contained in an array at the same time. When invoking the index, the colon operator : is used to extract a section or slice of an array.

<slice> = <array>[start:stop]


# Where <slice> is the slice or section of the array object <array>. The index of the slice is specified in [start:stop].

# The following is an example of slicing the first two elements of an array.

import numpy as np

a = np.array([2, 4, 6])
b = a[0:2]
print(b)


# Since Python counting starts at 0 and ends at n-1. The index [0:2] retrieves the array's first two values. The index [1:3] retrieves the array's second and third values.




