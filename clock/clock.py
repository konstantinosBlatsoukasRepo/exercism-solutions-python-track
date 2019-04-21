class Clock(object):
    def __init__(self, hour, minute):
        minute_to_hour, minute = self.__calculate_minute(minute)
        hour = self.__calculate_hour(minute_to_hour, hour)

        self.hour = hour
        self.minute = minute

    def __calculate_minute(self, minute):
        extra_hour = 0
        while (minute < 0):
            minute += 60
            extra_hour += 1

        final_minute = minute % 60
        result = (-extra_hour, final_minute)

        if minute >= 60:
            minute_to_hour = minute - final_minute
            print(minute_to_hour)
            result = (minute_to_hour, final_minute)

        return result

    def __calculate_hour(self, minute_to_hour, hour):
        while (hour < 0):
            hour += 24

        return (hour + minute_to_hour) % 24

    def __repr__(self):
        hour = self.__hour_representation(self.hour)
        minute = self.__minute_representation(self.minute)
        return "{0}:{1}".format(hour, minute)

    def __hour_representation(self, hour):
        if hour >= 0 and hour < 10:
            return '0' + str(hour)
        elif hour >= 10 and hour < 24:
            return str(hour)

    def __minute_representation(self, minute):
        if minute >= 0 and minute < 10:
            return '0' + str(minute)
        elif minute > 9 and minute < 60:
            return str(minute)

    def __eq__(self, other):
        return self.minute == other.minute and self.hour == other.hour

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)


clock = Clock(1, 60)

print(clock.minute)
print(clock.hour)
