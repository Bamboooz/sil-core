def unsupported_exception():
    return "\033[91mError: PySil library does not support your operating system.\033[0m"


def unsupported_func():
    return "\033[91mError: Currently function your trying to use is unavailable for your operating system.\033[0m"


def not_linux():
    return "\033[91mError: Cannot detect distro when your os is not Linux.\033[0m"


def no_linux_temp_driver():
    return "\033[91mError: Your Linux does not have driver required to get cpu temp.\033[0m"
