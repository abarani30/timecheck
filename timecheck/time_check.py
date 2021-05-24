class TimeCheck:
    def validTime(self, time):
        if len(time) != 5 or ":" not in time:
            return False
        hours = time.split(":")[0]
        minutes = time.split(":")[1]
        if len(hours) != 2 or len(minutes) != 2:
            return False
        else:
            if int(hours) <= 23 and int(minutes) <= 59:
                return True
        return False


if __name__ == "__main__":
    myObj = TimeCheck()
    print(myObj.validTime("01:45"))
