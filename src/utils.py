import time


class ElapsedTime:
    begin = 0
    end = 0

    def start(self):
        self.begin = time.time()
        return self

    def done(self):
        self.end = time.time()
        return self

    @property
    def result(self):
        elapsed = (self.end - self.begin) * 1000
        return f", elapsed: {str(elapsed)} ms"
