using UnityEngine;
using WebSocketSharp;

public class WebSocketClient : MonoBehaviour
{
    WebSocket ws;
    void Start()
    {
        ws = new WebSocket("ws://10.16.84.97:8080");// creates the initial websocket, and use port 8080
        ws.Connect(); // connect the websocket to the server
        Debug.Log("Conneted to ther server");
         ws.OnMessage += (sender, e) =>
        {
            Debug.Log("Message Received from "+((WebSocket)sender).Url+", Data : "+e.Data);
        };
    }
    
    void Update()
    {
        if (ws == null){ // if the websocket hasn't started, just return
            Debug.Log("Something went wrong");
            return;
        }
        
    }

    public void sendMessage(string message) // accepts a message to be sent to the server
    {
        ws.Send(message);
    }
}