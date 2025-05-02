"""
MQTT Bridge Example

This example demonstrates how to use the MQTT bridge for MCP Hardware Access.
"""

import json
import logging
import time
from typing import Dict, Any

import paho.mqtt.client as mqtt

from unitmcp.bridges import MQTTBridge

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def on_connect(client, userdata, flags, rc):
    """
    Callback for when the client connects to the broker.
    """
    if rc == 0:
        logger.info("Connected to MQTT broker")
        # Subscribe to response topics
        client.subscribe("mcp/gpio/setup/+/response")
        client.subscribe("mcp/gpio/control/+/+/response")
        client.subscribe("mcp/gpio/read/+/response")
        client.subscribe("mcp/gpio/write/+/response")
    else:
        logger.error(f"Failed to connect to MQTT broker with code {rc}")

def on_message(client, userdata, msg):
    """
    Callback for when a message is received from the broker.
    """
    logger.info(f"Received message on topic {msg.topic}: {msg.payload.decode()}")

def main():
    """
    Main function to demonstrate the MQTT bridge.
    """
    # Create and start the MQTT bridge
    bridge_config = {
        "broker": "localhost",
        "port": 1883,
        "client_id": "mcp_mqtt_bridge_example",
        "topic_prefix": "mcp",
        "qos": 1,
    }
    bridge = MQTTBridge(bridge_config)
    
    # Register a device
    bridge.register_device("led1", {
        "type": "led",
        "pin": 17,
        "active_high": True
    })
    
    # Start the bridge
    bridge.start()
    
    # Create a client to interact with the bridge
    client = mqtt.Client(client_id="mcp_mqtt_client_example")
    client.on_connect = on_connect
    client.on_message = on_message
    
    try:
        # Connect to the broker
        client.connect("localhost", 1883, 60)
        client.loop_start()
        
        # Wait for the connection to be established
        time.sleep(1)
        
        # Example 1: Set up a GPIO pin
        setup_payload = {
            "mode": "output",
            "pull_up_down": "up"
        }
        logger.info("Setting up GPIO pin 17")
        client.publish("mcp/gpio/setup/17", json.dumps(setup_payload), qos=1)
        
        # Wait for the response
        time.sleep(1)
        
        # Example 2: Control an LED
        control_payload = {
            "params": {
                "brightness": 100
            }
        }
        logger.info("Turning on LED1")
        client.publish("mcp/gpio/control/led1/on", json.dumps(control_payload), qos=1)
        
        # Wait for the response
        time.sleep(1)
        
        # Example 3: Read a GPIO pin
        logger.info("Reading GPIO pin 17")
        client.publish("mcp/gpio/read/17", json.dumps({}), qos=1)
        
        # Wait for the response
        time.sleep(1)
        
        # Example 4: Write to a GPIO pin
        write_payload = {
            "value": 1
        }
        logger.info("Writing to GPIO pin 17")
        client.publish("mcp/gpio/write/17", json.dumps(write_payload), qos=1)
        
        # Wait for the response
        time.sleep(1)
        
        # Example 5: Turn off the LED
        logger.info("Turning off LED1")
        client.publish("mcp/gpio/control/led1/off", json.dumps({}), qos=1)
        
        # Wait for the response
        time.sleep(1)
        
    except KeyboardInterrupt:
        logger.info("Interrupted by user")
    finally:
        # Clean up
        client.loop_stop()
        client.disconnect()
        bridge.stop()
        logger.info("Example completed")

if __name__ == "__main__":
    main()
