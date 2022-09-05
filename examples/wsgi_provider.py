import json
from wsgiref import simple_server
from HardwareMonitor.Util import OpenComputer, ToBuiltinTypes


class SensorApp():
    def __init__(self):
        self.computer = OpenComputer(all=True)
        self.http = simple_server.make_server('', 8085, self.handler)

    @property
    def port(self):
        return self.http.server_port

    def serve(self):
        self.http.serve_forever()

    def close(self):
        self.http.server_close()

    def handler(self, environ, respond):
        if environ['PATH_INFO'].lower() == "/data.json":
            json_str = json.dumps(ToBuiltinTypes(self.computer.Update().Hardware))
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
