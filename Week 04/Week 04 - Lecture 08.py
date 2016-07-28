
""" Following are scripts for Finger exercises & problems in Week 04 - Lecture 08. """





# ----- Problem 03 -----
# ----------------------

def FancyDivide(list_of_numbers, index):
    try:
        denom = list_of_numbers[index]
        return [SimpleDivide(item, denom) for item in list_of_numbers]
    except ZeroDivisionError:
        return [0 for item in list_of_numbers]
    except:
        raise Exception
    
def SimpleDivide(item, denom):
   return item / denom

print FancyDivide([0, 2, 4], 0)
