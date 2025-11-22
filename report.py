
class Report:
    def display_log(self, log_list):
        print("\n--- Health Monitoring Log ---")
        for i, entry in enumerate(log_list, 1):
            print(f"Record {i}: HR={entry['Heart Rate']} bpm, Temp={entry['Temperature']} °C")
            if entry['Alerts']:
                for alert in entry['Alerts']:
                    print(f"  {alert}")
            else:
                print("  All parameters normal.")
        print("-----------------------------")
