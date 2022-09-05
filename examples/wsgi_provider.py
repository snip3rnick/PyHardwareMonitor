import json
import time
from threading import Timer, Lock
from wsgiref import simple_server
from HardwareMonitor.Util import OpenComputer, ToBuiltinTypes


class IndefiniteTimer(Timer):
    def start(self):
        super().start()
        return self

    def run(self):
        delay = self.interval
        while not self.finished.wait(delay):
            start_time = time.perf_counter()
            self.function(*self.args, **self.kwargs)
            delay = max(0, self.interval - (time.perf_counter() - start_time))


class SensorApp():
    def __init__(self, port=8085, interval=1.0):
        self.interval = interval
        self.mutex    = Lock()
        self.computer = OpenComputer(all=True, time_window=interval)
        self.timer    = IndefiniteTimer(interval, self.update).start()
        self.http     = simple_server.make_server('', port, self.handler)

    @property
    def port(self):
        return self.http.server_port

    def update(self):
        with self.mutex:
            self.computer.Update()

    def getSensors(self):
        with self.mutex:
            return ToBuiltinTypes(self.computer.Hardware)

    def serve(self):
        self.http.serve_forever()

    def close(self):
        self.http.server_close()

    def handler(self, environ, respond):
        if environ['PATH_INFO'].lower() == "/data.json":
            json_str = json.dumps(self.getSensors())
            respond('200 OK', [('Content-Type', 'application/json')])
            return [json_str.encode()]
        else:
            respond('404 Not Found', [('Content-Type', 'application/json')])
            return [b'not found']


def main():
    app = SensorApp()
    print(f"Serving on port {app.port}, press 'ctrl + C' to stop")
    try:
        app.serve()
    except KeyboardInterrupt:
        app.close()

if __name__ == "__main__":
    main()
