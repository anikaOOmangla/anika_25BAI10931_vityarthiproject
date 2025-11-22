class HealthCheck:
    def __init__(self, hr_min=60, hr_max=100, temp_min=36.1, temp_max=37.2):
        self.hr_min = hr_min
        self.hr_max = hr_max
        self.temp_min = temp_min
        self.temp_max = temp_max

    def check_parameters(self, hr, temp):
        alerts = []
        if hr < self.hr_min:
            alerts.append(f"Alert: Heart rate too low! ({hr} bpm)")
        elif hr > self.hr_max:
            alerts.append(f"Alert: Heart rate too high! ({hr} bpm)")

        if temp < self.temp_min:
            alerts.append(f"Alert: Body temperature too low! ({temp} °C)")
        elif temp > self.temp_max:
            alerts.append(f"Alert: Body temperature too high! ({temp} °C)")
        return alerts
