class UserInput:
    def get_user_input(self):
        try:
            hr = int(input("Enter Heart Rate (bpm): "))
            temp = float(input("Enter Body Temperature (°C): "))
            return hr, temp
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return None, None