"""
Write a class called AlarmClock in the main.py file.

Give this class three instance variables declared inside of an __init__ method.
A string that represents the current time
A boolean that represents whether the alarm is on or off
A string that represents the time the alarm is set to.

Write three additional methods for the class.
Method #1: Will change the current time (by giving the current time instance variable a new value) and print that new value to the console.
This method should have an additional parameter that allows a value to be passed in for the new time as a string when the method is called.
Method #2: Will toggle the alarm clock on or off by changing the boolean instance variable between true or false.
Method #3: Will set or change the current alarm time by assigning a new value to the alarm time instance variable and printing the new time to the console.
This method should have an additional parameter that allows a value to be passed in for the new time as a string when the method is called.
"""
class AlarmClock:

    def __init__(self):
        self.current_time = "12 pm"
        self.alarm_status = True
        self.alarm_time = "2 pm"

    def change_current_time(self, time):
        self.current_time = time 
        print(self.current_time)

    def alarm_toggle(self, boolean):
        self.alarm_status = boolean
        print(self.alarm_status)

    def change_alarm_time(self, alarm_time):
        self.alarm_time = alarm_time
        print(self.alarm_time)


# rocky_alarm = AlarmClock()
# print(rocky_alarm.current_time)
# print(rocky_alarm.alarm_status)
# print(rocky_alarm.alarm_time)

# rocky_alarm.change_current_time("1 PM")
# rocky_alarm.alarm_toggle(False)
# rocky_alarm.change_alarm_time("6 PM")