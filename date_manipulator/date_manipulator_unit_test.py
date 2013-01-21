import unittest

from date_manipulator import date_manipulator

class TestDateManipulator(unittest.TestCase):

    def setUp(self):
        self.date_manipulator_obj = date_manipulator('ndq')
    
    def test_is_businessday(self):        
        day = (2013, 01, 20)    # This is a Sunday.
        self.assertFalse(self.date_manipulator_obj.is_businessday(day))
        
        day = (2013, 01, 22)    # This is a Tuesday.
        self.assertTrue(self.date_manipulator_obj.is_businessday(day))
        
        day = (2013, 01, 21)    # This is a Martin Luther King's day.
        self.assertFalse(self.date_manipulator_obj.is_businessday(day))
        
    def test_is_holiday(self):
        day = (1970,3,27)   # This is Good Friday.
        self.assertTrue(self.date_manipulator_obj.is_holiday(day))
        
        day = (2013, 1, 20) # This is Weekend.
        self.assertTrue(self.date_manipulator_obj.is_holiday(day))
        
        day = (2013, 1, 17) # This is Weekday.
        self.assertFalse(self.date_manipulator_obj.is_holiday(day))
        
        day = (2013, 7, 4) # This is Independence Day.
        self.assertTrue(self.date_manipulator_obj.is_holiday(day))
        
        day = (2013, 1, 21) # This is Martin Luther King Day.
        self.assertTrue(self.date_manipulator_obj.is_holiday(day))

    def test_is_holiday_per_market(self):
        # Testing Veterans Day
        day = (2013, 11, 11)
                
        self.date_manipulator_obj = date_manipulator('ndq')
        self.assertFalse(self.date_manipulator_obj.is_holiday(day))

        self.date_manipulator_obj = date_manipulator('cme')
        self.assertTrue(self.date_manipulator_obj.is_holiday(day))

        # Testing unexpected holiday
        day = (2012, 10, 30)
        
        self.date_manipulator_obj = date_manipulator('ndq')
        self.assertTrue(self.date_manipulator_obj.is_holiday(day))

        self.date_manipulator_obj = date_manipulator('cme')
        self.assertFalse(self.date_manipulator_obj.is_holiday(day))
        
    def test_add_bday(self):
        day = (2013, 1, 20)
        expected = (2013, 1, 28)
        result = self.date_manipulator_obj.add_bday(day, 5)
        self.assertEqual(expected, result)
        
    def test_add_cday(self):
        date = (2013, 1, 20)   # Set date : (2013, 1, 20)
        expected = (2013, 1, 25)
        result = self.date_manipulator_obj.add_cday(date, 5)
        self.assertEqual(expected, result) # Move 3 days from date.
        
        expected = (2013, 2, 9)
        result = self.date_manipulator_obj.add_cday(date, 20)
        self.assertEqual(expected, result)
         
    def test_nth_wkday(self):
        # Test 5th Tuesday
        date = (2013, 1, 20)    # Set date : (2013, 1, 20)
        expected = (2013, 1, 29) # 5th Tuesday
        result = self.date_manipulator_obj.nth_wkday(date, 5, 2)
        self.assertEqual(expected, result) 
        
        # Test 3rd Friday
        expected = (2013, 1, 18) # 3rd Friday
        result = self.date_manipulator_obj.nth_wkday(date, 3, 5)
        self.assertEqual(expected, result) 
        
        # Test 6th Thursday
        expected = (2013, 2, 7) # 6th Thursday from (2013,1,1)
        result = self.date_manipulator_obj.nth_wkday(date, 6, 4)
        self.assertEqual(expected, result)
        
    def test_add_month(self):
        # Simple month adding.
        date = (2013, 1, 20)    # Set date : (2013, 1, 20)
        expected = (2013, 2, 20)
        result = self.date_manipulator_obj.add_month(date, 1)
        self.assertEqual(expected, result)
        
        # More months than a year adding.
        expected = (2014, 2, 20)
        result = self.date_manipulator_obj.add_month(date, 13)
        self.assertEqual(expected, result)
        
        # Minus months change
        expected = (2012, 12, 20)
        result = self.date_manipulator_obj.add_month(date, -1)
        self.assertEqual(expected, result)
        
        # Minus months change more than a year.
        expected = (2011, 12, 20)
        result = self.date_manipulator_obj.add_month(date, -13)
        self.assertEqual(expected, result)
    
    def test_set_date(self):
        date = (2013, 1, 20)    # Set date : (2013, 1, 20)
        expected = (2013, 1, 4)
        result = self.date_manipulator_obj.set_date(date, 4)
        self.assertEqual(expected, result)
        
    def test_get_last_wkday(self):
        date = (2013, 1, 20)
        expected = (2013, 1, 30) # Last Wed of Jan
        result = self.date_manipulator_obj.get_last_wkday(date, 3)
        self.assertEqual(expected, result)
        
    def test_move_prev_nthwk(self):
        date = (2013, 1, 16)
        expected = (2013, 1, 16)
        result = self.date_manipulator_obj.move_prev_nthwk(date)
        self.assertEqual(expected, result)
        
        date = (2013, 1, 21)
        expected = (2013, 1, 14)
        result = self.date_manipulator_obj.move_prev_nthwk(date)
        self.assertEqual(expected, result)
    
    def test_period(self):
        
        pass
        
    def test_get_end_date(self):
        pass
    

if __name__ == '__main__':
    unittest.main()
