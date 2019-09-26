Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas
>>> print('\n\t\tSERIES\n')

		SERIES

>>> import pandas as pd
>>> s=[1,2,3,4]
>>> s1[[1,2],[3,4]]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s1[[1,2],[3,4]]
NameError: name 's1' is not defined
>>> s1=[[1,2],[3,4]]
>>> a=pd.series(s)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a=pd.series(s)
AttributeError: module 'pandas' has no attribute 'series'
>>> a=pd.Series(s)
>>> b=pd.Series(s1)
>>> print(a)
0    1
1    2
2    3
3    4
dtype: int64
>>> print(b)
0    [1, 2]
1    [3, 4]
dtype: object
>>> np.array(b)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    np.array(b)
NameError: name 'np' is not defined
>>> import numpy as np
>>> np.array(b)
array([list([1, 2]), list([3, 4])], dtype=object)
>>> print(pd.Series.__doc__)

    One-dimensional ndarray with axis labels (including time series).

    Labels need not be unique but must be a hashable type. The object
    supports both integer- and label-based indexing and provides a host of
    methods for performing operations involving the index. Statistical
    methods from ndarray have been overridden to automatically exclude
    missing data (currently represented as NaN).

    Operations between Series (+, -, /, *, **) align values based on their
    associated index values-- they need not be the same length. The result
    index will be the sorted union of the two indexes.

    Parameters
    ----------
    data : array-like, Iterable, dict, or scalar value
        Contains data stored in Series.

        .. versionchanged :: 0.23.0
           If data is a dict, argument order is maintained for Python 3.6
           and later.

    index : array-like or Index (1d)
        Values must be hashable and have the same length as `data`.
        Non-unique index values are allowed. Will default to
        RangeIndex (0, 1, 2, ..., n) if not provided. If both a dict and index
        sequence are used, the index will override the keys found in the
        dict.
    dtype : str, numpy.dtype, or ExtensionDtype, optional
        dtype for the output Series. If not specified, this will be
        inferred from `data`.
        See the :ref:`user guide <basics.dtypes>` for more usages.
    copy : bool, default False
        Copy input data.
    
>>> np.array(s1)
array([[1, 2],
       [3, 4]])
>>> dir(pd)
['Categorical', 'CategoricalDtype', 'CategoricalIndex', 'DataFrame', 'DateOffset', 'DatetimeIndex', 'DatetimeTZDtype', 'ExcelFile', 'ExcelWriter', 'Float64Index', 'Grouper', 'HDFStore', 'Index', 'IndexSlice', 'Int16Dtype', 'Int32Dtype', 'Int64Dtype', 'Int64Index', 'Int8Dtype', 'Interval', 'IntervalDtype', 'IntervalIndex', 'MultiIndex', 'NaT', 'Panel', 'Period', 'PeriodDtype', 'PeriodIndex', 'RangeIndex', 'Series', 'SparseArray', 'SparseDataFrame', 'SparseDtype', 'SparseSeries', 'TimeGrouper', 'Timedelta', 'TimedeltaIndex', 'Timestamp', 'UInt16Dtype', 'UInt32Dtype', 'UInt64Dtype', 'UInt64Index', 'UInt8Dtype', '__builtins__', '__cached__', '__doc__', '__docformat__', '__file__', '__git_version__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_hashtable', '_lib', '_libs', '_np_version_under1p13', '_np_version_under1p14', '_np_version_under1p15', '_np_version_under1p16', '_np_version_under1p17', '_tslib', '_version', 'api', 'array', 'arrays', 'bdate_range', 'compat', 'concat', 'core', 'crosstab', 'cut', 'date_range', 'datetime', 'describe_option', 'errors', 'eval', 'factorize', 'get_dummies', 'get_option', 'infer_freq', 'interval_range', 'io', 'isna', 'isnull', 'lreshape', 'melt', 'merge', 'merge_asof', 'merge_ordered', 'notna', 'notnull', 'np', 'offsets', 'option_context', 'options', 'pandas', 'period_range', 'pivot', 'pivot_table', 'plotting', 'qcut', 'read_clipboard', 'read_csv', 'read_excel', 'read_feather', 'read_fwf', 'read_gbq', 'read_hdf', 'read_html', 'read_json', 'read_msgpack', 'read_parquet', 'read_pickle', 'read_sas', 'read_sql', 'read_sql_query', 'read_sql_table', 'read_stata', 'read_table', 'reset_option', 'set_eng_float_format', 'set_option', 'show_versions', 'test', 'testing', 'timedelta_range', 'to_datetime', 'to_msgpack', 'to_numeric', 'to_pickle', 'to_timedelta', 'tseries', 'unique', 'util', 'value_counts', 'wide_to_long']
>>> %timeit 2+2
SyntaxError: invalid syntax
>>> 
>>> a.index=['a','b','c','d']
>>> print(a)
a    1
b    2
c    3
d    4
dtype: int64
>>> c=pd.Series(s,index=['a','b','c','d'])
>>> print(c)
a    1
b    2
c    3
d    4
dtype: int64
>>> s2={'a':1,'b':2,'c':3}
>>> pd.Series(s2)
a    1
b    2
c    3
dtype: int64
>>> d=pd.Series(s2)
>>> d
a    1
b    2
c    3
dtype: int64
>>> e=pd.Series([3,4,5,6])
>>> e
0    3
1    4
2    5
3    6
dtype: int64
>>> e=pd.Series([3,4,5])
>>> e.add(6)
0     9
1    10
2    11
dtype: int64
>>> e.sub(6)
0   -3
1   -2
2   -1
dtype: int64
>>> e.mul(2)
0     6
1     8
2    10
dtype: int64
>>> e.div(5)
0    0.6
1    0.8
2    1.0
dtype: float64
>>> e.add(d)
0   NaN
1   NaN
2   NaN
a   NaN
b   NaN
c   NaN
dtype: float64
>>> e.add(a)
0   NaN
1   NaN
2   NaN
a   NaN
b   NaN
c   NaN
d   NaN
dtype: float64
>>> f=pd.Series([3,4,5,6])
>>> e.add(f)
0     6.0
1     8.0
2    10.0
3     NaN
dtype: float64
>>> print('\n\t\t DATAFRAMES\n')

		 DATAFRAMES

>>> s=[ [1,2],[5,3,4] ]
>>> s1[1,2,3,4]
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    s1[1,2,3,4]
TypeError: list indices must be integers or slices, not tuple
>>> s1=[1,2,3,4]
>>> s2=[ [[1,2],[3,4]],[[1,3],[5,6]] ]
>>> np.array(s)
array([list([1, 2]), list([5, 3, 4])], dtype=object)
>>> np.array(s1)
array([1, 2, 3, 4])
>>> np.array(s2)
array([[[1, 2],
        [3, 4]],

       [[1, 3],
        [5, 6]]])
>>> pd.DataFrame(s)
   0  1    2
0  1  2  NaN
1  5  3  4.0
>>> pd.DataFrame(s1)
   0
0  1
1  2
2  3
3  4
>>> pd.DataFrame(s2)
        0       1
