class DataLogger:
    def __init__(self):
        self.log_list = []

    def log_data(self, hr, temp, alerts):
        entry = {"Heart Rate": hr, "Temperature": temp, "Alerts": alerts}
        self.log_list.append(entry)

    def get_logs(self):
        return self.log_list
