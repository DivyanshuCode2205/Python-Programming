s = {8, 7, 12, "Harry", [1, 2]}

"""set data type only contains hasable elements and here list is not hasable

hasable elements --> elements that have fixed unique ID (int, string, float, bool, tuple)
non-hasable elements --> elements that have not unique ID (list, dict, set)
"""

'''
Rule of thumb:

Immutable types → usually hashable (int, float, str, tuple if elements are also hashable, frozenset)

Mutable types → not hashable (list, dict, set)

'''