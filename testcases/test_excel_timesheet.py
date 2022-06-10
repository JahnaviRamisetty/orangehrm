import time
import pytest
from selenium.webdriver.common.by import By

from testcases.test_login import Test_login
from pageobjects.Admin.Login_timesheet import Time
from utilites import XLutilities

@pytest.mark.usefixtures("test_logintopage")
class Test_Time_excel(Test_login):
    path = ".\\testdata\\Timesheet.xlsx"
    # path1 = "C:\Jahnavi\Timesheet.xlsx"
    rows = XLutilities.getRowCount(path, 'timesheet')
    # lastrow = XLutilities.getLastrow(path)
    cols = XLutilities.getColumnCount(path,'timesheet')

    def test_excel_time(self):
        self.T =Time(self.driver)
        self.T.timesheet()
        sheet = ['Apache','Bug Fixes','6','6']
        self.T.table_data('Apache','Bug Fixes','6','6')
        self.T.table_data('h','Bug Fixes','6','8')
        self.driver.close()


        # # print("row count",self.rows)
        # # print("cols count",self.cols)
        # # for i in range (1, self.rows):
        # #     for c in range(1, self.cols+1):
        # #      val = XLutilities.readData(self.path, 'timesheet',i,c)
        # #      print(val, end="   ")
        # #     print()
        # for r in range(2, self.rows):
        #
        #     projectname = XLutilities.readData(self.path,'timesheet',r,1)
        #     # activityname = XLutilities.readData(self.path,'timesheet',r,2)
        #     # mon = XLutilities.readData(self.path,'timesheet',r,3)
        #     # tue = XLutilities.readData(self.path,'timesheet',r,4)
        #     # wed = XLutilities.readData(self.path,'timesheet',r,5)
        #     # thu = XLutilities.readData(self.path,'timesheet',r,6)
        #     # fri = XLutilities.readData(self.path,'timesheet',r,7)
        #     self.T.excel_table_data(projectname) #,mon,tue,wed,thu,fri
        #    # XLutilities.writeData(self.path, 'timesheet', r, 8, "row added successfully")
        #


