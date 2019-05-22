using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using uPLibrary.Networking.M2Mqtt;
using uPLibrary.Networking.M2Mqtt.Messages;
using M2MqttUnity;

namespace M2MqttUnity.Examples
{
    public class Emyl : M2MqttUnityClient
    {
        Boolean send = false;
        // Start is called before the first frame update

        protected override void OnConnected()
        {
            base.OnConnected();
            send = true;
            Debug.Log("connected");

        }
        protected override void Start()
        {
            Debug.Log("start is begonnen");
            brokerAddress = "192.168.0.69";
            brokerPort = 1883;
            autoConnect = true;
            base.Start();
            Debug.Log("start is uitgevoerd");
        }
        protected override void DecodeMessage(string topic, byte[] message)
        {
            Debug.LogFormat("Message received on topic: {0}", topic);
            string msg = System.Text.Encoding.UTF8.GetString(message);
            Debug.Log("Received: " + msg);

        }

        // Update is called once per frame
        protected override void Update()
        {
            base.Update();
           

        }

        public class Coordinaten
        {
            public int X;
            public int Y;
        }
    }
}