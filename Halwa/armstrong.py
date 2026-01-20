def checkArmstrong(number):
    digit=str(number)
    num=len(digit)
    sum=0
    for i in digit:
        sum += int(i)**num
        if number == sum:
            return True
        else:
            return False

print(checkArmstrong(153))