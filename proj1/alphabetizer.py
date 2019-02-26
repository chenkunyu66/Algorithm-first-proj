#project 01
#cse 331
#chen，kunyu
#A54470631

def order_first_name(a, b):
    """
    Orders two people by their first names
    :param a: a Person
    :param b: a Person
    :return: True if a comes before b alphabetically and False otherwise
    """
    #check a, b are alphabetically or not 
    if a.first < b.first:  
        return True
    elif a.first == b.first: # if a,b have same first neame
        if a.last < b.last:  # check last name 
            return True
    else:
        return False


def order_last_name(a, b):
    """
    Orders two people by their last names
    :param a: a Person
    :param b: a Person
    :return: True if a comes before b alphabetically and False otherwise
    """
    # check a,b last name are alphabetically or not 
    if a.last < b.last:    
        return True
    elif a.last == b.last: # if last name are same
        if a.first < b.first:  # check first name 
            return True
    else:
        return False


def is_alphabetized(roster, ordering):
    """
    Checks whether the roster of names is alphabetized in the given order
    :param roster: a list of people
    :param ordering: a function comparing two elements
    :return: True if the roster is alphabetized and False otherwise
    """
    # those peopel are list alphabetically or not
    for i in range(len(roster) - 1): 
        if not ordering(roster[i], roster[i + 1]):
            return False

    return True


def alphabetize(roster, ordering):
    """
    Alphabetizes the roster according to the given ordering
    :param roster: a list of people
    :param ordering: a function comparing two elements
    :return: a sorted version of roster
    :return: the number of comparisons made
    """
    return mergeSort(roster, ordering)

# using mergeSort 
def mergeSort(roster, ordering):
    count = 0
    # roster have more than 1 people 
    if len(roster) > 1:
        mid = len(roster) // 2
        left_half = roster[:mid]
        right_half = roster[mid:]
        left_half, count1 = mergeSort(left_half, ordering)
        right_half, count2 = mergeSort(right_half, ordering)
        # left half count + right half count
        count = count1 + count2

        i = 0
        j = 0
        k = 0
        roster = []
        # while loop 
        while (i < len(left_half) and j < len(right_half)):
            # if the order is alphabetically append left side name
            if ordering(left_half[i], right_half[j]):
                roster.append(left_half[i])
                i = i + 1
                # count the time of comparisons
                count = count +1
            #if not append right side name 
            else:
                roster.append(right_half[j])
                j = j + 1
                k = k + 1
                
        while i < len(left_half):
            roster.append(left_half[i])
            i = i + 1
            k = k + 1
            count = count+1
        while j < len(right_half):
            roster.append(right_half[j])
            j = j + 1
            k = k + 1
            count = count +1
    return (roster, count)
