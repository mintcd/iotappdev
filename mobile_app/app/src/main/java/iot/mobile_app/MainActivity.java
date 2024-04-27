package com.example.demoiot;
import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;

import android.util.Log;
import android.widget.TextView;

import com.github.angads25.toggle.interfaces.OnToggledListener;
import com.github.angads25.toggle.model.ToggleableView;
import com.github.angads25.toggle.widget.LabeledSwitch;

import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallbackExtended;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;

import java.nio.charset.Charset;

public class MainActivity extends AppCompatActivity {
    MQTTHelper mqttHelper;
    TextView txtHumi, txtTemp, txtLi;
    LabeledSwitch LED, PUMP;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        txtTemp = findViewById(R.id.txtTemperature);
        txtHumi = findViewById(R.id.txtHumidity);
        txtLi = findViewById(R.id.txtLight);
        LED = findViewById(R.id.led);
        PUMP = findViewById(R.id.pump);


        LED.setOnToggledListener(new OnToggledListener() {
            @Override
            public void onSwitched(ToggleableView toggleableView, boolean isOn) {
                if(isOn) {
                    sendataMQTT("Tuanhao911/feeds/nutnhan1", "1");
                } else {
                    sendataMQTT("Tuanhao911/feeds/nutnhan1","0");
                }
            }
        });

        PUMP.setOnToggledListener(new OnToggledListener() {
            @Override
            public void onSwitched(ToggleableView toggleableView, boolean isOn) {
                if(isOn) {
                    sendataMQTT("Tuanhao911/feeds/nutnhan2", "1");
                } else {
                    sendataMQTT("Tuanhao911/feeds/nutnhan2","0");
                }
            }

        });
        startMQTT();
    }
    public void sendataMQTT(String topic, String value) {
        MqttMessage msg = new MqttMessage();
        msg.setId(1234);
        msg.setQos(0);
        msg.setRetained(false);

        byte[] b = value.getBytes(Charset.forName("UTF-8"));
        msg.setPayload(b);

        try {
            mqttHelper.mqttAndroidClient.publish(topic, msg);
        }catch (MqttException e){
        }

    }

    public void startMQTT () {
        mqttHelper = new MQTTHelper(this);
        mqttHelper.setCallback(new MqttCallbackExtended() {
            @Override
            public void connectComplete(boolean reconnect, String serverURI) {

            }

            @Override
            public void connectionLost(Throwable cause) {

            }

            @Override
            public void messageArrived(String topic, MqttMessage message) throws Exception {
                Log.d("Test", topic + "===" + message.toString());
                if(topic.contains("cambien1")){
                    txtTemp.setText(message.toString() + " °C");
                } else if(topic.contains("cambien3")) {
                    txtHumi.setText(message.toString() + " %");
                } else if(topic.contains("cambien2")) {
                    txtLi.setText(message.toString() + " lux");
                } else if(topic.contains("nutnhan1")) {
                    if (message.toString().equals("1")) {
                        LED.setOn(true);
                    } else {
                        LED.setOn(false);
                    }
                }  else if(topic.contains("nutnhan2")) {
                    if (message.toString().equals("1")) {
                        PUMP.setOn(true);
                    } else {
                        PUMP.setOn(false);
                    }
                }

                }

            @Override
            public void deliveryComplete(IMqttDeliveryToken token) {

            }
        });
    }
}