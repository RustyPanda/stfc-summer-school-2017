# Fizz Bizz

def FizzBuzz(values=range(1,101),multiples=[3,5],phrases=['Fizz','Buzz']):

    N=len(values)
    # Create a list of empty strings
    print_vals=['']*N

    for v in range(N):

        emptStr=''
        for m in range(len(multiples)):

            if values[v]%multiples[m]==0:
                emptStr=emptStr+phrases[m]

        if emptStr!='':
            print_vals[v]=emptStr
        else:
            print_vals[v]=str(values[v])

        print values[v],'\t',print_vals[v]

    return print_vals

out=FizzBuzz()

out=FizzBuzz(values=range(-50,50))

out=FizzBuzz(
    values=range(1,101,1),
    multiples=[3,5,7],
    phrases=['I','Love','Python']
    )