# review
a = 1
b  = 1.2
z = 1 + 5j
text = "hello"

cond = True

lst = [1 ,True ,1.2 ,"hello" , 1000]


print(lst[3])

# a-z A-Z 0-9 _
#
# my_var = 10
# snake_case_naming
# camelCaseNaming
# PascalCaseNaming

var = text + a
# -------------------------------------------------------
# str_methods
text = "heLLo"


text_up = text.upper()
text_lo = text.lower()
print(text)

print(text.capitalize())
print(text_up)
print(text_lo)


print(text.center(100))
print(text.ljust(100))
print(text.rjust(100))

print(text.center(100, '-'))
print(text.ljust(100, '0'))
print(text.rjust(100, '*'))

poem = "nothing can ever happen twice"
res = poem.count("e")



# text.capitalize
# text.upper
# text.lower
# text.center
# text.ljust
# text.rjust




#-------------------------------------------------------------------------
# string_manipulation

poem = "nothing can ever happen twice"
word = "ever"

poem_2 = poem.replace("ever", "EVER")
print(poem_2)



indx_start = poem.index(word)
indx_stop = indx_start + len(word)

new_poem = poem[:indx_start] + word.upper() + poem[indx_stop:]

print(new_poem)


#-------------------------------------------------------------------------
# test list
lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7]
lst3 = lst1 + lst2
print(lst3[-2])

print(lst3)
lst3[-2] = 1000    # mutable object
print(lst3)
# test_str
text = "hello world! whatever"
print(text[1])
length_of_text = len(text)
# print(length_of_text )
out = text[6] + text[7] + text[8] + text[9] + text[10]
print(out)



#-------------------------------------------------------------------------
# test_tuple
tup1 = (1, 2, 3, 4, 5)
tup2 = (6, 7)
tup3 = tup1 + tup2
print(tup3[-2])
print(tup3)
tup3[-2] = 1000   # immutable object
print(tup3)

#-------------------------------------------------------------------------
# tuple_methods
tup = (1, 2, 3, 4, 5, 1, 1, 1)
repeats = tup.count(1)
indx = tup.index(3)

print(indx)
print(repeats)



#-------------------------------------------------------------------------
# tuple_slice_and_concate
tup = (0, 1, 2 ,3, 4 ,5, 6, 7, 8, 9, 10,)
tup_new = tup[:6] + (1000,) + tup[7:]
print(tup_new)


#-------------------------------------------------------------------------
# conditions
num1 = 100
num2 = 200

n = 200

cond = (n > num1) and (n < num2)
print(cond)

cond = not ((n <= num1) or (n >= num2))
print(cond)


text1 = "HELLO"
text2 = "hello"

text1.isupper() and text2.islower()




#-------------------------------------------------------------------------
# convert
tup = (1, 2, 3, 4)
lst = list(tup)

lst[1] = 1000
print(lst)
tup_new = tuple(lst)
print(tup_new)


#-------------------------------------------------------------------------
# list_methods.
lst = [1, "whatever", 2, 3, 4, 5]

lst[1] = "hello"




#-------------------------------------------------------------------------
# mutable_objects_assignment
list_a = [1, 2, 3, 4]
list_b = list_a
list_b[1] = 1000
print(list_a)    # [1, 1000, 3, 4]




