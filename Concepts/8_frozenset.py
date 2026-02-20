"""
Frozenset: We already have option to store multiple values like list of employee names.
        - We can store UNIQUE values
        - We don't have index number to each values
        - It is unordered

"""

print("frozenset PART-1")
print("How to store values")
print("-"*20)
# ---------------

# We don't have shortcut for 'frozenset' class,
# so we need to use class name to create object
my_fs = frozenset([10, 10, 10, "python", "python", "Java", "Java"])
print("my_fs: ", my_fs, end="\n\n")

# if we want index number then convert to other type like tuple/list
my_list = list(my_fs)
print("my_list", my_list, end="\n\n")

print("#"*40, end="\n\n")
############################

print("frozenset PART-2")
print("Methods present inside frozenset class")
print("-"*20)
# ---------------

print(dir(frozenset))
# OR
print(dir(my_fs))

print("#"*40, end="\n\n")
############################

print("frozenset PART-3")
print("union, intersection, difference methods")
print("-"*20)
# ---------------

java_course_candidates = frozenset(["emp-1", "emp-2", "emp-3", "emp-4"])
python_course_candidates = frozenset(["emp-3", "emp-4", "emp-5", "emp-6"])
print("java_course_candidates: ", java_course_candidates, end="\n\n")
print("python_course_candidates: ", python_course_candidates, end="\n\n")

# all employees
all_employees = java_course_candidates.union(python_course_candidates)
print("all_employees: ", all_employees, end="\n\n")

# employees enrolled for both the courses
employees_enrolled_for_both = java_course_candidates.intersection(python_course_candidates)
print("employees_enrolled_for_both: ", employees_enrolled_for_both)

# enrolled only for java
enrolled_only_for_java = java_course_candidates.difference(python_course_candidates)
print("enrolled_only_for_java: ", enrolled_only_for_java)

print("#"*40, end="\n\n")
############################