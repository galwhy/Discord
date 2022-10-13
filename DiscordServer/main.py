from Objects import Server


def main():
    port = 6900
    server = Server.Server(port)
    server.start()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
