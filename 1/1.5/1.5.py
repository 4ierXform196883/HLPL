from datetime import datetime


class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, filename="app.log"):
        if self._initialized:
            return
        self.filename = filename
        self._initialized = True

    def _write(self, status, message):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(f"[{status}] {time}: {message}\n")

    def debug(self, message):
        self._write("DEBUG", message)

    def info(self, message):
        self._write("INFO", message)

    def warn(self, message):
        self._write("WARN", message)

    def error(self, message):
        self._write("ERROR", message)

    def critical(self, message):
        self._write("CRITICAL", message)


if __name__ == "__main__":
    log1 = Logger()
    log2 = Logger("other.log")
    print("Один и тот же объект:", log1 is log2)

    log1.debug("отладочное сообщение")
    log1.info("информационное сообщение")
    log2.warn("предупреждение")
    log2.error("ошибка")
    log2.critical("критическая ошибка")
