Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> lst=[4,0,0,1]
>>> lst*4
[4, 0, 0, 1, 4, 0, 0, 1, 4, 0, 0, 1, 4, 0, 0, 1]
>>> import numpy as np
>>> arr=np.array([1,2,3])
>>> arr
array([1, 2, 3])
>>> arr1=np.array([[1,2],[3,4]])
>>> arr1
array([[1, 2],
       [3, 4]])
>>> arr2=np.array(1,2,3,4)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    arr2=np.array(1,2,3,4)
ValueError: only 2 non-keyword arguments accepted
>>> print(arr,"\n\n",arr1)
[1 2 3] 

 [[1 2]
 [3 4]]
>>> arr*4
array([ 4,  8, 12])
>>> arr.shape()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    arr.shape()
TypeError: 'tuple' object is not callable
>>> arr.shape
(3,)
>>> arr.size
3
>>> arr.ndim
1
>>> arr1.shape
(2, 2)
>>> arr.size
3
>>> arr1.size
4
>>> arr.itemsize
8
>>> arr1.ndim
2
>>> arr1.itemsize
8
>>> lst=[[1,2,3,[1,2]],[0,9,8,7]]
>>> np.array(lst)
array([[1, 2, 3, list([1, 2])],
       [0, 9, 8, 7]], dtype=object)
>>> np.array(lst).size
8
>>> lst=[[1,2,3],[0,9,8,7]]
>>> np.array(lst)
array([list([1, 2, 3]), list([0, 9, 8, 7])], dtype=object)
>>> arr1=np.array([[2,3],[3,5],[4,6]])
>>> arr1.shape
(3, 2)
>>> arr1=np.array([[[2,3],[3,5],[4,6]],[1,2,3]])
>>> arr1.shape
(2, 3)
>>> arr1
array([[list([2, 3]), list([3, 5]), list([4, 6])],
       [1, 2, 3]], dtype=object)
>>> arr1=np.array([[2,3][2],[3,5][3],[4,6][4]])
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    arr1=np.array([[2,3][2],[3,5][3],[4,6][4]])
IndexError: list index out of range
>>> arr1=np.array([[2,3],[3,5],[4,6]])
>>> list(arr1)
[array([2, 3]), array([3, 5]), array([4, 6])]
>>> arr1=np.array([[[2,3],[3,5],[4,6]]])
>>> arr1
array([[[2, 3],
        [3, 5],
        [4, 6]]])
>>> arr1.shape
(1, 3, 2)
>>> arr1.ndim
3
>>> arr1.size
6
>>> list(arr1)
[array([[2, 3],
       [3, 5],
       [4, 6]])]
>>> "NUMPY"
'NUMPY'
>>> arr1=np.array([[[2,3],[3,5],[4,6]]])
>>> arr1=np.array([[[2,3],[3,5],[4,6]],])
KeyboardInterrupt
>>> arr1=np.array([[[2,3],[3,5],[4,6]],[[2,3],[3,5],[4,6]]])
>>> arr1
array([[[2, 3],
        [3, 5],
        [4, 6]],

       [[2, 3],
        [3, 5],
        [4, 6]]])
>>> arr1.shape
(2, 3, 2)
>>> # 3D array
>>> arr1=np.array([[2,3],[3,5],[4,6]])
>>> arr1.shape
(3, 2)
>>> for lst in arr1:
	x.append(lst)

	
Traceback (most recent call last):
  File "<pyshell#49>", line 2, in <module>
    x.append(lst)
NameError: name 'x' is not defined
>>> x=[]
>>> for lst in arr1:
	x.append(lst)

	
>>> x
[array([2, 3]), array([3, 5]), array([4, 6])]
>>> for lst in arr1:
	list(x.append(lst))

	
Traceback (most recent call last):
  File "<pyshell#55>", line 2, in <module>
    list(x.append(lst))
TypeError: 'NoneType' object is not iterable
>>> # matrix
>>> #MATRIX
>>> np.ones(5)
array([1., 1., 1., 1., 1.])
>>> np.ones(5,5)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    np.ones(5,5)
  File "/home/anuranjan/.local/lib/python3.6/site-packages/numpy/core/numeric.py", line 223, in ones
    a = empty(shape, dtype, order)
TypeError: data type not understood
>>> np.ones([5,5])
array([[1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.]])
>>> np.zeros(5)
array([0., 0., 0., 0., 0.])
>>> np.zeros(5,5)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    np.zeros(5,5)
TypeError: data type not understood
>>> np.zeros([5,5])
array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])
>>> np.identity(5)
array([[1., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0.],
       [0., 0., 1., 0., 0.],
       [0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 1.]])
>>> np.identity(5,5)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    np.identity(5,5)
  File "/home/anuranjan/.local/lib/python3.6/site-packages/numpy/core/numeric.py", line 2348, in identity
    return eye(n, dtype=dtype)
  File "/home/anuranjan/.local/lib/python3.6/site-packages/numpy/lib/twodim_base.py", line 201, in eye
    m = zeros((N, M), dtype=dtype, order=order)
TypeError: data type not understood
>>> np.identity([5,5])
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    np.identity([5,5])
  File "/home/anuranjan/.local/lib/python3.6/site-packages/numpy/core/numeric.py", line 2348, in identity
    return eye(n, dtype=dtype)
  File "/home/anuranjan/.local/lib/python3.6/site-packages/numpy/lib/twodim_base.py", line 201, in eye
    m = zeros((N, M), dtype=dtype, order=order)
