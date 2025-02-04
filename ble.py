import bluetooth
import struct
import time

NODE_NAME = "BLE_Mesh_Node"
MESH_NETWORK_KEY = b"your_network_key_here"

class BLEMeshNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.mesh_network = {} 
        self.bluetooth = bluetooth.Bluetooth()
        self.bluetooth.active(True)
        self.advertise()
    
    def advertise(self):
        adv_data = struct.pack("B", self.node_id)
        self.bluetooth.gap_advertise(100, adv_data)
        print(f"Node {self.node_id} advertising...")

    def scan_for_nodes(self):
        self.bluetooth.gap_scan(2000)
        devices = self.bluetooth.gap_scan_results()
        for device in devices:
            node_id = struct.unpack("B", device[1])[0]
            if node_id not in self.mesh_network:
                self.mesh_network[node_id] = device[0]
                print(f"Discovered node {node_id}")

    def send_message(self, target_node, message):
        if target_node in self.mesh_network:
            encrypted_message = self.encrypt_message(message)
            self.bluetooth.gap_send(target_node, encrypted_message)
            print(f"Message sent to Node {target_node}")
    
    def encrypt_message(self, message):
        return bytes([b ^ MESH_NETWORK_KEY[i % len(MESH_NETWORK_KEY)] for i, b in enumerate(message.encode())])


node = BLEMeshNode(node_id=1)
time.sleep(5)
node.scan_for_nodes()
time.sleep(5)
node.send_message(2, "Hello, Node 2!")
