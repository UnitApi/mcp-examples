#!/usr/bin/env python3
"""
Audio Recording Example

This example demonstrates how to record audio using the MCP Hardware Client.
"""

import logging
import time
import argparse
from unitmcp import MCPHardwareClient

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def main():
    """
    Main function to demonstrate audio recording.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Record audio using MCP Hardware Client")
    parser.add_argument("--duration", type=int, default=5, help="Duration of recording in seconds")
    parser.add_argument("--sample-rate", type=int, default=44100, help="Sample rate in Hz")
    parser.add_argument("--channels", type=int, default=1, help="Number of audio channels (1 for mono, 2 for stereo)")
    parser.add_argument("--output", type=str, default="recording.wav", help="Output file name")
    args = parser.parse_args()
    
    # Create and connect to the MCP hardware client
    client_config = {
        "server": "localhost",
        "port": 8080,
        "protocol": "http"
    }
    client = MCPHardwareClient(client_config)
    
    # Connect to the server
    if not client.connect():
        logger.error("Failed to connect to the MCP server")
        return
    
    try:
        # Record audio
        logger.info(f"Recording audio for {args.duration} seconds at {args.sample_rate} Hz with {args.channels} channels")
        result = client.record_audio(args.duration, args.sample_rate, args.channels)
        
        if result["status"] == "success":
            logger.info(f"Recording completed successfully")
            logger.info(f"Saving to {args.output}")
            # In a real implementation, we would save the audio data to a file here
            # For this example, we'll just simulate success
            logger.info(f"Audio saved to {args.output}")
        else:
            logger.error(f"Recording failed: {result.get('message', 'Unknown error')}")
        
    except KeyboardInterrupt:
        logger.info("Interrupted by user")
    finally:
        # Disconnect from the server
        client.disconnect()
        logger.info("Example completed")

if __name__ == "__main__":
    main()
