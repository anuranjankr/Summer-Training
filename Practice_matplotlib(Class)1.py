Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> import matplotlib
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import matplotlib
ModuleNotFoundError: No module named 'matplotlib'
>>> import matplotlib
>>> import matplotlib.pyplot as plt
>>> # from matplotlib import pyplot as plt  (same statement)
>>> plt.plot([1,2,3],[4,5,6])
[<matplotlib.lines.Line2D object at 0x7f6cb4d83940>]
>>> plt.show()
>>> plt.plot([1,2,3],[4,5,6],'r')
[<matplotlib.lines.Line2D object at 0x7f6cb48fb240>]
>>> plt.show()
>>> plt.plot([1,2,3],[4,5,6],'r')
[<matplotlib.lines.Line2D object at 0x7f6cb48e98d0>]
>>> plt.xlabel("X-Axis")
Text(0.5, 0, 'X-Axis')
>>> plt.ylabel("Y-Axis")
Text(0, 0.5, 'Y-Axis')
>>> plt.title("My Plot")
Text(0.5, 1.0, 'My Plot')
>>> plt.plot([2,4,6],[9,7,3],'b')
[<matplotlib.lines.Line2D object at 0x7f6cb48d2208>]
>>> plt.show()
>>> plt.plot([1,2,3],[4,5,6],'r',label='Line1')
[<matplotlib.lines.Line2D object at 0x7f6cb4855588>]
>>> plt.plot([2,4,6],[9,7,3],'b',label='Line2')
[<matplotlib.lines.Line2D object at 0x7f6cb4880588>]
>>> plt.show()
>>> plt.plot([1,2,3],[4,5,6],'r',label='Line1')
[<matplotlib.lines.Line2D object at 0x7f6cb47b5da0>]
>>> plt.plot([2,4,6],[9,7,3],'b',label='Line2')
[<matplotlib.lines.Line2D object at 0x7f6cb486be80>]
>>> plt.xlabel("X-Axis")
Text(0.5, 0, 'X-Axis')
>>> plt.ylabel("Y-Axis")
Text(0, 0.5, 'Y-Axis')
>>> plt.title("My Plot")
Text(0.5, 1.0, 'My Plot')
>>> plt.legend()
<matplotlib.legend.Legend object at 0x7f6cb47c24e0>
>>> plt.show()
>>> plt.plot([1,2,3],[4,5,6],'r',label='Line1',linewidth=0.5)
[<matplotlib.lines.Line2D object at 0x7f6cb47392e8>]
>>> plt.show()
>>> from matplotlib import style
>>> plt.plot([1,2,3],[4,5,6],'r',label='Line1',linewidth=0.5)
[<matplotlib.lines.Line2D object at 0x7f6cb4724588>]
>>> plt.plot([2,4,6],[9,7,3],'b',label='Line2')
[<matplotlib.lines.Line2D object at 0x7f6cb4896a58>]
>>> style.use('ggplot')
>>> plt.grid(True,color='k')
>>> plt.show()
>>> 
== RESTART: /home/anuranjan/Summer Training/Practice_matplotlib(class)2.py ==
>>> plt.subplot(211)
<matplotlib.axes._subplots.AxesSubplot object at 0x7f00a0147f98>
>>> plt.show()
>>> plt.subplot(211)
<matplotlib.axes._subplots.AxesSubplot object at 0x7f00a00b3438>
>>> plt.subplot(212)
<matplotlib.axes._subplots.AxesSubplot object at 0x7f00a01210f0>
>>> plt.show()
>>> plt.subplot(211)
<matplotlib.axes._subplots.AxesSubplot object at 0x7f009bdc76a0>
>>> plt.plot([1,2,3],[4,5,6],'r',label='Line1',linewidth=1.5)
[<matplotlib.lines.Line2D object at 0x7f00a00502e8>]
>>> plt.subplot(211)

Warning (from warnings module):
  File "/home/anuranjan/Summer Training/Practice_matplotlib(class)2.py", line 1
    import matplotlib.pyplot as plt