0  [1, 2]  [3, 4]
1  [1, 3]  [5, 6]
>>> print(pd.DataFrame.__doc__)

    Two-dimensional size-mutable, potentially heterogeneous tabular data
    structure with labeled axes (rows and columns). Arithmetic operations
    align on both row and column labels. Can be thought of as a dict-like
    container for Series objects. The primary pandas data structure.

    Parameters
    ----------
    data : ndarray (structured or homogeneous), Iterable, dict, or DataFrame
        Dict can contain Series, arrays, constants, or list-like objects

        .. versionchanged :: 0.23.0
           If data is a dict, argument order is maintained for Python 3.6
           and later.

    index : Index or array-like
        Index to use for resulting frame. Will default to RangeIndex if
        no indexing information part of input data and no index provided
    columns : Index or array-like
        Column labels to use for resulting frame. Will default to
        RangeIndex (0, 1, 2, ..., n) if no column labels are provided
    dtype : dtype, default None
        Data type to force. Only a single dtype is allowed. If None, infer
    copy : boolean, default False
        Copy data from inputs. Only affects DataFrame / 2d ndarray input

    See Also
    --------
    DataFrame.from_records : Constructor from tuples, also record arrays.
    DataFrame.from_dict : From dicts of Series, arrays, or dicts.
    DataFrame.from_items : From sequence of (key, value) pairs
        pandas.read_csv, pandas.read_table, pandas.read_clipboard.

    Examples
    --------
    Constructing DataFrame from a dictionary.

    >>> d = {'col1': [1, 2], 'col2': [3, 4]}
    >>> df = pd.DataFrame(data=d)
    >>> df
       col1  col2
    0     1     3
    1     2     4

    Notice that the inferred dtype is int64.

    >>> df.dtypes
    col1    int64
    col2    int64
    dtype: object

    To enforce a single dtype:

    >>> df = pd.DataFrame(data=d, dtype=np.int8)
    >>> df.dtypes
    col1    int8
    col2    int8
    dtype: object

    Constructing DataFrame from numpy ndarray:

    >>> df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
    ...                    columns=['a', 'b', 'c'])
    >>> df2
       a  b  c
    0  1  2  3
    1  4  5  6
    2  7  8  9
    
>>> df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),columns=['a', 'b', 'c'],index=['1','2','3'])
>>> df2
   a  b  c
1  1  2  3
2  4  5  6
3  7  8  9
>>> d = {'col1': [1, 2], 'col2': [3, 4]}
>>> d
{'col1': [1, 2], 'col2': [3, 4]}
>>> pd.DtaFrame(d)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    pd.DtaFrame(d)
AttributeError: module 'pandas' has no attribute 'DtaFrame'
>>> pd.DataFrame(d)
   col1  col2
0     1     3
1     2     4
>>> 
>>> print('\t\tSORT\n')
		SORT

>>> print(pd.sort_by.__doc__)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    print(pd.sort_by.__doc__)
AttributeError: module 'pandas' has no attribute 'sort_by'
>>> print(pd.Sort_by.__doc__)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    print(pd.Sort_by.__doc__)
AttributeError: module 'pandas' has no attribute 'Sort_by'
>>> df={'a':[4,2,55,4],'b':['a','b','c']}
>>> pd.DataFrame(df)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    pd.DataFrame(df)
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/frame.py", line 392, in __init__
    mgr = init_dict(data, index, columns, dtype=dtype)
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/internals/construction.py", line 212, in init_dict
    return arrays_to_mgr(arrays, data_names, index, columns, dtype=dtype)
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/internals/construction.py", line 51, in arrays_to_mgr
    index = extract_index(arrays)
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/internals/construction.py", line 317, in extract_index
    raise ValueError('arrays must all be same length')
ValueError: arrays must all be same length
>>> df={'a':[4,2,55,4],'b':['a','b','c','d']}
>>> df=pd.DataFrame(df)
>>> df
    a  b
0   4  a
1   2  b
2  55  c
3   4  d
>>> pd.DataFrame.sort_by('9')
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    pd.DataFrame.sort_by('9')
AttributeError: type object 'DataFrame' has no attribute 'sort_by'
>>> pd.DataFrame.Sort_by('9')
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    pd.DataFrame.Sort_by('9')
AttributeError: type object 'DataFrame' has no attribute 'Sort_by'
>>> df.sort_values()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    df.sort_values()
TypeError: sort_values() missing 1 required positional argument: 'by'
>>> df.sort_values(by=[''])
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    df.sort_values(by=[''])
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/frame.py", line 4719, in sort_values
    k = self._get_label_or_level_values(by, axis=axis)
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/generic.py", line 1706, in _get_label_or_level_values
    raise KeyError(key)
KeyError: ''
>>> df.sort_by('a')
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    df.sort_by('a')
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/generic.py", line 5067, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'sort_by'
>>> df.sort_by('a')[1:3]
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    df.sort_by('a')[1:3]
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/generic.py", line 5067, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'sort_by'
>>> df.sort_values(by=['a'])
    a  b
1   2  b
0   4  a
3   4  d
2  55  c
>>> df.sort_index()
    a  b
0   4  a
1   2  b
2  55  c
3   4  d
>>> print(pd.DataFrame.sort_index.__doc__)

Sort object by labels (along an axis)

Parameters
----------
axis : index, columns to direct sorting
level : int or level name or list of ints or list of level names
    if not None, sort on values in specified index level(s)
ascending : boolean, default True
    Sort ascending vs. descending
inplace : bool, default False
    if True, perform operation in-place
kind : {'quicksort', 'mergesort', 'heapsort'}, default 'quicksort'
     Choice of sorting algorithm. See also ndarray.np.sort for more
     information.  `mergesort` is the only stable algorithm. For
     DataFrames, this option is only applied when sorting on a single
     column or label.
na_position : {'first', 'last'}, default 'last'
     `first` puts NaNs at the beginning, `last` puts NaNs at the end.
     Not implemented for MultiIndex.
sort_remaining : bool, default True
    if true and sorting by level and index is multilevel, sort by other
    levels too (in order) after sorting by specified level

Returns
-------
sorted_obj : DataFrame

>>> print(pd.DataFrame.sort_values.__doc__)

Sort by the values along either axis

Parameters
----------
        by : str or list of str
            Name or list of names to sort by.

            - if `axis` is 0 or `'index'` then `by` may contain index
              levels and/or column labels
            - if `axis` is 1 or `'columns'` then `by` may contain column
              levels and/or index labels

            .. versionchanged:: 0.23.0
               Allow specifying index or column level names.
axis : {0 or 'index', 1 or 'columns'}, default 0
     Axis to be sorted
ascending : bool or list of bool, default True
     Sort ascending vs. descending. Specify list for multiple sort
     orders.  If this is a list of bools, must match the length of
     the by.
inplace : bool, default False
     if True, perform operation in-place
kind : {'quicksort', 'mergesort', 'heapsort'}, default 'quicksort'
     Choice of sorting algorithm. See also ndarray.np.sort for more
     information.  `mergesort` is the only stable algorithm. For
     DataFrames, this option is only applied when sorting on a single
     column or label.
na_position : {'first', 'last'}, default 'last'
     `first` puts NaNs at the beginning, `last` puts NaNs at the end

Returns
-------
sorted_obj : DataFrame

Examples
--------
>>> df = pd.DataFrame({
...     'col1' : ['A', 'A', 'B', np.nan, 'D', 'C'],
...     'col2' : [2, 1, 9, 8, 7, 4],
...     'col3': [0, 1, 9, 4, 2, 3],
... })
>>> df
    col1 col2 col3
0   A    2    0
1   A    1    1
2   B    9    9
3   NaN  8    4
4   D    7    2
5   C    4    3

Sort by col1

>>> df.sort_values(by=['col1'])
    col1 col2 col3
0   A    2    0
1   A    1    1
2   B    9    9
5   C    4    3
4   D    7    2
3   NaN  8    4

Sort by multiple columns

