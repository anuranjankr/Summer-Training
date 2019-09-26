import xlrd
import xlwt
from xlutils.copy import copy
ws=xlwt.Workbook()

wb=xlrd.open_workbook(r'C:\Users\kashy\OneDrive\Desktop\techie\xlutil.xls')
d=wb.sheet_by_index(0)
wx=copy(wb)
t=wx.get_sheet(0)
t.write(1,2,9)
wx.save('xlutil.xls')
