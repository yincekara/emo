import socket


def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

def main():
    print ("main")
    connected = is_connected()
    print (connected)
   

if __name__ == "__main__":main()    
    
