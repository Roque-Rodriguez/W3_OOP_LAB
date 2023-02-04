from alarm_clock import AlarmClock
from venmo_clone import Person


rocky_alarm = AlarmClock()
print(rocky_alarm.current_time)
print(rocky_alarm.alarm_status)
print(rocky_alarm.alarm_time)

rocky_alarm.change_current_time("1 PM")
rocky_alarm.alarm_toggle(False)
rocky_alarm.change_alarm_time("6 PM")


player_one = Person("Rocky", 700)
player_two = Person("Adrian", 1000)

player_one.removing_money(800)
print(player_one.cash)
print(player_two.cash)
