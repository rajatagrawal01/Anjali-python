import timeit
import sys

demo_List= [1,2,3,"Indore","Dewas"]

demo_tuple=(1,2,3,"Indore","Dewas","MHOW")
print("First element",demo_tuple[0])
# print("List Before: ",demo_List)
# print("Tuple Before: ",demo_tuple)
# demo_List[0]=30
# demo_tuple[0]=20
# print("List After : ",demo_List)

print(timeit.timeit('[1,2,3,"Indore","Dewas"]'))
print(timeit.timeit('(1,2,3,"Indore","Dewas")'))

print(sys.getsizeof(demo_List))
print(sys.getsizeof(demo_tuple))

a=(1,2,3,4,5) # 1-D tuple

b=(
    (1,2,3,4,5),
    ("a","b","c","d"),
    ("!","@","#","$")
) # 2-D tuple

c=(
    (1,2,3,4,5),
    ("a","b","c","d"),
    ("!","@","#","$",
     ("Alpha","Beta","Gamma")
    )
) # 3-D tuple