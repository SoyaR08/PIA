class Reloj:

    def __init__(self, actual_hour, actual_minute, actual_second):
        self.actual_hour = actual_hour
        self.actual_minute = actual_minute
        self.actual_second = actual_second

        self.adjust_time(self.actual_hour, self.actual_minute, self.actual_second)

    def advance_time(self, position):

        match position:

            case 'm':
                self.adjust_time(self.actual_hour, self.actual_minute + 1, self.actual_second)
            case 's':
                self.adjust_time(self.actual_hour, self.actual_minute, self.actual_second + 1)

        return f"Han transcurrido 1 {'minutos' if position == 'm' else 'segundos'}."

    def adjust_time(self, hours, minutes, seconds):

        fixed_seconds = seconds % 60
        extra_minutes = seconds // 60
        fixed_minutes = (minutes % 60) + extra_minutes
        extra_hours = minutes // 60

        self.actual_hour = hours + extra_hours
        self.actual_minute = fixed_minutes
        self.actual_second = fixed_seconds

    def show_time(self):
        return f"La hora actual es {self.actual_hour:02}:{self.actual_minute:02}:{self.actual_second:02}"