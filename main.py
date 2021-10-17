import socket
import threading

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
server.bind(("127.0.0.1", 2000))
server.listen(5)

users = []


def send_all(data):
    for user in users:
        user.send(data)


def listen_users(user):
    print("Listen users")

    while True:
        data = user.recv(2048)
        print(f"User sent {data}")
        send_all(data)


def start_server():
    while True:
        user_socket, address = server.accept()

        print(f"User {address[0]} connected")
        users.append(user_socket)

        listen_accepted_users = threading.Thread(
            target=listen_users,
            args=(user_socket,))
        listen_accepted_users.start()
        listen_accepted_users.join()


if __name__ == '__main__':
    start_server()
