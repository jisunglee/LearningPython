import datetime
import calendar

class date_manipulator(object):

    def is_businessday(self, date):
        """Returns True/False if a day is a business day."""
        year, month, day = date
        datetime_obj = datetime.date(year, month, day)
        if self.is_holiday(date):
            return False
        else:
            return True
            
    def is_holiday(self, date):
        """Returns true if given date is a holiday."""
        year, month, day = date
        datetime_obj = datetime.date(year, month, day)
        
        Good_Friday_list = [
            (1970,3,27),(1971,4,9),(1972,3,31),(1973,4,20),(1974,4,12),
            (1975,3,28),(1976,4,16),(1977,4,8),(1978,3,24),(1979,4,13),
            (1980,4,4),(1981,4,17),(1982,4,9),(1983,4,1),(1984,4,20),
            (1985,4,5),(1986,3,28),(1987,4,17),(1988,4,1),(1989,3,24),
            (1990,4,13),(1991,3,29),(1992,4,17),(1993,4,9),(1994,4,1),
            (1995,4,14),(1996,4,5),(1997,3,28),(1998,4,10),(1999,4,2),
            (2000,4,21),(2001,4,13),(2002,3,29),(2003,4,18),(2004,4,9),
            (2005,3,25),(2006,4,14),(2007,4,6),(2008,3,21),(2009,4,10),
            (2010,4,2),(2011,4,22),(2012,4,6),(2013,3,29),(2014,4,18),
            (2015,4,3),(2016,3,25),(2017,4,14),(2018,3,30),(2019,4,19),
            (2020,4,10),(2021,4,2),(2022,4,15),(2023,4,7),(2024,3,29),
            (2025,4,18),(2026,4,3),(2027,3,26),(2028,4,14),(2029,3,30),
            (2030,4,19),(2031,4,11),(2032,3,26),(2033,4,15),(2034,4,7)
            ]
            
        fixed_date_holiday = [
            (1, 1),     # New Years Day
            (7, 4),     # Independence Day
            (12, 24),   # Christmas Eve
            (12, 25),   # Christmas
            ]
            
        relative_date_holiday = [
            self.nth_wkday((year, 1, 1), 3, 1), # Martin Luther King Day
            self.nth_wkday((year, 2, 1), 3, 1),   # Washingtons Birthday
            self.get_last_wkday((year, 5, 1), 1), # Memorial Day
            self.nth_wkday((year, 9, 1), 1, 1), # Labor Day
            self.nth_wkday((year, 11, 1), 4, 4), # Thanksgiving Day
            self.nth_wkday((year, 11, 1), 4, 5), # Black Friday
            ]

        if datetime_obj.weekday() > 4:
            return True
        elif date in Good_Friday_list:
            return True
        elif date in relative_date_holiday:
            return True
        elif (month, day) in fixed_date_holiday:
            return True
        else:
            return False
            
    def add_bday(self):
        pass
    
    def add_cday(self, date, days_to_move):
        year, month, day = date
        datetime_obj = datetime.date(year, month, day)
        
        datetime_obj += datetime.timedelta(days = days_to_move)
        
        return (datetime_obj.year, datetime_obj.month, datetime_obj.day)

    def nth_wkday(self, date, nth_week, weekday):
        """For given date, find the nth_week, weekday."""
        year, month, day = date
        datetime_obj = datetime.date(year, month, day)
        
        weekday = (weekday - 1) % 7 # Converts to python format (monday = 0).
        date = datetime_obj.replace(day = 1)    # Move to the first day of the month.
        adj = (weekday - date.weekday()) % 7
        date += datetime.timedelta(days = adj)
        date += datetime.timedelta(weeks = nth_week-1)
        return (date.year, date.month, date.day)
        
    def add_month(self, date, month_chg):
        """Add month to date.
        
        Args:
            date: (year, month, day) tuple
            month_chg: <int> of months to change. It can take negative
                values.
        """
        year, month, day = date
        
        year_chg = month_chg/12
        month_chg = month_chg%12
            
        return (year+year_chg, month+month_chg, day)
        
    def set_date(self, date, set_day):
        """Set day to the same month as date."""
        year, month, day = date
        return (year, month, set_day)
        
    def get_last_wkday(self, date, wkday):
        """Get the last weekday of the given month where date falls in."""
        year, month, day = date
        _, last_day = calendar.monthrange(year, month)
        datetime_obj = datetime.date(year, month, last_day)
        
        while datetime_obj.weekday() != wkday-1:
            datetime_obj += datetime.timedelta(days = -1)
            
        return (datetime_obj.year, datetime_obj.month, datetime_obj.day)
        
    def move_prev_nthwk(self, date):
        """For given date, subtrace one week if the week with
        the date has less than 5 working days. If the week with the date
        has 5 working days, return the date.
        """
        year, month, day = date
        datetime_obj = datetime.date(year, month, day)
        
        # Setting counter to Monday.
        datetime_it = (
            datetime_obj - datetime.timedelta(days=datetime_obj.weekday()))

        # Iterate through the week to count whether all five days are working days.
        working_days = 0
        for i in range(6):
            datetime_it += datetime.timedelta(days=i)
            date_tuple = (
                datetime_it.year, datetime_it.month, datetime_it.day)
            if not self.is_holiday(date_tuple):
                working_days += 1
                
        if working_days < 5:
            datetime_obj -= datetime.timedelta(weeks=1)
            
        return (datetime_obj.year, datetime_obj.month, datetime_obj.day)
        
    def period(self):
        pass
        
    def get_end_date(self):
        pass
