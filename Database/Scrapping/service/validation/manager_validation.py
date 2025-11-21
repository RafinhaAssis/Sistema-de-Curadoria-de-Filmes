class ManagerValidation():
    
    def __get_month(self, month: str)-> str:
        month = month.lower()
        
        if month == 'jan':
            return "01"
        elif month == 'fev':
            return "02"
        elif month == 'mar':
            return "03"
        elif month == 'abr':
            return "04"
        elif month == 'mai':
            return "05"
        elif month == 'jun':
            return "06"
        elif month == 'jul':
            return "07"
        elif month == 'ago':
            return "08"
        elif month == 'set':
            return "09"
        elif month == 'out':
            return "10"
        elif month == 'nov':
            return "11"
        elif month == 'dev':
            return "12"
        else:
            return "01"
        
    
    def convert_date(self, date: str) -> str:
        date_split: list = date.split(" ")
        if len(date_split) == 5:
            day: str = date_split[0]
            month: str = self.__get_month(date_split[2])
            year: str = date_split[4]
            return f"{day}/{month}/{year}"
            
        return "01/01/0001"
    
    def convert_hour(self, time: str) -> str:
        time_split: list = time.split(" ")
        if len(time_split) ==2:
            hour: str = time_split[0].replace("h", "")
            if len(hour) < 2:
                hour = f"0{hour}"
            
            minute: str = time_split[1].replace("m", "")
            if len(minute) < 2:
                minute = f"0{minute}"
        
            return f"{hour}:{minute}"
        
        return time
            
        