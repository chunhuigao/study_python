# singleton.py
class _Singleton:
    def __init__(self):
        self.name = "唯一实例"

instance = _Singleton()

