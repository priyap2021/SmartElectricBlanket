using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class OnBtnScript : MonoBehaviour
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

    public void onTapped(){
        Debug.Log("Tapped: " + label.text);
    }
}
