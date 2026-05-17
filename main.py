number=input("好きな数字を入れてください:" )
def fizz_buzz(number):
    n=int(number)
    if (n%3==0) and (n%5==0):
        kan=str("fizz_buzz")
    elif n%3==0:
        kan=str("Fizz")
    elif n%5==0:
        kan=str("Buzz")
    else:
        kan=str(n)
    return kan

answer=fizz_buzz(number)
print(answer)

        
