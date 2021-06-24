import socket
import threading

UDP_IP = "127.0.0.1"
UDP_PORT = 6454

class ArtNetSocket:
    def __init__(self, channel_manager):
        self._channel_manager = channel_manager
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.bind((UDP_IP, UDP_PORT))
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.settimeout(0.25)
        self._terminate_thread = False

        self._thread = threading.Thread(target=self.thread_task)
        self._thread.start()

    def connect(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        self._socket.bind((UDP_IP, UDP_PORT))
        
        return self._socket

    def disconnect(self):
        if self._socket is not None:
            self._socket.close()
        self._socket = None

    def shutdown(self):
        self._terminate_thread = True
        self._thread.join()

    def thread_task(self):
        while True:
            try:
                while True:
                    if self._terminate_thread:
                        self.disconnect()
                        return
                    data = self._socket.recv(1024)

                    if(self.check_packet(data)):
                        self.parse_packet(data)

            except socket.timeout:
                # do nothing
                pass
            except socket.error:
                # reconnect socket
                self.disconnect()
                self._socket = self.connect()
            except Exception:
                pass

    def check_packet(self, packet):
        if len(packet) > 18 and packet[:8] == b'Art-Net\x00' and int.from_bytes(packet[8:10], "little") == 0x5000:
            return True
        else:
            return False

    def parse_packet(self, packet):
        universe = int.from_bytes(packet[14:16], "little")
        channels = int.from_bytes(packet[16:18], "big")
        channel_data = packet[18:18+channels]

        self._channel_manager.ingest_data(universe, channels, channel_data)