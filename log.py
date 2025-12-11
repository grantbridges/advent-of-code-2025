from enum import Enum

class LogLevel(Enum):
    Debug = 0,
    Info = 1,
    Warning = 2,
    Error = 3

LOG_LEVEL = LogLevel.Debug

def log(msg, level: LogLevel):
    if level.value >= LOG_LEVEL.value:
        log_level_label = ""
        if level == LogLevel.Debug:
            log_level_label += "DBG "
        elif level == LogLevel.Info:
            log_level_label += "INF "
        elif level == LogLevel.Warning:
            log_level_label += "WRN "
        elif level == LogLevel.Error:
            log_level_label += "ERR "

        print(log_level_label + msg)

def log_debug(msg):
    log(msg, LogLevel.Debug)

def log_info(msg):
    log(msg, LogLevel.Info)

def log_warning(msg):
    log(msg, LogLevel.Warning)

def log_error(msg):
    log(msg, LogLevel.Error)