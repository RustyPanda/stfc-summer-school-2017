
# Need to print out numbers 1 to 100
# all multiples of 3 and 5 are replaced by 'Fizz' and 'Buzz' resp
# Multiples of both 3 and 5 need to be 'FizzBuzz'

def FizzBuzzSkeleton():

    values=range(1,101) # Creates a list from 1 to 100

    FizzBuzzList=['Fizz','Buzz'] # A list can contain strings
    print FizzBuzzList[0] # prints the first element of the list

    for i in values: # Loops over every element in values

        print i%3 # Returns the remainder

    return #Ends the function, any variables after return are output

FizzBuzzSkeleton() # Executes the function