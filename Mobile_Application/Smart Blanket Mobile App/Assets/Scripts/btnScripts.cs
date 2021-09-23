using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class btnScripts : MonoBehaviour
{

    public Text label;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void powerOnBlanket(){ // this method will later be used to power on the blanket
        Debug.Log("Tapped: " + label.text);
    }

    public void powerOffBlanket(){
        Debug.Log("Tapped: " + label.text);
    }
}
