from enum import unique
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

                if(self.check_packet(data)):
                    self.parse_packet(data)

        except socket.error:
            # reconnect socket
            self.disconnect()
            self._socket = self.connect()
        except Exception:
            pass

    def check_packet(self, packet):
        if(packet[:8] == b'Art-Net\x00' and int.from_bytes(packet[8:10], "little") == 0x5000):
            return True
        else:
            return False

    def parse_packet(self, packet):
        universe = int.from_bytes(packet[14:16], "little")
        channel_num = int.from_bytes(packet[16:18], "big")
        channels = packet[18:18+channel_num]