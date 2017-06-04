# caughtSpeeding.py
# by _______

# Write function defintion: caughtSpeeding

# Make sure it returns a value

def caughtSpeeding(speed, speed_limit, isBirthday):
    print(speed,speed_limit,isBirthday)

    if isBirthday == True:
        speed = int(speed - 5)
    if speed <= 5 + int(speed_limit):
        print('You get no ticket')
        fine = 0
    elif speed > 100 + int(speed_limit):
        print('You ar fined $2000, perhaps with a cold side of jailtime')
        fine = 2000
    elif speed > 25 + int(speed_limit):
        print('You are fined $1,500')
        fine = 1500
    elif speed > 15 + int(speed_limit):
        print('You are fined $1000')
        fine = 1000
    elif speed > 5 + int(speed_limit):
        print('You are fined $500')
        fine = 500

    return(fine)
    
        
if __name__ == '__main__':
    
    # Call the function in here if you want to test it
    # Make sure it's indented
    pass # remove or comment out this line if you wish to test the function
