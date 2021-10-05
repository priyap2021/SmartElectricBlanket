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
    
    // Start is called before the first frame update
    void Start()
    {
        _slider.onValueChanged.AddListener((v) => {
            _sliderText.text = v.ToString("0°C");

            currentTemp = getCurrentTemp();
            Debug.Log("Current temp is " + currentTemp.text);
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
