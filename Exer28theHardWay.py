# Boolean Practice

True and True       # true

False and True      # false

1 == 1 and 2 == 1   # false

'test' == "test"    # true

1 == 1 or 2 != 1    # true

True and 1 == 1   # true

False and 0 != 0  # false

True or 1 == 1  #  true

"test" == "testing"  # false

1 != 0 and 2 == 1   # false

"test" != "testing"  # true

"test" == 1  # false

not (True and False)  #true

not (1 == 1 and 0 != 1)  # false
    # not (1 == 1 and 0 != 1)
    # False

not (10 == 1 or 1000 == 1000) # False
    # not (10 == 1 or 1000 == 1000)
    # False

not (1 != 10 or 3 == 4) # false
    # not (1 != 10 or 3 == 4)
    # False

not ("testing" == "testing" and "Zed" == "Cool Guy")  #true
    # not ("testing" == "testing" and "Zed" == "Cool Guy")
    # True

1 == 1 and not ("testing" == 1 or 1 == 0)  # true
    # 1 == 1 and not ("testing" == 1 or 1 == 0)
    # True

"chunky" == "bacon" and not (3 == 4 or 3 == 3) # false
    # "chunky" == "bacon" and not (3 == 4 or 3 == 3)
    # False

3 == 3 and not ("testing" == "testing" or "Python" == "fun") # false
    # 3 == 3 and not ("testing" == "testing" or "Python" == "fun")
    # False

# note:
# Whenever you see these boolean logic statements, you can solve them easily by this simple process:
# 1. Find an equality test (== or !=) and replace it with its truth.
# 2. Find each and/or inside parenthesis and solve those first
# 3. Find each not and invert it
# 4. Find any remaining and/or and solve it
# 5. When you are done, you should have True or False

# e.g: 3 != 4 and not ("testing" != "test" or "Python" == "Python")

# Here's an example to solve this
# a. 3 != 4 is TRUE:    TRUE and not ("testing" != "test" or "Python" == "Python")
# b. "testing" != "test" is TRUE:    True and not (True or "Python" == "Python")
# c. "Python" == "Python":      True and not (True or True)

# Find each and/or in parenthesis():
# (True or True) is True:        True and not (True)

# Find each not and invert it:
# not (True)is False:     True and False

# Find any remaining and/or and solve them:
# True and False is False

# With that, we're done and know the result is FALSE


# SHORTCUT TECHNIQUE
# Any expression that has a FALSE is immediately FALSE, so you can stop there. Any or expression
# that has a TRUE is immediately TRUE, so you can stop there. But make sure that you can process the whole expression, because later it becomes helpful.



