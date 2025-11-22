from user_input import UserInput         # Imports the UserInput class
from health_check import HealthCheck     # Imports the HealthCheck class
from data_logger import DataLogger       # Imports the DataLogger class
from report import Report                # Imports the Report class


class Monitor:
    def __init__(self):
        self.user_input = UserInput()
        self.health_check = HealthCheck()
        self.data_logger = DataLogger()
        self.report = Report()

    def start_monitoring(self):
        print("Health Monitoring and Alert System")
        print("Enter 'q' at any time to quit.\n")

        while True:
            user_command = input("Press Enter to input health data or 'q' to quit: ").strip().lower()
            if user_command == 'q':
                break

            hr, temp = self.user_input.get_user_input()
            if hr is None or temp is None:
                continue

            alerts = self.health_check.check_parameters(hr, temp)
            if alerts:
                for alert in alerts:
                    print(alert)
            else:
                print("All parameters normal.")

            self.data_logger.log_data(hr, temp, alerts)
            print()  # Blank line for readability

        self.report.display_log(self.data_logger.get_logs())
        print("Monitoring session ended. Thank you!")

