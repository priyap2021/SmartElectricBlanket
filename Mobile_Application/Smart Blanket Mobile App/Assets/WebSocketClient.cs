using WebSocketSharp;
using UnityEngine;

public class WebSocketClient : MonoBehaviour
{
    WebSocket ws;
    void Start()
    {
        ws = new WebSocket("ws://localhost:8080"); // creates the initial websocket, and use port 8080
        ws.OnMessage += (sender, message) =>
        { // if the server sent a message, print it out
            Debug.Log("Got a message from " +((WebSocket)sender).Url + ". Data sent: " + message.Data);
        };
        
        ws.Connect(); // connect the websocket to the server

        
    }
    
    void Update()
    {
        if (ws == null){ // if there's an issue with the websocket, and it's null, just return
            return;
        }
        
    }
}
