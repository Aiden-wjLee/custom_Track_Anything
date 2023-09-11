import numpy as np
import socket

# 데이터 생성
data = np.array([[1, 2], [3, 4]])

# UDP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# numpy 배열을 바이트 스트림으로 변환
data_bytes = data.tobytes()

# 데이터 전송
sock.sendto(data_bytes, ('192.168.50.5', 22))

sock.close()