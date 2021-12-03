using UnityEngine;
using WebSocketSharp;

public class WebSocketClient : MonoBehaviour
{
    WebSocket ws;
    void Start()
    {
        ws = new WebSocket("ws://10.16.84.97:8080"); // creates the initial websocket, and use port 8080
        ws.Connect(); // connect the websocket to the server
    }
    
    void Update()
    {
        if (ws == null){ // if the websocket hasn't started, just return
            return;
        }
        
    }

    public void sendMessage(string message) // accepts a message to be sent to the server
    {
        ws.Send(message);
    }
}
