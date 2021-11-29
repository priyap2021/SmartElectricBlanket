const WebSocket = require('ws');
const PORT = 8080;
const webSocketServer = new WebSocket.Server({
    port: PORT },()=>{

    console.log('server starts')
});

webSocketServer.on('connection', function (socket) {
   
    // Incoming Socket
    socket.on('message', function (message) {
        console.log("Received message from client: "  + message);
        // message to broadcast
        webSocketServer.clients.forEach(function (key) {
            key.send( message);
        });
    });
    //listening and close the port
    socket.on('Listenting',()=>{
        console.log('Listen to port 8080')
    })
    socket.on('close', function () {
        console.log('Client is not connected');
    })
  
});





