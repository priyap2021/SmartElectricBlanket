using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class btnScripts : MonoBehaviour
{
   
    public Text label;
    WebSocketClient ws;

    // Start is called before the first frame update
    void Start()
    {
        // get acces to the WebSocket component
        ws = gameObject.AddComponent(typeof(WebSocketClient)) as WebSocketClient;
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void powerOnBlanket(){ // this method will later be used to power on the blanket
        Debug.Log("Tapped: " + label.text);
        ws.sendMessage("ON"); // send a message to the Server saying "ON"
    }

    public void powerOffBlanket(){
        Debug.Log("Tapped: " + label.text);
        ws.sendMessage("OFF"); // send a message to the Server saying "OFF"
    }
}
