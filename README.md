Bluetooth Low Energy (BLE) Mesh Network for IoT

Overview

This project implements a BLE Mesh Network for IoT devices, allowing multiple nodes to communicate efficiently. It includes features such as power optimization and security mechanisms.

Features

BLE Mesh topology setup with node discovery

Encrypted message transmission

Power-optimized device communication

Secure key-based message encryption

Requirements

Python 3.x

MicroPython with Bluetooth support (e.g., ESP32, Nordic nRF52)

Installation & Usage

Step 1: Setup Hardware

Flash MicroPython firmware onto your IoT device (ESP32/nRF52).

Install the required libraries for Bluetooth communication.

Step 2: Clone the Repository

$ git clone https://github.com/yourusername/BLE-Mesh-IoT.git
$ cd BLE-Mesh-IoT

Step 3: Upload Code to IoT Device

Use rshell or mpy-cross to upload the script to your MicroPython board:

$ rshell
> cp ble_mesh_iot.py /pyboard/

Step 4: Run the Code

Connect to your IoT device and execute the script:

$ python ble_mesh_iot.py

Contributing

Contributions are welcome! Feel free to submit pull requests or report issues.

License

This project is licensed under the MIT License.