>>> df.sort_values(by=['col1', 'col2'])
    col1 col2 col3
1   A    1    1
0   A    2    0
2   B    9    9
5   C    4    3
4   D    7    2
3   NaN  8    4

Sort Descending

>>> df.sort_values(by='col1', ascending=False)
    col1 col2 col3
4   D    7    2
5   C    4    3
2   B    9    9
0   A    2    0
1   A    1    1
3   NaN  8    4

Putting NAs first

>>> df.sort_values(by='col1', ascending=False, na_position='first')
    col1 col2 col3
3   NaN  8    4
4   D    7    2
5   C    4    3
2   B    9    9
0   A    2    0
1   A    1    1

>>> df.mean()
a    16.25
dtype: float64
>>> df
    a  b
0   4  a
1   2  b
2  55  c
3   4  d
>>> df = pd.DataFrame({
...     'col1' : ['A', 'A', 'B', np.nan, 'D', 'C'],
...     'col2' : [2, 1, 9, 8, 7, 4],
...     'col3': [0, 1, 9, 4, 2, 3],
... })
SyntaxError: invalid syntax
>>> df = pd.DataFrame({'col1' : ['A', 'A', 'B', np.nan, 'D', 'C'],'col2' : [2, 1, 9, 8, 7, 4],'col3': [0, 1, 9, 4, 2, 3],})
>>> df.mean()
col2    5.166667
col3    3.166667
dtype: float64
>>> df[0]['col1']
Traceback (most recent call last):
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/indexes/base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas/_libs/index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 0

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    df[0]['col1']
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/indexes/base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/_libs/index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 0
>>> df[0,'col1']
Traceback (most recent call last):
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/indexes/base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas/_libs/index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: (0, 'col1')

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    df[0,'col1']
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/indexes/base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/_libs/index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: (0, 'col1')
>>> df(0,'col1')
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    df(0,'col1')
TypeError: 'DataFrame' object is not callable
>>> df.max()
col2    9
col3    9
dtype: int64
>>> mn=df.mean()
>>> mn
col2    5.166667
col3    3.166667
dtype: float64
>>> mn.mean()
4.166666666666667
>>> mean(df.mean())
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    mean(df.mean())
NameError: name 'mean' is not defined
>>> val=df(0,'col')
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    val=df(0,'col')
TypeError: 'DataFrame' object is not callable
>>> dir(pd.DataFrame)
['T', '_AXIS_ALIASES', '_AXIS_IALIASES', '_AXIS_LEN', '_AXIS_NAMES', '_AXIS_NUMBERS', '_AXIS_ORDERS', '_AXIS_REVERSED', '_AXIS_SLICEMAP', '__abs__', '__add__', '__and__', '__array__', '__array_priority__', '__array_wrap__', '__bool__', '__bytes__', '__class__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__div__', '__doc__', '__eq__', '__finalize__', '__floordiv__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__iand__', '__ifloordiv__', '__imod__', '__imul__', '__init__', '__init_subclass__', '__invert__', '__ior__', '__ipow__', '__isub__', '__iter__', '__itruediv__', '__ixor__', '__le__', '__len__', '__lt__', '__matmul__', '__mod__', '__module__', '__mul__', '__ne__', '__neg__', '__new__', '__nonzero__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmatmul__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__setitem__', '__setstate__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__unicode__', '__weakref__', '__xor__', '_accessors', '_add_numeric_operations', '_add_series_only_operations', '_add_series_or_dataframe_operations', '_agg_by_level', '_agg_examples_doc', '_agg_summary_and_see_also_doc', '_aggregate', '_aggregate_multiple_funcs', '_align_frame', '_align_series', '_box_col_values', '_box_item_values', '_builtin_table', '_check_inplace_setting', '_check_is_chained_assignment_possible', '_check_label_or_level_ambiguity', '_check_percentile', '_check_setitem_copy', '_clear_item_cache', '_clip_with_one_bound', '_clip_with_scalar', '_combine_const', '_combine_frame', '_combine_match_columns', '_combine_match_index', '_consolidate', '_consolidate_inplace', '_construct_axes_dict', '_construct_axes_dict_for_slice', '_construct_axes_dict_from', '_construct_axes_from_arguments', '_constructor', '_constructor_expanddim', '_constructor_sliced', '_convert', '_count_level', '_create_indexer', '_cython_table', '_deprecations', '_dir_additions', '_dir_deletions', '_drop_axis', '_drop_labels_or_levels', '_ensure_valid_index', '_expand_axes', '_find_valid_index', '_from_arrays', '_from_axes', '_get_agg_axis', '_get_axis', '_get_axis_name', '_get_axis_number', '_get_axis_resolvers', '_get_block_manager_axis', '_get_bool_data', '_get_cacher', '_get_index_resolvers', '_get_item_cache', '_get_label_or_level_values', '_get_numeric_data', '_get_value', '_get_values', '_getitem_bool_array', '_getitem_frame', '_getitem_multilevel', '_gotitem', '_iget_item_cache', '_indexed_same', '_info_axis', '_info_axis_name', '_info_axis_number', '_info_repr', '_init_mgr', '_internal_names', '_internal_names_set', '_is_builtin_func', '_is_cached', '_is_copy', '_is_cython_func', '_is_datelike_mixed_type', '_is_homogeneous_type', '_is_label_or_level_reference', '_is_label_reference', '_is_level_reference', '_is_mixed_type', '_is_numeric_mixed_type', '_is_view', '_ix', '_ixs', '_join_compat', '_maybe_cache_changed', '_maybe_update_cacher', '_metadata', '_needs_reindex_multi', '_obj_with_exclusions', '_protect_consolidate', '_reduce', '_reindex_axes', '_reindex_columns', '_reindex_index', '_reindex_multi', '_reindex_with_indexers', '_repr_data_resource_', '_repr_fits_horizontal_', '_repr_fits_vertical_', '_repr_html_', '_repr_latex_', '_reset_cache', '_reset_cacher', '_sanitize_column', '_selected_obj', '_selection', '_selection_list', '_selection_name', '_series', '_set_as_cached', '_set_axis', '_set_axis_name', '_set_is_copy', '_set_item', '_set_value', '_setitem_array', '_setitem_frame', '_setitem_slice', '_setup_axes', '_shallow_copy', '_slice', '_stat_axis', '_stat_axis_name', '_stat_axis_number', '_take', '_to_dict_of_blocks', '_try_aggregate_string_function', '_typ', '_unpickle_frame_compat', '_unpickle_matrix_compat', '_update_inplace', '_validate_dtype', '_values', '_where', '_xs', 'abs', 'add', 'add_prefix', 'add_suffix', 'agg', 'aggregate', 'align', 'all', 'any', 'append', 'apply', 'applymap', 'as_blocks', 'as_matrix', 'asfreq', 'asof', 'assign', 'astype', 'at', 'at_time', 'axes', 'between_time', 'bfill', 'blocks', 'bool', 'boxplot', 'clip', 'clip_lower', 'clip_upper', 'columns', 'combine', 'combine_first', 'compound', 'convert_objects', 'copy', 'corr', 'corrwith', 'count', 'cov', 'cummax', 'cummin', 'cumprod', 'cumsum', 'describe', 'diff', 'div', 'divide', 'dot', 'drop', 'drop_duplicates', 'droplevel', 'dropna', 'dtypes', 'duplicated', 'empty', 'eq', 'equals', 'eval', 'ewm', 'expanding', 'ffill', 'fillna', 'filter', 'first', 'first_valid_index', 'floordiv', 'from_csv', 'from_dict', 'from_items', 'from_records', 'ftypes', 'ge', 'get', 'get_dtype_counts', 'get_ftype_counts', 'get_value', 'get_values', 'groupby', 'gt', 'head', 'hist', 'iat', 'idxmax', 'idxmin', 'iloc', 'index', 'infer_objects', 'info', 'insert', 'interpolate', 'is_copy', 'isin', 'isna', 'isnull', 'items', 'iteritems', 'iterrows', 'itertuples', 'ix', 'join', 'keys', 'kurt', 'kurtosis', 'last', 'last_valid_index', 'le', 'loc', 'lookup', 'lt', 'mad', 'mask', 'max', 'mean', 'median', 'melt', 'memory_usage', 'merge', 'min', 'mod', 'mode', 'mul', 'multiply', 'ndim', 'ne', 'nlargest', 'notna', 'notnull', 'nsmallest', 'nunique', 'pct_change', 'pipe', 'pivot', 'pivot_table', 'plot', 'pop', 'pow', 'prod', 'product', 'quantile', 'query', 'radd', 'rank', 'rdiv', 'reindex', 'reindex_axis', 'reindex_like', 'rename', 'rename_axis', 'reorder_levels', 'replace', 'resample', 'reset_index', 'rfloordiv', 'rmod', 'rmul', 'rolling', 'round', 'rpow', 'rsub', 'rtruediv', 'sample', 'select', 'select_dtypes', 'sem', 'set_axis', 'set_index', 'set_value', 'shape', 'shift', 'size', 'skew', 'slice_shift', 'sort_index', 'sort_values', 'squeeze', 'stack', 'std', 'style', 'sub', 'subtract', 'sum', 'swapaxes', 'swaplevel', 'tail', 'take', 'timetuple', 'to_clipboard', 'to_csv', 'to_dense', 'to_dict', 'to_excel', 'to_feather', 'to_gbq', 'to_hdf', 'to_html', 'to_json', 'to_latex', 'to_msgpack', 'to_numpy', 'to_panel', 'to_parquet', 'to_period', 'to_pickle', 'to_records', 'to_sparse', 'to_sql', 'to_stata', 'to_string', 'to_timestamp', 'to_xarray', 'transform', 'transpose', 'truediv', 'truncate', 'tshift', 'tz_convert', 'tz_localize', 'unstack', 'update', 'values', 'var', 'where', 'xs']
>>> df.g
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    df.g
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/generic.py", line 5067, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'g'
>>> val=df[0,'col']
Traceback (most recent call last):
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/indexes/base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas/_libs/index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: (0, 'col')

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    val=df[0,'col']
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/indexes/base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/_libs/index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: (0, 'col')
>>> val=df[0,0]
Traceback (most recent call last):
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/indexes/base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas/_libs/index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: (0, 0)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    val=df[0,0]
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/indexes/base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/_libs/index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: (0, 0)
>>> df = pd.DataFrame({'col1' : ['A', 'A', 'B', np.nan, 'D', 'C'],'col2' : [2, 1, 9, 8, 7, 4],'col3': [0, 1, 9, 4, 2, 3],})
>>> df[0,1]
Traceback (most recent call last):
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/indexes/base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas/_libs/index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: (0, 1)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    df[0,1]
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/indexes/base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/_libs/index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: (0, 1)
>>> df['col1']'
SyntaxError: EOL while scanning string literal
>>> df['col1']
0      A
1      A
2      B
3    NaN
4      D
5      C
Name: col1, dtype: object
>>> df['col1'][1]
'A'
>>> df[1]
Traceback (most recent call last):
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/indexes/base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas/_libs/index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 1

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    df[1]
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/indexes/base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/_libs/index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 1
>>> df[1]['col1']
Traceback (most recent call last):
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/indexes/base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas/_libs/index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 1

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    df[1]['col1']
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/indexes/base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/_libs/index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 1
>>> df['col1'][1]
'A'
>>> df.get_values('col1',0)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    df.get_values('col1',0)
TypeError: get_values() takes 1 positional argument but 3 were given
>>> df.get_values()
array([['A', 2, 0],
       ['A', 1, 1],
       ['B', 9, 9],
       [nan, 8, 4],
       ['D', 7, 2],
       ['C', 4, 3]], dtype=object)
