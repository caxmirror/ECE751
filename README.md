# LoRaFREE

This is repository of LoRaFREE, a new simulator tool that have been used in [1]. Please cite the paper if you consider using LoRaFREE in your research.

LoRaFREE is a more comprehensive Simpy simulator for LoRa than LoRaSim, which considers a packet error model, the imperfect orthogonality of spreading factors, the fading impact, and the duty cycle limitation at both, the devices and the gateway. LoRaFREE supports bidirectional communication by adding the downlink capability and the retransmission strategy in case of confirmable uplink transmissions. LoRaFree also extends the energy consumption profile from LoRaSim to consider the consumed energy at the reception time. In additions to that, we added an additional simulator for the synchronized transmissions schedule based on the work in [1].


[1] @ARTICLE{8884111,
  author={K. Q. {Abdelfadeel} and D. {Zorbas} and V. {Cionca} and D. {Pesch}},
  journal={IEEE Internet of Things Journal}, 
  title={ $FREE$ —Fine-Grained Scheduling for Reliable and Energy-Efficient Data Collection in LoRaWAN}, 
  year={2020},
  volume={7},
  number={1},
  pages={669-683},}

# Instruction
python3 FREEalpha=0.py 5 64 600 1 42

# output explanation:
1. `Nodes: 5` - The number of nodes in the simulation.
2. `DataSize [bytes] 64` - The size of data that each device sends in bytes.
3. `Full Collision: 600` - The average send time.
4. `Random Seed: 1` - The random seed used for the simulation.
5. `maxDist: 175.14838823607136` - The maximum distance between any two nodes.
6. The next few lines (`first node`, `node 0`, `node 1`, etc.) show the details of each node, including its ID, x and y coordinates, and distance from the gateway.
7. The `CHECK node X` lines are checking for collisions between the packets sent by different nodes. It checks for frequency and spreading factor (SF) collisions.
8. `Guards: [1, 1, 1, 1, 2, 3]` - The guard time for each node.
9. `energy (in J): 0.8652526080000003` - The total energy consumed by the nodes.
10. `sent packets: 8` - The total number of packets sent by the nodes.
11. `collisions: 0` - The total number of packet collisions.
12. `received packets: 8` - The total number of packets received by the gateway.
13. `processed packets: 8` - The total number of packets processed by the gateway.
14. `lost packets: 0` - The total number of packets lost during transmission.
15. `Bad CRC: 0` - The total number of packets with bad CRC.
16. `NoACK packets: 0` - The total number of packets that didn't receive an ACK.
17. `ACKLost packets: 0` - The total number of ACKs that were lost.
18. `DER: 1.0` - The Delivery Ratio, which is the ratio of the number of packets received to the number of packets sent.
19. `DER method 2: 1.0` - Another method of calculating the Delivery Ratio.
20. `SFdistribution: [1, 0, 1, 0, 3, 0]` - The distribution of Spreading Factors among the nodes.
21. `BWdistribution: [0, 0, 5]` - The distribution of Bandwidth among the nodes.
22. `CRdistribution: [5, 0, 0, 0]` - The distribution of Coding Rate among the nodes.
23. `TXdistribution: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5]` - The distribution of Transmission Power among the nodes.
24. `Slotsperframe: [98, 1, 100, 1, 100, 1]` - The number of slots per frame for each node.
25. `Slotlengths: [0.099344, 0.176208, 0.309456, 0.48379200000000006, 1.0290240000000002, 1.8922080000000001]` - The length of each slot.
26. `Framelengths: [0.198688, 0.176208, 0.618912, 0.48379200000000006, 4.116096000000001, 1.8922080000000001]` - The length of each frame.
27. `Collmap: [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]` - A map showing the collisions between different nodes.
28. `CollectionTime: 103.93142400000002` - The total time taken to collect all the packets.
29. `confirmabletdmaTX.dat` - The name of the file where the results of the simulation are saved.
30. The last line is a space-separated list of all the values calculated during the simulation, which is saved in the `confirmabletdmaTX.dat` file.
