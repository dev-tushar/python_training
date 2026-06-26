"""
git/github steps
https://git-scm.com/docs
https://github.com/
"""

# --------------
# Install git software
# --------------
# Download and install git software from below link
# https://git-scm.com/
#############################

# --------------
# Make python_folder as git repository
# --------------
#  Run below commands
#
# C:\>cd python_training
# C:\python_training>git init
#
# Now 'python_training' folder is git repository
#############################

# --------------
# Add files and folders to 'python_training' git repository
# --------------
#  Run below commands
#
# C:\python_training>git add concepts programs
#  C:\B1_python_training>git commit -m "Added concepts and programs folders to git repository"
#
# Now 'concepts' and 'programs' folders are part of 'python_training' git repository
#############################

# --------------
# Create account in github
# --------------
# https://github.com/
#############################

# --------------
# Create new repository in github
# --------------
# click on "New" in github and create "python_training" repository
#############################

# --------------
# Link local repository with github repository
# --------------
# C:\python_training>git remote add origin https://github.com/mahadevaprabhug/python_training_21.git
#
# IMPORTANT: you need to provide your git url here
#############################

# --------------
# Push to github
# --------------
# C:\python_training>git push -u origin master
#
#############################

# --------------
# Pull trainer code to trainer_code directory
# --------------
# Step-1: create directory "trainer_code"
#
# Step-2: make directory "trainer_code" directory as git repository
#   C:\B1_python_training>cd C:\Users\mahad\Downloads\trainer_code
#   C:\Users\mahad\Downloads\trainer_code>git init
#   NOW, trainer_code folder is git repository
#
# Step-3: link local trainer_code git repository with trainer git repository
#   C:\python_training>git remote add origin https://github.com/mahadevaprabhug/python_training_21.git
#
#   IMPORTANT: link to trainer git repository only, because we need to pull trainer code
#
# Step-4: pull trainer code
#   git pull origin master
#############################

# tup = ([10,20],)
# print(tup)
#
# X = "Python"
#
# if(X[-1] == X[(len(X) - 1)]) and X.startswith("py"): print("Condition True")
# else: print("f")

# X = 0
# S = "PYTHON"
# while X < len(S):
#       print(S[X])
#       while True:
#              X = X + 1
#              break


# class MyClass:
#     def init(self, name):
#         self.name = name
#         name = "abc"
#
#         obj = MyClass("xyz")
#         print(obj.name)


# class MyClass:
#     @staticmethod
#     def ﬁnd_avg_sal(s1, s2):
#         return (s1 + s2) / 2
#
# print(MyClass.ﬁnd_avg_sal(1000, 2000))


# X = 10
# Y = 0
# try:
#     result = X/Y
#     print(result)
# except:
#      print("In Except Block")
#      else:
#     print("In Else Block")
#     finally:
#     print("In Finally Block")


# def add(a, b):
#     return a + b
#
#
# def sub(a, b):
#     return a - b




# from mymodule import add
# from mymodule import sub
# import mymodule as add
# import mymodule as sub
#
# print(add.add(10, 20))
# print(sub.add(10, 20))


# x = 5
# def my_outer_func(): x = 10
#
# def my_inner_func(): nonlocal x
#
# x = 100
#
# print("inner
# x:", x) my_inner_func()
# print("outer
# x:", x)
#
# my_outer_func()
# print("global x:", x)

def A():            # Scope A
    x = 1

    def B():        # Scope B
        x = 2

        def C():    # Scope C
            nonlocal x
            x = 3

        C()
        print(x)    # ← which x?

    B()
    print(x)        # ← which x?

A()