>>> df.get_values()[0][0]
'A'
>>> df.sort_values(by='col1')
  col1  col2  col3
0    A     2     0
1    A     1     1
2    B     9     9
5    C     4     3
4    D     7     2
3  NaN     8     4
>>> df.sort_values(by='col1',ascending=False)
  col1  col2  col3
4    D     7     2
5    C     4     3
2    B     9     9
0    A     2     0
1    A     1     1
3  NaN     8     4
>>> df.sort_values(by='col1',ascending=False,na_position='first')
  col1  col2  col3
3  NaN     8     4
4    D     7     2
5    C     4     3
2    B     9     9
0    A     2     0
1    A     1     1
>>> df.max()
col2    9
col3    9
dtype: int64
>>> print('\t DataSets in csv\n1.headbrain.csv\n2.stock_market_data.csv\n3.forestfires.csv')
	 DataSets in csv
1.headbrain.csv
2.stock_market_data.csv
3.forestfires.csv
>>> print('\n\t\t CSV Files\n')

		 CSV Files

>>> a=pd.read_csv("Iris.csv")
>>> b=np.array(a)
>>> b
array([[1, 5.1, 3.5, 1.4, 0.2, 'Iris-setosa'],
       [2, 4.9, 3.0, 1.4, 0.2, 'Iris-setosa'],
       [3, 4.7, 3.2, 1.3, 0.2, 'Iris-setosa'],
       [4, 4.6, 3.1, 1.5, 0.2, 'Iris-setosa'],
       [5, 5.0, 3.6, 1.4, 0.2, 'Iris-setosa'],
       [6, 5.4, 3.9, 1.7, 0.4, 'Iris-setosa'],
       [7, 4.6, 3.4, 1.4, 0.3, 'Iris-setosa'],
       [8, 5.0, 3.4, 1.5, 0.2, 'Iris-setosa'],
       [9, 4.4, 2.9, 1.4, 0.2, 'Iris-setosa'],
       [10, 4.9, 3.1, 1.5, 0.1, 'Iris-setosa'],
       [11, 5.4, 3.7, 1.5, 0.2, 'Iris-setosa'],
       [12, 4.8, 3.4, 1.6, 0.2, 'Iris-setosa'],
       [13, 4.8, 3.0, 1.4, 0.1, 'Iris-setosa'],
       [14, 4.3, 3.0, 1.1, 0.1, 'Iris-setosa'],
       [15, 5.8, 4.0, 1.2, 0.2, 'Iris-setosa'],
       [16, 5.7, 4.4, 1.5, 0.4, 'Iris-setosa'],
       [17, 5.4, 3.9, 1.3, 0.4, 'Iris-setosa'],
       [18, 5.1, 3.5, 1.4, 0.3, 'Iris-setosa'],
       [19, 5.7, 3.8, 1.7, 0.3, 'Iris-setosa'],
       [20, 5.1, 3.8, 1.5, 0.3, 'Iris-setosa'],
       [21, 5.4, 3.4, 1.7, 0.2, 'Iris-setosa'],
       [22, 5.1, 3.7, 1.5, 0.4, 'Iris-setosa'],
       [23, 4.6, 3.6, 1.0, 0.2, 'Iris-setosa'],
       [24, 5.1, 3.3, 1.7, 0.5, 'Iris-setosa'],
       [25, 4.8, 3.4, 1.9, 0.2, 'Iris-setosa'],
       [26, 5.0, 3.0, 1.6, 0.2, 'Iris-setosa'],
       [27, 5.0, 3.4, 1.6, 0.4, 'Iris-setosa'],
       [28, 5.2, 3.5, 1.5, 0.2, 'Iris-setosa'],
       [29, 5.2, 3.4, 1.4, 0.2, 'Iris-setosa'],
       [30, 4.7, 3.2, 1.6, 0.2, 'Iris-setosa'],
       [31, 4.8, 3.1, 1.6, 0.2, 'Iris-setosa'],
       [32, 5.4, 3.4, 1.5, 0.4, 'Iris-setosa'],
       [33, 5.2, 4.1, 1.5, 0.1, 'Iris-setosa'],
       [34, 5.5, 4.2, 1.4, 0.2, 'Iris-setosa'],
       [35, 4.9, 3.1, 1.5, 0.1, 'Iris-setosa'],
       [36, 5.0, 3.2, 1.2, 0.2, 'Iris-setosa'],
       [37, 5.5, 3.5, 1.3, 0.2, 'Iris-setosa'],
       [38, 4.9, 3.1, 1.5, 0.1, 'Iris-setosa'],
       [39, 4.4, 3.0, 1.3, 0.2, 'Iris-setosa'],
       [40, 5.1, 3.4, 1.5, 0.2, 'Iris-setosa'],
       [41, 5.0, 3.5, 1.3, 0.3, 'Iris-setosa'],
       [42, 4.5, 2.3, 1.3, 0.3, 'Iris-setosa'],
       [43, 4.4, 3.2, 1.3, 0.2, 'Iris-setosa'],
       [44, 5.0, 3.5, 1.6, 0.6, 'Iris-setosa'],
       [45, 5.1, 3.8, 1.9, 0.4, 'Iris-setosa'],
       [46, 4.8, 3.0, 1.4, 0.3, 'Iris-setosa'],
       [47, 5.1, 3.8, 1.6, 0.2, 'Iris-setosa'],
       [48, 4.6, 3.2, 1.4, 0.2, 'Iris-setosa'],
       [49, 5.3, 3.7, 1.5, 0.2, 'Iris-setosa'],
       [50, 5.0, 3.3, 1.4, 0.2, 'Iris-setosa'],
       [51, 7.0, 3.2, 4.7, 1.4, 'Iris-versicolor'],
       [52, 6.4, 3.2, 4.5, 1.5, 'Iris-versicolor'],
       [53, 6.9, 3.1, 4.9, 1.5, 'Iris-versicolor'],
       [54, 5.5, 2.3, 4.0, 1.3, 'Iris-versicolor'],
       [55, 6.5, 2.8, 4.6, 1.5, 'Iris-versicolor'],
       [56, 5.7, 2.8, 4.5, 1.3, 'Iris-versicolor'],
       [57, 6.3, 3.3, 4.7, 1.6, 'Iris-versicolor'],
       [58, 4.9, 2.4, 3.3, 1.0, 'Iris-versicolor'],
       [59, 6.6, 2.9, 4.6, 1.3, 'Iris-versicolor'],
       [60, 5.2, 2.7, 3.9, 1.4, 'Iris-versicolor'],
       [61, 5.0, 2.0, 3.5, 1.0, 'Iris-versicolor'],
       [62, 5.9, 3.0, 4.2, 1.5, 'Iris-versicolor'],
       [63, 6.0, 2.2, 4.0, 1.0, 'Iris-versicolor'],
       [64, 6.1, 2.9, 4.7, 1.4, 'Iris-versicolor'],
       [65, 5.6, 2.9, 3.6, 1.3, 'Iris-versicolor'],
       [66, 6.7, 3.1, 4.4, 1.4, 'Iris-versicolor'],
       [67, 5.6, 3.0, 4.5, 1.5, 'Iris-versicolor'],
       [68, 5.8, 2.7, 4.1, 1.0, 'Iris-versicolor'],
       [69, 6.2, 2.2, 4.5, 1.5, 'Iris-versicolor'],
       [70, 5.6, 2.5, 3.9, 1.1, 'Iris-versicolor'],
       [71, 5.9, 3.2, 4.8, 1.8, 'Iris-versicolor'],
       [72, 6.1, 2.8, 4.0, 1.3, 'Iris-versicolor'],
       [73, 6.3, 2.5, 4.9, 1.5, 'Iris-versicolor'],
       [74, 6.1, 2.8, 4.7, 1.2, 'Iris-versicolor'],
       [75, 6.4, 2.9, 4.3, 1.3, 'Iris-versicolor'],
       [76, 6.6, 3.0, 4.4, 1.4, 'Iris-versicolor'],
       [77, 6.8, 2.8, 4.8, 1.4, 'Iris-versicolor'],
       [78, 6.7, 3.0, 5.0, 1.7, 'Iris-versicolor'],
       [79, 6.0, 2.9, 4.5, 1.5, 'Iris-versicolor'],
       [80, 5.7, 2.6, 3.5, 1.0, 'Iris-versicolor'],
       [81, 5.5, 2.4, 3.8, 1.1, 'Iris-versicolor'],
       [82, 5.5, 2.4, 3.7, 1.0, 'Iris-versicolor'],
       [83, 5.8, 2.7, 3.9, 1.2, 'Iris-versicolor'],
       [84, 6.0, 2.7, 5.1, 1.6, 'Iris-versicolor'],
       [85, 5.4, 3.0, 4.5, 1.5, 'Iris-versicolor'],
       [86, 6.0, 3.4, 4.5, 1.6, 'Iris-versicolor'],
       [87, 6.7, 3.1, 4.7, 1.5, 'Iris-versicolor'],
       [88, 6.3, 2.3, 4.4, 1.3, 'Iris-versicolor'],
       [89, 5.6, 3.0, 4.1, 1.3, 'Iris-versicolor'],
       [90, 5.5, 2.5, 4.0, 1.3, 'Iris-versicolor'],
       [91, 5.5, 2.6, 4.4, 1.2, 'Iris-versicolor'],
       [92, 6.1, 3.0, 4.6, 1.4, 'Iris-versicolor'],
       [93, 5.8, 2.6, 4.0, 1.2, 'Iris-versicolor'],
       [94, 5.0, 2.3, 3.3, 1.0, 'Iris-versicolor'],
       [95, 5.6, 2.7, 4.2, 1.3, 'Iris-versicolor'],
       [96, 5.7, 3.0, 4.2, 1.2, 'Iris-versicolor'],
       [97, 5.7, 2.9, 4.2, 1.3, 'Iris-versicolor'],
       [98, 6.2, 2.9, 4.3, 1.3, 'Iris-versicolor'],
       [99, 5.1, 2.5, 3.0, 1.1, 'Iris-versicolor'],
       [100, 5.7, 2.8, 4.1, 1.3, 'Iris-versicolor'],
       [101, 6.3, 3.3, 6.0, 2.5, 'Iris-virginica'],
       [102, 5.8, 2.7, 5.1, 1.9, 'Iris-virginica'],
       [103, 7.1, 3.0, 5.9, 2.1, 'Iris-virginica'],
       [104, 6.3, 2.9, 5.6, 1.8, 'Iris-virginica'],
       [105, 6.5, 3.0, 5.8, 2.2, 'Iris-virginica'],
       [106, 7.6, 3.0, 6.6, 2.1, 'Iris-virginica'],
       [107, 4.9, 2.5, 4.5, 1.7, 'Iris-virginica'],
       [108, 7.3, 2.9, 6.3, 1.8, 'Iris-virginica'],
       [109, 6.7, 2.5, 5.8, 1.8, 'Iris-virginica'],
       [110, 7.2, 3.6, 6.1, 2.5, 'Iris-virginica'],
       [111, 6.5, 3.2, 5.1, 2.0, 'Iris-virginica'],
       [112, 6.4, 2.7, 5.3, 1.9, 'Iris-virginica'],
       [113, 6.8, 3.0, 5.5, 2.1, 'Iris-virginica'],
       [114, 5.7, 2.5, 5.0, 2.0, 'Iris-virginica'],
       [115, 5.8, 2.8, 5.1, 2.4, 'Iris-virginica'],
       [116, 6.4, 3.2, 5.3, 2.3, 'Iris-virginica'],
       [117, 6.5, 3.0, 5.5, 1.8, 'Iris-virginica'],
       [118, 7.7, 3.8, 6.7, 2.2, 'Iris-virginica'],
       [119, 7.7, 2.6, 6.9, 2.3, 'Iris-virginica'],
       [120, 6.0, 2.2, 5.0, 1.5, 'Iris-virginica'],
       [121, 6.9, 3.2, 5.7, 2.3, 'Iris-virginica'],
       [122, 5.6, 2.8, 4.9, 2.0, 'Iris-virginica'],
       [123, 7.7, 2.8, 6.7, 2.0, 'Iris-virginica'],
       [124, 6.3, 2.7, 4.9, 1.8, 'Iris-virginica'],
       [125, 6.7, 3.3, 5.7, 2.1, 'Iris-virginica'],
       [126, 7.2, 3.2, 6.0, 1.8, 'Iris-virginica'],
       [127, 6.2, 2.8, 4.8, 1.8, 'Iris-virginica'],
       [128, 6.1, 3.0, 4.9, 1.8, 'Iris-virginica'],
       [129, 6.4, 2.8, 5.6, 2.1, 'Iris-virginica'],
       [130, 7.2, 3.0, 5.8, 1.6, 'Iris-virginica'],
       [131, 7.4, 2.8, 6.1, 1.9, 'Iris-virginica'],
       [132, 7.9, 3.8, 6.4, 2.0, 'Iris-virginica'],
       [133, 6.4, 2.8, 5.6, 2.2, 'Iris-virginica'],
       [134, 6.3, 2.8, 5.1, 1.5, 'Iris-virginica'],
       [135, 6.1, 2.6, 5.6, 1.4, 'Iris-virginica'],
       [136, 7.7, 3.0, 6.1, 2.3, 'Iris-virginica'],
       [137, 6.3, 3.4, 5.6, 2.4, 'Iris-virginica'],
       [138, 6.4, 3.1, 5.5, 1.8, 'Iris-virginica'],
       [139, 6.0, 3.0, 4.8, 1.8, 'Iris-virginica'],
       [140, 6.9, 3.1, 5.4, 2.1, 'Iris-virginica'],
       [141, 6.7, 3.1, 5.6, 2.4, 'Iris-virginica'],
       [142, 6.9, 3.1, 5.1, 2.3, 'Iris-virginica'],
       [143, 5.8, 2.7, 5.1, 1.9, 'Iris-virginica'],
       [144, 6.8, 3.2, 5.9, 2.3, 'Iris-virginica'],
       [145, 6.7, 3.3, 5.7, 2.5, 'Iris-virginica'],
       [146, 6.7, 3.0, 5.2, 2.3, 'Iris-virginica'],
       [147, 6.3, 2.5, 5.0, 1.9, 'Iris-virginica'],
       [148, 6.5, 3.0, 5.2, 2.0, 'Iris-virginica'],
       [149, 6.2, 3.4, 5.4, 2.3, 'Iris-virginica'],
       [150, 5.9, 3.0, 5.1, 1.8, 'Iris-virginica']], dtype=object)
