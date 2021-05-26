class TimeCheck:
    def validTime(self, time):
        try:
            if len(time) != 5 or ":" not in time:
                return False
            hours = time.split(":")[0]
            minutes = time.split(":")[1]
            if (len(hours) == 2 and len(minutes) == 2 and hours.isnumeric()
                    and minutes.isnumeric() and int(hours) <= 23 and int(minutes) <= 59):
                return True
            else:
                return False

        except ValueError:
            return False


if __name__ == "__main__":
    myObj = TimeCheck()
    print(myObj.validTime("02:42"))
