using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using uPLibrary.Networking.M2Mqtt;
using uPLibrary.Networking.M2Mqtt.Messages;
using M2MqttUnity;

public class NewBehaviourScript : M2MqttUnityClient
{
    public void TestPublish()
    {
        client.Publish("test_channel", System.Text.Encoding.UTF8.GetBytes("Test message"), MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
        Debug.Log("Test message published");
    }
    // Start is called before the first frame update
    protected override void Start()
    {
        base.Start();
        TestPublish();
    }

    // Update is called once per frame
    protected override void Update()
    {
        
    }
}
