using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;
using UnityEngine.UI;

public class sliderScript : MonoBehaviour
{
    
    [SerializeField] private Slider _slider;

    [SerializeField] public TextMeshProUGUI _sliderText;

    [SerializeField] public TextMeshProUGUI currentTemp;
    
    [SerializeField] public string temp;
    
    WebSocketClient ws;

    // Start is called before the first frame update
    void Start()
    {
        // get acces to the WebSocket component
        ws = gameObject.AddComponent(typeof(WebSocketClient)) as WebSocketClient;

        _slider.onValueChanged.AddListener((v) => { // added a listener to tell when the temperature is changed
            //currentTemp = getCurrentTemp();
            temp = v.ToString("0");
            _sliderText.text = v.ToString("0°C");
            Debug.Log("Current temp is " + temp);
            ws.sendMessage(temp);
            
            //Debug.Log("Current temp is " + currentTemp.text);
            //ws.sendMessage(currentTemp.text); // send the server the current temperature
        });
    }
    // get the current value of the temperature
    TextMeshProUGUI getCurrentTemp(){
        return _sliderText;
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
