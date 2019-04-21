class Clock(object):
    def __init__(self, hour, minute):
        extra_hours, minute = self.__calculate_minute(minute)
        hour = self.__calculate_hour(extra_hours, hour)

        self.hour = hour
        self.minute = minute

    def __calculate_minute(self, minute):
        result = (0, 0)

        if minute >= 0:
            final_minute = minute % 60
            extra_hours = self.__extra_hours(minute)
            result = (extra_hours, final_minute)
        else:
            hours_for_decrement, minute = self.__normalize_minute(minute)
            result = (hours_for_decrement, minute)
        return result

    def __calculate_hour(self, extra_hours, hour):
        hour += extra_hours
        hour = self.__normalize_hour(hour)
        return hour % 24

    def __normalize_minute(self, minute):
        hours_for_decrement = 0
        while (minute < 0):
            minute += 60
            hours_for_decrement -= 1
        return (hours_for_decrement, minute)

    def __normalize_hour(self, hour):
        while (hour < 0):
            hour += 24
        return hour

    def __extra_hours(self, minutes):
        extra_hours = 0
        while(minutes > 59):
            minutes -= 60
            extra_hours += 1
        return extra_hours

    def __repr__(self):
        hour_representation = self.__hour_representation(self.hour)
        minute_representation = self.__minute_representation(self.minute)
        return "{0}:{1}".format(hour_representation, minute_representation)

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
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
