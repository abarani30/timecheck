class TimeCheck:
    def validTime(self, time):
        # سويته بهاي الطريقة بدون كود زايد 
        try:
            # هنا ما تحتاج كل -variable- تخليه بسطر واحد
            hours, minutes = time.split(':')
        except:
            return False
        else:
            # هنا اي حالة ما تطابق الشرط ترجع False
            return (len(hours) == 2 and len(minutes) == 2 and int(hours) in range(1, 24) and int(minutes) in range(1, 60))
     
if __name__ == "__main__":
    myObj = TimeCheck()
    print(myObj.validTime("01:45"))
