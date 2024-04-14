from simple_websocket_server import WebSocketServer, WebSocket


class SimpleEcho(WebSocket):
    def handle(self):
        #x = int(self.data)
        print ("I got " + self.data)
        x = int(self.data)
        x+=1
        print ("new number is " + str(x))
        self.send_message(str(x))
        #self.send_message(self.data)
        #self.send_message(x+1)
        # echo message back to client
        #self.send_message(self.d
        #self.send_message(self.data)

    def connected(self):
        print(self.address, 'connected')

    def handle_close(self):
        print(self.address, 'closed')


server = WebSocketServer('0.0.0.0', 3000, SimpleEcho)
server.serve_forever()