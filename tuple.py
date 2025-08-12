import timeit
import sys

demo_List= [1,2,3,"Indore","Dewas"]

demo_tuple=(1,2,3,"Indore","Dewas","MHOW")

# print("List Before: ",demo_List)
# print("Tuple Before: ",demo_tuple)
# demo_List[0]=30
# demo_tuple[0]=20
# print("List After : ",demo_List)

print(timeit.timeit('[1,2,3,"Indore","Dewas"]'))
print(timeit.timeit('(1,2,3,"Indore","Dewas")'))

print(sys.getsizeof(demo_List))
print(sys.getsizeof(demo_tuple))