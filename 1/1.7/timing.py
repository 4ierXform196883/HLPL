import functools
import time
from datetime import datetime


class TimeIt:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.history = []

    def __call__(self, *args, **kwargs):
        record = {
            "name": self.func.__name__,
            "args": args,
            "kwargs": kwargs,
            "result": None,
            "elapsed": None,
            "called_at": datetime.now(),
        }
        start = time.perf_counter()
        try:
            result = self.func(*args, **kwargs)
            record["result"] = result
            return result
        except Exception as exc:
            # В историю пишем тип исключения, само исключение пробрасываем дальше
            record["result"] = type(exc)
            raise
        finally:
            record["elapsed"] = time.perf_counter() - start
            self.history.append(record)

    def last(self):
        """Последняя запись истории (None, если вызовов не было)."""
        return self.history[-1] if self.history else None

    def count(self):
        return len(self.history)

    def clear(self):
        self.history.clear()

    def report(self):
        if not self.history:
            print(f"{self.func.__name__}: история пуста")
            return
        for i, rec in enumerate(self.history, 1):
            params = [repr(a) for a in rec["args"]]
            params += [f"{k}={v!r}" for k, v in rec["kwargs"].items()]
            
            result = rec["result"]

            if isinstance(result, type) and issubclass(result, BaseException):
                outcome = f"исключение {result.__name__}"
            else:
                outcome = f"результат {result!r}"
            print(
                f"{i}. [{rec['called_at']:%Y-%m-%d %H:%M:%S}] "
                f"{rec['name']}({', '.join(params)}) -> {outcome}, "
                f"время {rec['elapsed']:.6f} с"
            )


if __name__ == "__main__":

    @TimeIt
    def divide(a, b=1):
        return a / b

    divide(10, 2)
    divide(7, b=2)
    try:
        divide(1, 0)
    except ZeroDivisionError:
        pass

    divide.report()
    print(' ')

    print("Вызовов:", divide.count())
    print("Последний:", divide.last())
    print(' ')
    
    divide.clear()
    print("История после clear():")
    divide.report()
