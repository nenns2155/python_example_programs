"""
Python program to find the largest element and its location.
"""

def largest_element(a,Flag):
    """ Return the largest element of a sequence a."""
    try:
        max = a[0]
        loc = 0
        for i in range(1,len(a)):
            if a[i] > max:
                max=a[i]
                loc = i
            
        if Flag == True:
            return max, loc
        return max
    except TypeError:
        print("Hey, that's a Type Error!")
        return -1
    except:
        print("Unexpected Error")
        return -2

if __name__ == "__main__":

    a = [1,2,5,2,1]
    b = [1,'a',2]
    print("Largest element is {:}".format(largest_element(b,False)))