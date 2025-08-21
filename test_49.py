"""
关于time模块
strftime 方法 将时间戳转为 对应格式的时间字符串
strptime 方法 将时间字符串 转为 时间戳
"""


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


def get_today_zero():
    """获取当天的0点"""
    now = int(time.time())
    today_zero = time.strftime("%Y-%m-%d", time.localtime(now)) # 先转为整天 时间字符串
    today_zero = time.strptime(today_zero,"%Y-%m-%d") # 再转 struct.time
    today_zero = int(time.mktime(today_zero)) # 最后再转回时间戳
    return today_zero,now

if __name__ == "__main__":
    import time
    now = int(time.time())
    print(now) # 时间戳
    print(time.localtime(now)) # 本地时区


    print(timestamp_to_string(now))

    time_str = "2025-08-19"
    print(string_to_timestamp(time_str,"%Y-%m-%d"))

    time_str = "2025-08-21"
    timestamp =  time.strptime(time_str,"%Y-%m-%d")
    print(timestamp)
    print(time.strftime("%Y-%m-%d %H:%M:%S", timestamp))

    now = int(time.time())
    time2 =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now))
    print(time2)

    today_zero,now = get_today_zero()
    print(today_zero,now)