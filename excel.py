import xlrd
>>> wb=xlrd.open_workbook(C:\Users\kashy\OneDrive\Documents\anu.xlsx)
SyntaxError: invalid syntax
>>> wb=xlrd.open_workbook(C\Users\kashy\OneDrive\Documents\anu.xlsx)
SyntaxError: unexpected character after line continuation character
>>> wb=xlrd.open_workbook(C:\Users\kashy\OneDrive\Documents\anu.xlsx)
SyntaxError: invalid syntax
>>> wb=xlrd.open_workbook("C:\Users\kashy\OneDrive\Documents\anu.xlsx")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> wb=xlrd.open_workbook("C:\\Users\\kashy\\OneDrive\\Documents\\anu.xlsx")
>>> s=wb.sheet_by_index(0)
>>> print(s.nrows)
5
>>> print(s.row_values())
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(s.row_values())
TypeError: row_values() missing 1 required positional argument: 'rowx'
>>> print(s.row_values(2))
['suresh', 1232.0, 5300.0]
>>> print(s.row_values(2,0))
['suresh', 1232.0, 5300.0]
>>> print(s.cell_value(2,0))
suresh
>>> print(s.cell_value(2))
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(s.cell_value(2))
TypeError: cell_value() missing 1 required positional argument: 'colx'
>>> print(s.ncols)
3
>>> print(s.col_values(2))
[5000.0, 5500.0, 5300.0, 2800.0, 7640.0]
>>> for lst in s:
	print(s)

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    for lst in s:
TypeError: 'Sheet' object is not iterable
>>> for lst in s.rows:
	print(lst)

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    for lst in s.rows:
AttributeError: 'Sheet' object has no attribute 'rows'
>>> for i in range(0,s.nrows):
	print(s.row_values(i))

['anu', 2345.0, 5000.0]
['ram', 5432.0, 5500.0]
['suresh', 1232.0, 5300.0]
['ramesh', 2331.0, 2800.0]
['shyam', 2321.0, 7640.0]
>>> users=s.col_values(0)
>>> print(users)
['anu', 'ram', 'suresh', 'ramesh', 'shyam']
>>> import xlwt
>>> ws=xlwt.Workbook("C:\\Users\\kashy\\OneDrive\\Documents\\anu.xls")
>>> s=ws.add_sheet()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    s=ws.add_sheet()
TypeError: add_sheet() missing 1 required positional argument: 'sheetname'
>>> s=ws.add_sheet(1)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    s=ws.add_sheet(1)
  File "C:\Users\kashy\AppData\Local\Programs\Python\Python37-32\lib\site-packages\xlwt\Workbook.py", line 366, in add_sheet
    sheetname = sheetname.decode(self.encoding)
AttributeError: 'int' object has no attribute 'decode'
>>> s=ws.add_sheet('sheet1')
>>> s.write(0,1,'hello')
>>> ws.save()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    ws.save()
TypeError: save() missing 1 required positional argument: 'filename_or_stream'
>>> ws.save('anu.xls')
>>> ws=xlwt.Workbook("C:\\Users\\kashy\\OneDrive\\Documents\\anu.xls")
>>> s1=ws.add_sheet()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    s1=ws.add_sheet()
TypeError: add_sheet() missing 1 required positional argument: 'sheetname'
>>> s=ws.add_sheet('sheet1')
>>> s.write(0,1,'hello')
>>> ws.save()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    ws.save()
TypeError: save() missing 1 required positional argument: 'filename_or_stream'
>>> ws.save('anu.xls')
>>> ws.save("C:\\Users\\kashy\\OneDrive\\Documents\\anu.xls")
>>> 


kumaranuranjan652@gmail.com