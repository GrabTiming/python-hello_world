"""
关于time模块
"""

time_format1 = "YYMMDD"


def timestamp_to_string(timestamp, format_str="%Y-%m-%d %H:%M"):
    """
    将时间戳转换为格式化的时间字符串

    Args:
        timestamp: 时间戳（int或float）
        format_str: 时间格式字符串，默认为"%Y-%m-%d %H:%M:%S"

    Returns:
        str: 格式化的时间字符串
    """
    time_struct = time.localtime(timestamp)
    return time.strftime(format_str, time_struct)


def string_to_timestamp(time_string, format_str="%Y-%m-%d %H:%M"):
    """
    将格式化的时间字符串转换为时间戳

    Args:
        time_string: 时间字符串
        format_str: 时间格式字符串，默认为"%Y-%m-%d %H:%M"

    Returns:
        float: 时间戳
    """
    time_struct = time.strptime(time_string, format_str)
    return time.mktime(time_struct)

if __name__ == "__main__":
    import time
    now = int(time.time())
    print(now) # 时间戳
    print(time.localtime(now)) # 本地时区


    print(timestamp_to_string(now))

    time_str = "2025-08-19"
    print(string_to_timestamp(time_str,"%Y-%m-%d"))

