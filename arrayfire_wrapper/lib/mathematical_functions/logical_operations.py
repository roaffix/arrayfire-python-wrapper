from arrayfire_wrapper.defines import AFArray
from arrayfire_wrapper.lib._utility import binary_op, unary_op


def and_(lhs: AFArray, rhs: AFArray, /) -> AFArray:
    """
    source:
    """
    return binary_op("and", lhs, rhs)


def bitand(lhs: AFArray, rhs: AFArray, /) -> AFArray:
    """
    source: https://arrayfire.org/docs/group__arith__func__bitand.htm#ga45c0779ade4703708596df11cca98800
    """
    return binary_op(bitand.__name__, lhs, rhs)


def bitnot(arr: AFArray, /) -> AFArray:
    """
    source: https://arrayfire.org/docs/group__arith__func__bitnot.htm#gaf97e8a38aab59ed2d3a742515467d01e
    """
    return unary_op(bitnot.__name__, arr)


def bitor(lhs: AFArray, rhs: AFArray, /) -> AFArray:
    """
    source: https://arrayfire.org/docs/group__arith__func__bitor.htm#ga84c99f77d1d83fd53f949b4d67b5b210
    """
    return binary_op(bitor.__name__, lhs, rhs)


def bitxor(lhs: AFArray, rhs: AFArray, /) -> AFArray:
    """
    source: https://arrayfire.org/docs/group__arith__func__bitxor.htm#ga8188620da6b432998e55fdd1fad22100
    """
    return binary_op(bitxor.__name__, lhs, rhs)


def eq(lhs: AFArray, rhs: AFArray, /) -> AFArray:
    """
    source: https://arrayfire.org/docs/group__arith__func__eq.htm#ga76d2da7716831616bb81effa9e163693
    """
    return binary_op(eq.__name__, lhs, rhs)


def ge(lhs: AFArray, rhs: AFArray, /) -> AFArray:
    """
    source: https://arrayfire.org/docs/group__arith__func__ge.htm#ga4513f212e0b0a22dcf4653e89c85e3d9
    """
    return binary_op(ge.__name__, lhs, rhs)


def gt(lhs: AFArray, rhs: AFArray, /) -> AFArray:
    """
    source: https://arrayfire.org/docs/group__arith__func__gt.htm#ga4e65603259515de8939899a163ebaf9e
    """
    return binary_op(gt.__name__, lhs, rhs)


def le(lhs: AFArray, rhs: AFArray, /) -> AFArray:
    """
    source: https://arrayfire.org/docs/group__arith__func__le.htm#gad5535ce64dbed46d0773fd494e84e922
    """
    return binary_op(le.__name__, lhs, rhs)


def lt(lhs: AFArray, rhs: AFArray, /) -> AFArray:
    """
    source: https://arrayfire.org/docs/arith_8h.htm#ae7aa04bf23b32bb11c4bab8bdd637103
    """
    return binary_op(lt.__name__, lhs, rhs)


def neq(lhs: AFArray, rhs: AFArray, /) -> AFArray:
    """
    source: https://arrayfire.org/docs/group__arith__func__neq.htm#gae4ee8bd06a410f259f1493fb811ce441
    """
    return binary_op(neq.__name__, lhs, rhs)


def not_(arr: AFArray, /) -> AFArray:
    """
    source:
    """
    return unary_op("not", arr)


def or_(lhs: AFArray, rhs: AFArray, /) -> AFArray:
    """
    source:
    """
    return binary_op("or", lhs, rhs)