TypeError: 'list' object cannot be interpreted as an integer
>>> np.identity((5,5))
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    np.identity((5,5))
  File "/home/anuranjan/.local/lib/python3.6/site-packages/numpy/core/numeric.py", line 2348, in identity
    return eye(n, dtype=dtype)
  File "/home/anuranjan/.local/lib/python3.6/site-packages/numpy/lib/twodim_base.py", line 201, in eye
    m = zeros((N, M), dtype=dtype, order=order)
TypeError: 'tuple' object cannot be interpreted as an integer
>>> np.delete()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    np.delete()
TypeError: delete() missing 2 required positional arguments: 'arr' and 'obj'
>>> np.ones([5,6])
array([[1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1.]])
>>> np.ones([5,4])
array([[1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.]])
>>> np.ones([5,4,1])
array([[[1.],
        [1.],
        [1.],
        [1.]],

       [[1.],
        [1.],
        [1.],
        [1.]],

       [[1.],
        [1.],
        [1.],
        [1.]],

       [[1.],
        [1.],
        [1.],
        [1.]],

       [[1.],
        [1.],
        [1.],
        [1.]]])
>>> np.ones([5,4,5])
array([[[1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.]],

       [[1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.]],

       [[1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.]],

       [[1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.]],

       [[1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.]]])
>>> a=np.array( [ [1,2,3,4][5,6,7,8][9,01,11,12] ] )
SyntaxError: invalid token
>>> a=np.array( [ [1,2,3,4][5,6,7,8][9,10,11,12] ] )
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a=np.array( [ [1,2,3,4][5,6,7,8][9,10,11,12] ] )
TypeError: list indices must be integers or slices, not tuple
>>> a=np.array( [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ] )
>>> a
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
>>> a.shape
(3, 4)
>>> list(a)
[array([1, 2, 3, 4]), array([5, 6, 7, 8]), array([ 9, 10, 11, 12])]
>>> list(list(a))
[array([1, 2, 3, 4]), array([5, 6, 7, 8]), array([ 9, 10, 11, 12])]
>>> a[0]
array([1, 2, 3, 4])
>>> a[0][1]
2
>>> a=np.array( [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ] )
>>> a[0]
array([1, 2, 3, 4])
>>> list(a[0])
[1, 2, 3, 4]
>>> x=[]
>>> for i in range(o,a.ndim):
	x.append(list(a[0]))

	
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    for i in range(o,a.ndim):
NameError: name 'o' is not defined
>>> for i in range(0,a.ndim):
	x.append(list(a[0]))

	
>>> x
[[1, 2, 3, 4], [1, 2, 3, 4]]
>>> for i in range(0,a.shape):
	x.append(list(a[0]))

	
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    for i in range(0,a.shape):
TypeError: 'tuple' object cannot be interpreted as an integer
>>> for i in range(0,a.shape[0]):
	x.append(list(a[0]))

	
>>> x
[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
>>> a
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
>>> a.shape
(3, 4)
>>> a.shape[0]
3
>>> for i in range(0,a.shape[0]):
	x.append(list(a[i]))

	
>>> x=[]
>>> for i in range(0,a.shape[0]):
	x.append(list(a[i]))

	
>>> x
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
>>> a
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
>>> a=np.delete(a,2,axis=1)
>>> a
array([[ 1,  2,  4],
       [ 5,  6,  8],
       [ 9, 10, 12]])
>>> a=np.delete(a,2,axis=0)
>>> a
array([[1, 2, 4],
       [5, 6, 8]])
>>> np.arange(0,10)
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> a.reshape(3,2,2)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    a.reshape(3,2,2)
ValueError: cannot reshape array of size 6 into shape (3,2,2)
>>> a=np.array( [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ] )
>>> a.reshape(3,2,2)
array([[[ 1,  2],
        [ 3,  4]],

       [[ 5,  6],
        [ 7,  8]],

       [[ 9, 10],
        [11, 12]]])
>>> a=np.array( [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ] )
>>> a.reshape(3,2,3)
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    a.reshape(3,2,3)
ValueError: cannot reshape array of size 12 into shape (3,2,3)
>>> # 3*2*3=18 != 12(3*2*2)
>>> # 3*2*3=18 != 12(3*2*2)
>>>  '3*2*3=18 != 12(3*2*2)'
SyntaxError: unexpected indent
>>> '3*2*3=18 != 12(3*2*2)'
'3*2*3=18 != 12(3*2*2)'
>>> a[][0]
SyntaxError: invalid syntax
>>> a[0:3,0]
array([1, 5, 9])
>>> a[:3,0]
array([1, 5, 9])
>>> a[:,0]
array([1, 5, 9])
>>> a[:,3]
array([ 4,  8, 12])
>>> a[0][1:3]
array([2, 3])
>>> a[1:3]
array([[ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
>>> a.shape
(3, 4)
>>> import xlwt
>>> ws=xlwt.Workbook()
>>> s=ws.add_sheet("Sheet1")
>>> s.write(0,1,'hello')
>>> ws.save("/home/anuranjan/Summer\ Training/anu.xls")
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    ws.save("/home/anuranjan/Summer\ Training/anu.xls")
  File "/home/anuranjan/.local/lib/python3.6/site-packages/xlwt/Workbook.py", line 710, in save
    doc.save(filename_or_stream, self.get_biff_data())
  File "/home/anuranjan/.local/lib/python3.6/site-packages/xlwt/CompoundDoc.py", line 262, in save
    f = open(file_name_or_filelike_obj, 'w+b')
FileNotFoundError: [Errno 2] No such file or directory: '/home/anuranjan/Summer\\ Training/anu.xls'
>>> ws.save("anu.xls")
>>> ws.save("Summer Training/anu.xls")
>>> 
