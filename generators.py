'''
To get the generator object we use () brackets
to get list comprehension we use []
to convert generator to list use list(generator_name)
genertors are better in performance, since they do not hold all the values
in memory. List calulates everything and holds values in memory

generator basically uses yield concept and generates only first value
when we try to fetch the next value it generates next results entries
advantage is generator does not fill the memory with the results.

Discussion:
As soon as the yield is put the loop stops right there.
Later on when I iterated over the generator,
it is then when it consumed the time
'''

'''------ conventional way ---------
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return  result


my_nums = square_numbers([1,2,3,4,5])
print my_nums
#-------------------------------------'''

'''---------- simple generator example -----------

def square_numbers(nums):
    for i in nums:
        yield (i*i) # it just generates the first result
        # Next results are generated as we try to access it.

my_nums = square_numbers([1,2,3,4,5])
print my_nums   # it just prints the generator object

# print each element from generator. It is produced as we try to access it.
print next(my_nums) # 1
print next(my_nums) # 4
# print next(my_nums) # 9
# print next(my_nums) # 16
# print next(my_nums) # 25

# iterate over the generator
for num in my_nums:
    print num,
-----------------------------------------'''

# ----- List comprehension-----
# see the video again to see conversion between generator and list
# ref - https://www.youtube.com/watch?v=bD05uGo_sVI
my_nums = (x*x for x in [1,2,3,4,5])

#print list(my_nums) # [1, 4, 9, 16, 25]

for num in my_nums:
    print num
