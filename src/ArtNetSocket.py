import socket
import threading

UDP_IP = "127.0.0.1"
UDP_PORT = 6454

class ArtNetSocket:
    def __init__(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.bind((UDP_IP, UDP_PORT))
        self._terminate_thread = False

        self._thread = threading.Thread(target=self.thread_task)
        self._thread.start()

    def disconnect(self):
        if self._socket is not None:
            self._socket.close()
        self._socket = None

    def shutdown(self):
        self._terminate_thread = True
        self._thread.join()

    def thread_task(self):
        try:
            while True:
                if self._terminate_thread:
                    self.disconnect()
                    break
                data, addr = self._socket.recvfrom(1024)
        except socket.error:
            # reconnect socket
            self.disconnect()
            self._socket = self.connect()
        except Exception:
            pass