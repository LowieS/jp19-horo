using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using uPLibrary.Networking.M2Mqtt;

public class MQTT : MonoBehaviour
{
    private MqttClient client;
    // The connection information
    public string brokerHostname = "192.168.0.69";
    public int brokerPort = 8883;
    public string userName = "test";
    public string password = "test";
    public TextAsset certificate;
    // listen on all the Topic
    static string subTopic = "#";
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