MatplotlibDeprecationWarning: Adding an axes using the same arguments as a previous axes currently reuses the earlier instance.  In a future version, a new instance will always be created and returned.  Meanwhile, this warning can be suppressed, and the future behavior ensured, by passing a unique label to each axes instance.
<matplotlib.axes._subplots.AxesSubplot object at 0x7f009bdc76a0>
>>> plt.subplot(212)
<matplotlib.axes._subplots.AxesSubplot object at 0x7f00a0050470>
>>> plt.plot([2,4,6],[9,7,3],'b',label='Line2')
[<matplotlib.lines.Line2D object at 0x7f009bdb82e8>]
>>> plt.show()
>>> 
== RESTART: /home/anuranjan/Summer Training/Practice_matplotlib(class)2.py ==
>>> plt.pie([1,2,3],[4,5,6])
([<matplotlib.patches.Wedge object at 0x7f2d07b88ba8>, <matplotlib.patches.Wedge object at 0x7f2d079120b8>, <matplotlib.patches.Wedge object at 0x7f2d07912550>], [Text(4.416729519509265, 2.550000068920677, ''), Text(-3.0500003297381366, 5.28275477271066, ''), Text(6.647499734949005e-07, -7.0999999999999694, '')])
>>> plt.show()
>>> plt.hist([1,2,3],[4,5,6])
(array([0., 0.]), array([4, 5, 6]), <a list of 2 Patch objects>)
>>> plt.show()
>>> plt.bar([1,2,3],[4,5,6])
<BarContainer object of 3 artists>
>>> plt.show()
>>> plt.plot([1,2,3],[4,5,6],'r-',label='Line1',linewidth=1.5)
[<matplotlib.lines.Line2D object at 0x7f2d077cb1d0>]
>>> plt.show()
>>> plt.plot([1,2,3],[4,5,6],'r--',label='Line1',linewidth=1.5)
[<matplotlib.lines.Line2D object at 0x7f2d077c1128>]
>>> plt.show()
>>> print(plt.axis.__doc__)

        Convenience method to get or set some axis properties.

        Call signatures::

          xmin, xmax, ymin, ymax = axis()
          xmin, xmax, ymin, ymax = axis([xmin, xmax, ymin, ymax])
          xmin, xmax, ymin, ymax = axis(option)
          xmin, xmax, ymin, ymax = axis(**kwargs)

        Parameters
        ----------
        xmin, xmax, ymin, ymax : float, optional
            The axis limits to be set. Either none or all of the limits must
            be given.

        option : bool or str
            If a bool, turns axis lines and labels on or off. If a string,
            possible values are:

            ======== ==========================================================
            Value    Description
            ======== ==========================================================
            'on'     Turn on axis lines and labels. Same as ``True``.
            'off'    Turn off axis lines and labels. Same as ``False``.
            'equal'  Set equal scaling (i.e., make circles circular) by
                     changing axis limits.
            'scaled' Set equal scaling (i.e., make circles circular) by
                     changing dimensions of the plot box.
            'tight'  Set limits just large enough to show all data.
            'auto'   Automatic scaling (fill plot box with data).
            'normal' Same as 'auto'; deprecated.
            'image'  'scaled' with axis limits equal to data limits.
            'square' Square plot; similar to 'scaled', but initially forcing
                     ``xmax-xmin = ymax-ymin``.
            ======== ==========================================================

        emit : bool, optional, default *True*
            Whether observers are notified of the axis limit change.
            This option is passed on to `~.Axes.set_xlim` and
            `~.Axes.set_ylim`.

        Returns
        -------
        xmin, xmax, ymin, ymax : float
            The axis limits.

        See also
        --------
        matplotlib.axes.Axes.set_xlim
        matplotlib.axes.Axes.set_ylim
        
>>> plt.plot([1,2,3],[4,5,6],'r--',label='Line1',linewidth=1.5)
[<matplotlib.lines.Line2D object at 0x7f2d0772efd0>]
>>> plt.axis([-10,10,-10,10])
[-10, 10, -10, 10]
>>> plt.show()
>>> plt.plot([-8,-6,-2,1,2,3],[1,3,9,4,5,6],'r--',label='Line1',linewidth=1.5)
[<matplotlib.lines.Line2D object at 0x7f2d04680b70>]
>>> plt.axis([-10,10,-10,10])
[-10, 10, -10, 10]
>>> plt.show()
>>> plt.plot([-8,-6,-2,1,2,3],[1,3,-9,4,5,6],'r^',label='Line1',linewidth=1.5)
[<matplotlib.lines.Line2D object at 0x7f2d045f36a0>]
>>> plt.axis([-10,10,-10,10])
[-10, 10, -10, 10]
>>> plt.xlabel("X-Axis")
Text(0.5, 0, 'X-Axis')
>>> plt.ylabel("Y-Axis")
Text(0, 0.5, 'Y-Axis')
>>> plt.label("My Plot")
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    plt.label("My Plot")
AttributeError: module 'matplotlib.pyplot' has no attribute 'label'
>>> plt.title("My Plot")
Text(0.5, 1.0, 'My Plot')
>>> plt.show()
>>> 
== RESTART: /home/anuranjan/Summer Training/Practice_matplotlib(class)2.py ==
Traceback (most recent call last):
  File "/home/anuranjan/Summer Training/Practice_matplotlib(class)2.py", line 4, in <module>
    plt.sublplot(211)
AttributeError: module 'matplotlib.pyplot' has no attribute 'sublplot'
>>> 
== RESTART: /home/anuranjan/Summer Training/Practice_matplotlib(class)2.py ==
>>> 
== RESTART: /home/anuranjan/Summer Training/Practice_matplotlib(class)2.py ==

== RESTART: /home/anuranjan/Summer Training/Practice_matplotlib(class)2.py ==

== RESTART: /home/anuranjan/Summer Training/Practice_matplotlib(class)2.py ==
>>> 
