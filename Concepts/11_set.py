"""
set: We already have option to store multiple values like list of employee names.
        - We can store UNIQUE values
        - We don't have index number to each value
        - It is unordered
"""

print("set PART-1")
print("How to store values")
print("-"*20)
# ---------------

my_set = {10, 10, 10, "python", "python", "Java", "Java"}
print("my_set: ", my_set, end="\n\n")
# OR
my_set = set([10, 10, 10, "python", "python", "Java", "Java"])
print("my_set: ", my_set, end="\n\n")

# if we want index number then convert to other type like tuple/list
my_list = list(my_set)
print("my_list", my_list, end="\n\n")

print("#"*40, end="\n\n")
############################

print("set PART-2")
print("Methods present inside set class")
print("-"*20)
# ---------------

print(dir(set))
# OR
print(dir(my_set))

print("#"*40, end="\n\n")
############################

print("set PART-3")
print("union, intersection, difference methods")
print("-"*20)
# ---------------

java_course_candidates = set(["emp-1", "emp-2", "emp-3", "emp-4"])
python_course_candidates = set(["emp-3", "emp-4", "emp-5", "emp-6"])
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

print("set PART-4")
print("ADD/REMOVE/UPDATE Methods")
print("-"*20)
# ---------------

java_course_candidates = set(["emp-1", "emp-2", "emp-3", "emp-4"])
print("java_course_candidates: ", java_course_candidates, end="\n\n")

# Add
java_course_candidates.add("emp-5")
print("java_course_candidates after adding emp-5: ", java_course_candidates, end="\n\n")

# remove
java_course_candidates.remove("emp-2")
print("java_course_candidates after removing emp-2: ", java_course_candidates, end="\n\n")

# Update
python_course_candidates = set(["emp-3", "emp-4", "emp-5", "emp-6"])
java_course_candidates.update(python_course_candidates)
print("java_course_candidates after updating python_course_candidates: ", java_course_candidates, end="\n\n")

print("#"*40, end="\n\n")
############################