>>> pd.DataFrame(b)
       0    1    2    3    4               5
0      1  5.1  3.5  1.4  0.2     Iris-setosa
1      2  4.9    3  1.4  0.2     Iris-setosa
2      3  4.7  3.2  1.3  0.2     Iris-setosa
3      4  4.6  3.1  1.5  0.2     Iris-setosa
4      5    5  3.6  1.4  0.2     Iris-setosa
5      6  5.4  3.9  1.7  0.4     Iris-setosa
6      7  4.6  3.4  1.4  0.3     Iris-setosa
7      8    5  3.4  1.5  0.2     Iris-setosa
8      9  4.4  2.9  1.4  0.2     Iris-setosa
9     10  4.9  3.1  1.5  0.1     Iris-setosa
10    11  5.4  3.7  1.5  0.2     Iris-setosa
11    12  4.8  3.4  1.6  0.2     Iris-setosa
12    13  4.8    3  1.4  0.1     Iris-setosa
13    14  4.3    3  1.1  0.1     Iris-setosa
14    15  5.8    4  1.2  0.2     Iris-setosa
15    16  5.7  4.4  1.5  0.4     Iris-setosa
16    17  5.4  3.9  1.3  0.4     Iris-setosa
17    18  5.1  3.5  1.4  0.3     Iris-setosa
18    19  5.7  3.8  1.7  0.3     Iris-setosa
19    20  5.1  3.8  1.5  0.3     Iris-setosa
20    21  5.4  3.4  1.7  0.2     Iris-setosa
21    22  5.1  3.7  1.5  0.4     Iris-setosa
22    23  4.6  3.6    1  0.2     Iris-setosa
23    24  5.1  3.3  1.7  0.5     Iris-setosa
24    25  4.8  3.4  1.9  0.2     Iris-setosa
25    26    5    3  1.6  0.2     Iris-setosa
26    27    5  3.4  1.6  0.4     Iris-setosa
27    28  5.2  3.5  1.5  0.2     Iris-setosa
28    29  5.2  3.4  1.4  0.2     Iris-setosa
29    30  4.7  3.2  1.6  0.2     Iris-setosa
..   ...  ...  ...  ...  ...             ...
120  121  6.9  3.2  5.7  2.3  Iris-virginica
121  122  5.6  2.8  4.9    2  Iris-virginica
122  123  7.7  2.8  6.7    2  Iris-virginica
123  124  6.3  2.7  4.9  1.8  Iris-virginica
124  125  6.7  3.3  5.7  2.1  Iris-virginica
125  126  7.2  3.2    6  1.8  Iris-virginica
126  127  6.2  2.8  4.8  1.8  Iris-virginica
127  128  6.1    3  4.9  1.8  Iris-virginica
128  129  6.4  2.8  5.6  2.1  Iris-virginica
129  130  7.2    3  5.8  1.6  Iris-virginica
130  131  7.4  2.8  6.1  1.9  Iris-virginica
131  132  7.9  3.8  6.4    2  Iris-virginica
132  133  6.4  2.8  5.6  2.2  Iris-virginica
133  134  6.3  2.8  5.1  1.5  Iris-virginica
134  135  6.1  2.6  5.6  1.4  Iris-virginica
135  136  7.7    3  6.1  2.3  Iris-virginica
136  137  6.3  3.4  5.6  2.4  Iris-virginica
137  138  6.4  3.1  5.5  1.8  Iris-virginica
138  139    6    3  4.8  1.8  Iris-virginica
139  140  6.9  3.1  5.4  2.1  Iris-virginica
140  141  6.7  3.1  5.6  2.4  Iris-virginica
141  142  6.9  3.1  5.1  2.3  Iris-virginica
142  143  5.8  2.7  5.1  1.9  Iris-virginica
143  144  6.8  3.2  5.9  2.3  Iris-virginica
144  145  6.7  3.3  5.7  2.5  Iris-virginica
145  146  6.7    3  5.2  2.3  Iris-virginica
146  147  6.3  2.5    5  1.9  Iris-virginica
147  148  6.5    3  5.2    2  Iris-virginica
148  149  6.2  3.4  5.4  2.3  Iris-virginica
149  150  5.9    3  5.1  1.8  Iris-virginica

