import time

hour = int(time.strftime('%H'))
print('Now Timing :', hour)
name = input('Enter Your Name : ').title()

if 0 <= hour < 12:
    print('Good Morning', name)
elif 12 <= hour <= 16:
    print('Good Afternoon', name)
elif 17 <= hour <= 20: 
    print('Good Evening', name)
else:
    print("Good Night", name)
