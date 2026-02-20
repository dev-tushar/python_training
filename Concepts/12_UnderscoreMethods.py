
# ---------------
# about __ methods
# ---------------
# Example-1
# >>> a = "Hi"
# >>> b = "Hello"
# >>> c = a + b # Concat
# >>> c
# 'HiHello'
# >>> d = a.__add__(b)
# >>> d
# 'HiHello'
# >>>
# CONCLUSION: Internally + calls __add__ method
#
#
# >>> # Example-2
# >>> b = "Hello"
# >>> b[0]
# 'H'
# >>> b.__getitem__(0)
# 'H'
# >>>
# CONCLUSION: Internally [] calls __getitem__ method
############################