Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> import cv2
>>> a.cv2.imread('flower1.jpg')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a.cv2.imread('flower1.jpg')
NameError: name 'a' is not defined
>>> a=cv2.imread('flower1.jpg')
>>> type(a)
<class 'NoneType'>
>>> a.shape
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a.shape
AttributeError: 'NoneType' object has no attribute 'shape'
>>> # the above command didn't worked because there was no such image in the folder (show attention)
>>> 
>>> a.cv2.imread('flower1.jpg')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.cv2.imread('flower1.jpg')
AttributeError: 'NoneType' object has no attribute 'cv2'
>>> a=cv2.imread('flower1.jpg')
>>> type(a)
<class 'NoneType'>
>>> a=cv2.imread('flower1.jpeg')
>>> type(a)
<class 'numpy.ndarray'>
>>> #Worked
>>> a.shape
(194, 259, 3)
>>> a
array([[[41, 52, 26],
        [41, 52, 26],
        [41, 52, 26],
        ...,
        [41, 52, 26],
        [41, 52, 26],
        [41, 52, 26]],

       [[41, 52, 26],
        [41, 52, 26],
        [41, 52, 26],
        ...,
        [41, 52, 26],
        [41, 52, 26],
        [41, 52, 26]],

       [[41, 52, 26],
        [41, 52, 26],
        [41, 52, 26],
        ...,
        [41, 52, 26],
        [41, 52, 26],
        [41, 52, 26]],

       ...,

       [[41, 52, 26],
        [41, 52, 26],
        [41, 52, 26],
        ...,
        [41, 52, 26],
        [41, 52, 26],
        [41, 52, 26]],

       [[41, 52, 26],
        [41, 52, 26],
        [41, 52, 26],
        ...,
        [41, 52, 26],
        [41, 52, 26],
        [41, 52, 26]],

       [[41, 52, 26],
        [41, 52, 26],
        [41, 52, 26],
        ...,
        [41, 52, 26],
        [41, 52, 26],
        [41, 52, 26]]], dtype=uint8)
>>> a.size
150738
>>> 194*259*3
150738
>>> a.ndim
3
>>> import numpy
>>> import numpy as np
>>> arr=np.array([ [[2,2],[2,2]] ])
>>> arr
array([[[2, 2],
        [2, 2]]])
>>> arr.shape
(1, 2, 2)
>>> arr=np.array([ [[2,2,3],[2,2,4]] ])
>>> arr.shape
(1, 2, 3)
>>> a.shape
(194, 259, 3)
>>> a
array([[[41, 52, 26],
        [41, 52, 26],
        [41, 52, 26],
        ...,
        [41, 52, 26],
        [41, 52, 26],
        [41, 52, 26]],

       [[41, 52, 26],
        [41, 52, 26],
        [41, 52, 26],
        ...,
        [41, 52, 26],
        [41, 52, 26],
        [41, 52, 26]],

       [[41, 52, 26],
        [41, 52, 26],
        [41, 52, 26],
        ...,
        [41, 52, 26],
        [41, 52, 26],
        [41, 52, 26]],

       ...,

       [[41, 52, 26],
        [41, 52, 26],
        [41, 52, 26],
        ...,
        [41, 52, 26],
        [41, 52, 26],
        [41, 52, 26]],

       [[41, 52, 26],
        [41, 52, 26],
        [41, 52, 26],
        ...,
        [41, 52, 26],
        [41, 52, 26],
        [41, 52, 26]],

       [[41, 52, 26],
        [41, 52, 26],
        [41, 52, 26],
        ...,
        [41, 52, 26],
        [41, 52, 26],
        [41, 52, 26]]], dtype=uint8)
>>> arr
array([[[2, 2, 3],
        [2, 2, 4]]])
>>> cv2.imshow('My Image',a)
>>> 
=============================== RESTART: Shell ===============================
>>> 