[150 rows x 6 columns]
>>> pd.DataFrame(b).to_array()
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    pd.DataFrame(b).to_array()
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/generic.py", line 5067, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'to_array'
>>> pd.DataFrame(b).to_ar()
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    pd.DataFrame(b).to_ar()
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/generic.py", line 5067, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'to_ar'
>>> pd.DataFrame(b).to_xarray()
Traceback (most recent call last):
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/generic.py", line 2729, in to_xarray
    import xarray
ModuleNotFoundError: No module named 'xarray'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    pd.DataFrame(b).to_xarray()
  File "/home/anuranjan/.local/lib/python3.6/site-packages/pandas/core/generic.py", line 2732, in to_xarray
    raise ImportError("the xarray library is not installed\n"
ImportError: the xarray library is not installed
you can install via conda
conda install xarray
or via pip
pip install xarray

>>> pd.DataFrame(b).to_numpy()
		      
array([[1, 5.1, 3.5, 1.4, 0.2, 'Iris-setosa'],
       [2, 4.9, 3.0, 1.4, 0.2, 'Iris-setosa'],
       [3, 4.7, 3.2, 1.3, 0.2, 'Iris-setosa'],
       [4, 4.6, 3.1, 1.5, 0.2, 'Iris-setosa'],
       [5, 5.0, 3.6, 1.4, 0.2, 'Iris-setosa'],
       [6, 5.4, 3.9, 1.7, 0.4, 'Iris-setosa'],
       [7, 4.6, 3.4, 1.4, 0.3, 'Iris-setosa'],
       [8, 5.0, 3.4, 1.5, 0.2, 'Iris-setosa'],
       [9, 4.4, 2.9, 1.4, 0.2, 'Iris-setosa'],
       [10, 4.9, 3.1, 1.5, 0.1, 'Iris-setosa'],
       [11, 5.4, 3.7, 1.5, 0.2, 'Iris-setosa'],
       [12, 4.8, 3.4, 1.6, 0.2, 'Iris-setosa'],
       [13, 4.8, 3.0, 1.4, 0.1, 'Iris-setosa'],
       [14, 4.3, 3.0, 1.1, 0.1, 'Iris-setosa'],
       [15, 5.8, 4.0, 1.2, 0.2, 'Iris-setosa'],
       [16, 5.7, 4.4, 1.5, 0.4, 'Iris-setosa'],
       [17, 5.4, 3.9, 1.3, 0.4, 'Iris-setosa'],
       [18, 5.1, 3.5, 1.4, 0.3, 'Iris-setosa'],
       [19, 5.7, 3.8, 1.7, 0.3, 'Iris-setosa'],
       [20, 5.1, 3.8, 1.5, 0.3, 'Iris-setosa'],
       [21, 5.4, 3.4, 1.7, 0.2, 'Iris-setosa'],
       [22, 5.1, 3.7, 1.5, 0.4, 'Iris-setosa'],
       [23, 4.6, 3.6, 1.0, 0.2, 'Iris-setosa'],
       [24, 5.1, 3.3, 1.7, 0.5, 'Iris-setosa'],
       [25, 4.8, 3.4, 1.9, 0.2, 'Iris-setosa'],
       [26, 5.0, 3.0, 1.6, 0.2, 'Iris-setosa'],
       [27, 5.0, 3.4, 1.6, 0.4, 'Iris-setosa'],
       [28, 5.2, 3.5, 1.5, 0.2, 'Iris-setosa'],
       [29, 5.2, 3.4, 1.4, 0.2, 'Iris-setosa'],
       [30, 4.7, 3.2, 1.6, 0.2, 'Iris-setosa'],
       [31, 4.8, 3.1, 1.6, 0.2, 'Iris-setosa'],
       [32, 5.4, 3.4, 1.5, 0.4, 'Iris-setosa'],
       [33, 5.2, 4.1, 1.5, 0.1, 'Iris-setosa'],
       [34, 5.5, 4.2, 1.4, 0.2, 'Iris-setosa'],
       [35, 4.9, 3.1, 1.5, 0.1, 'Iris-setosa'],
       [36, 5.0, 3.2, 1.2, 0.2, 'Iris-setosa'],
       [37, 5.5, 3.5, 1.3, 0.2, 'Iris-setosa'],
       [38, 4.9, 3.1, 1.5, 0.1, 'Iris-setosa'],
       [39, 4.4, 3.0, 1.3, 0.2, 'Iris-setosa'],
       [40, 5.1, 3.4, 1.5, 0.2, 'Iris-setosa'],
       [41, 5.0, 3.5, 1.3, 0.3, 'Iris-setosa'],
       [42, 4.5, 2.3, 1.3, 0.3, 'Iris-setosa'],
       [43, 4.4, 3.2, 1.3, 0.2, 'Iris-setosa'],
       [44, 5.0, 3.5, 1.6, 0.6, 'Iris-setosa'],
       [45, 5.1, 3.8, 1.9, 0.4, 'Iris-setosa'],
       [46, 4.8, 3.0, 1.4, 0.3, 'Iris-setosa'],
       [47, 5.1, 3.8, 1.6, 0.2, 'Iris-setosa'],
       [48, 4.6, 3.2, 1.4, 0.2, 'Iris-setosa'],
       [49, 5.3, 3.7, 1.5, 0.2, 'Iris-setosa'],
       [50, 5.0, 3.3, 1.4, 0.2, 'Iris-setosa'],
       [51, 7.0, 3.2, 4.7, 1.4, 'Iris-versicolor'],
       [52, 6.4, 3.2, 4.5, 1.5, 'Iris-versicolor'],
       [53, 6.9, 3.1, 4.9, 1.5, 'Iris-versicolor'],
       [54, 5.5, 2.3, 4.0, 1.3, 'Iris-versicolor'],
       [55, 6.5, 2.8, 4.6, 1.5, 'Iris-versicolor'],
       [56, 5.7, 2.8, 4.5, 1.3, 'Iris-versicolor'],
       [57, 6.3, 3.3, 4.7, 1.6, 'Iris-versicolor'],
       [58, 4.9, 2.4, 3.3, 1.0, 'Iris-versicolor'],
       [59, 6.6, 2.9, 4.6, 1.3, 'Iris-versicolor'],
       [60, 5.2, 2.7, 3.9, 1.4, 'Iris-versicolor'],
       [61, 5.0, 2.0, 3.5, 1.0, 'Iris-versicolor'],
       [62, 5.9, 3.0, 4.2, 1.5, 'Iris-versicolor'],
       [63, 6.0, 2.2, 4.0, 1.0, 'Iris-versicolor'],
       [64, 6.1, 2.9, 4.7, 1.4, 'Iris-versicolor'],
       [65, 5.6, 2.9, 3.6, 1.3, 'Iris-versicolor'],
       [66, 6.7, 3.1, 4.4, 1.4, 'Iris-versicolor'],
       [67, 5.6, 3.0, 4.5, 1.5, 'Iris-versicolor'],
       [68, 5.8, 2.7, 4.1, 1.0, 'Iris-versicolor'],
       [69, 6.2, 2.2, 4.5, 1.5, 'Iris-versicolor'],
       [70, 5.6, 2.5, 3.9, 1.1, 'Iris-versicolor'],
       [71, 5.9, 3.2, 4.8, 1.8, 'Iris-versicolor'],
       [72, 6.1, 2.8, 4.0, 1.3, 'Iris-versicolor'],
       [73, 6.3, 2.5, 4.9, 1.5, 'Iris-versicolor'],
       [74, 6.1, 2.8, 4.7, 1.2, 'Iris-versicolor'],
       [75, 6.4, 2.9, 4.3, 1.3, 'Iris-versicolor'],
       [76, 6.6, 3.0, 4.4, 1.4, 'Iris-versicolor'],
       [77, 6.8, 2.8, 4.8, 1.4, 'Iris-versicolor'],
       [78, 6.7, 3.0, 5.0, 1.7, 'Iris-versicolor'],
       [79, 6.0, 2.9, 4.5, 1.5, 'Iris-versicolor'],
       [80, 5.7, 2.6, 3.5, 1.0, 'Iris-versicolor'],
       [81, 5.5, 2.4, 3.8, 1.1, 'Iris-versicolor'],
       [82, 5.5, 2.4, 3.7, 1.0, 'Iris-versicolor'],
       [83, 5.8, 2.7, 3.9, 1.2, 'Iris-versicolor'],
       [84, 6.0, 2.7, 5.1, 1.6, 'Iris-versicolor'],
       [85, 5.4, 3.0, 4.5, 1.5, 'Iris-versicolor'],
       [86, 6.0, 3.4, 4.5, 1.6, 'Iris-versicolor'],
       [87, 6.7, 3.1, 4.7, 1.5, 'Iris-versicolor'],
       [88, 6.3, 2.3, 4.4, 1.3, 'Iris-versicolor'],
       [89, 5.6, 3.0, 4.1, 1.3, 'Iris-versicolor'],
       [90, 5.5, 2.5, 4.0, 1.3, 'Iris-versicolor'],
       [91, 5.5, 2.6, 4.4, 1.2, 'Iris-versicolor'],
       [92, 6.1, 3.0, 4.6, 1.4, 'Iris-versicolor'],
       [93, 5.8, 2.6, 4.0, 1.2, 'Iris-versicolor'],
       [94, 5.0, 2.3, 3.3, 1.0, 'Iris-versicolor'],
       [95, 5.6, 2.7, 4.2, 1.3, 'Iris-versicolor'],
       [96, 5.7, 3.0, 4.2, 1.2, 'Iris-versicolor'],
       [97, 5.7, 2.9, 4.2, 1.3, 'Iris-versicolor'],
       [98, 6.2, 2.9, 4.3, 1.3, 'Iris-versicolor'],
       [99, 5.1, 2.5, 3.0, 1.1, 'Iris-versicolor'],
       [100, 5.7, 2.8, 4.1, 1.3, 'Iris-versicolor'],
       [101, 6.3, 3.3, 6.0, 2.5, 'Iris-virginica'],
       [102, 5.8, 2.7, 5.1, 1.9, 'Iris-virginica'],
       [103, 7.1, 3.0, 5.9, 2.1, 'Iris-virginica'],
       [104, 6.3, 2.9, 5.6, 1.8, 'Iris-virginica'],
       [105, 6.5, 3.0, 5.8, 2.2, 'Iris-virginica'],
       [106, 7.6, 3.0, 6.6, 2.1, 'Iris-virginica'],
       [107, 4.9, 2.5, 4.5, 1.7, 'Iris-virginica'],
       [108, 7.3, 2.9, 6.3, 1.8, 'Iris-virginica'],
       [109, 6.7, 2.5, 5.8, 1.8, 'Iris-virginica'],
       [110, 7.2, 3.6, 6.1, 2.5, 'Iris-virginica'],
       [111, 6.5, 3.2, 5.1, 2.0, 'Iris-virginica'],
       [112, 6.4, 2.7, 5.3, 1.9, 'Iris-virginica'],
       [113, 6.8, 3.0, 5.5, 2.1, 'Iris-virginica'],
       [114, 5.7, 2.5, 5.0, 2.0, 'Iris-virginica'],
       [115, 5.8, 2.8, 5.1, 2.4, 'Iris-virginica'],
       [116, 6.4, 3.2, 5.3, 2.3, 'Iris-virginica'],
       [117, 6.5, 3.0, 5.5, 1.8, 'Iris-virginica'],
       [118, 7.7, 3.8, 6.7, 2.2, 'Iris-virginica'],
       [119, 7.7, 2.6, 6.9, 2.3, 'Iris-virginica'],
       [120, 6.0, 2.2, 5.0, 1.5, 'Iris-virginica'],
       [121, 6.9, 3.2, 5.7, 2.3, 'Iris-virginica'],
       [122, 5.6, 2.8, 4.9, 2.0, 'Iris-virginica'],
       [123, 7.7, 2.8, 6.7, 2.0, 'Iris-virginica'],
       [124, 6.3, 2.7, 4.9, 1.8, 'Iris-virginica'],
       [125, 6.7, 3.3, 5.7, 2.1, 'Iris-virginica'],
       [126, 7.2, 3.2, 6.0, 1.8, 'Iris-virginica'],
       [127, 6.2, 2.8, 4.8, 1.8, 'Iris-virginica'],
       [128, 6.1, 3.0, 4.9, 1.8, 'Iris-virginica'],
       [129, 6.4, 2.8, 5.6, 2.1, 'Iris-virginica'],
       [130, 7.2, 3.0, 5.8, 1.6, 'Iris-virginica'],
       [131, 7.4, 2.8, 6.1, 1.9, 'Iris-virginica'],
       [132, 7.9, 3.8, 6.4, 2.0, 'Iris-virginica'],
       [133, 6.4, 2.8, 5.6, 2.2, 'Iris-virginica'],
       [134, 6.3, 2.8, 5.1, 1.5, 'Iris-virginica'],
       [135, 6.1, 2.6, 5.6, 1.4, 'Iris-virginica'],
       [136, 7.7, 3.0, 6.1, 2.3, 'Iris-virginica'],
       [137, 6.3, 3.4, 5.6, 2.4, 'Iris-virginica'],
       [138, 6.4, 3.1, 5.5, 1.8, 'Iris-virginica'],
       [139, 6.0, 3.0, 4.8, 1.8, 'Iris-virginica'],
       [140, 6.9, 3.1, 5.4, 2.1, 'Iris-virginica'],
       [141, 6.7, 3.1, 5.6, 2.4, 'Iris-virginica'],
       [142, 6.9, 3.1, 5.1, 2.3, 'Iris-virginica'],
       [143, 5.8, 2.7, 5.1, 1.9, 'Iris-virginica'],
       [144, 6.8, 3.2, 5.9, 2.3, 'Iris-virginica'],
       [145, 6.7, 3.3, 5.7, 2.5, 'Iris-virginica'],
       [146, 6.7, 3.0, 5.2, 2.3, 'Iris-virginica'],
       [147, 6.3, 2.5, 5.0, 1.9, 'Iris-virginica'],
       [148, 6.5, 3.0, 5.2, 2.0, 'Iris-virginica'],
       [149, 6.2, 3.4, 5.4, 2.3, 'Iris-virginica'],
       [150, 5.9, 3.0, 5.1, 1.8, 'Iris-virginica']], dtype=object)
>>> 
