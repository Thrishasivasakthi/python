def fact(x):
    fact=[]
    divisor=2
    while divisor<=x:
        if x%divisor==0:
            fact.append(divisor)
            x=x/divisor
        else:
            divisor+=1
    return max(fact)
    
print(fact(600851475143))
