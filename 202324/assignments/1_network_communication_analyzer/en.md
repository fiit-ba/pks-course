
# **Assignment 1: Network communication analyzer** ([SK](README.md))

## **Task assignment**

Design and implement Ethernet network analyzer for network communications recorded in .pcap file and provides the following information about the communications. A fully developed assignment fulfills the following tasks: 

1.  **A listing of all frames in hexadecimal form** sequentially as they were recorded in the file. .
 
    For each frame, output should state:

    > a) Sequence number of the frame in the parsed file. 
    >    
    > b) The length of the frame in bytes provided by the pcap API, as well as the length of this frame carried over the medium. (these values may not be the same)
    >    
    > c) Frame type - Ethernet II, IEEE 802.3 (IEEE 802.3 with LLC, IEEE 802.3 with LLC and SNAP, IEEE 802.3 - Raw).
    >    
    > d) For IEEE 802.3 with LLC, also indicate the Service Access Point (SAP), e.g. STP, CDP, IPX, SAP... 
    > 
    > e) For IEEE 802.3 with LLC and SNAP,  also indicate PID, e.g. AppleTalk, CDP, DTP ...
    >    
    > f) The source and destination physical (MAC) addresses of the nodes between which the frame was transmitted. 

    Other requirements:

    > g)  In the output, ***the frame 16 bytes per line.***. Each line is terminated by a newline character. For the clarity of the output, it is recommended to use a non-proportional (monospace) font.
    >
    > h)  The output must be in ***YAML***. You should use Ruamel for Python.
    >
    > i)  Submission to AIS by 2.10.2023 23:59
    >
    > j)  The solution to this task is to be ***presented in the 3th exercise***.

    Scoring: **2 points**

2.  **List of IP addresses and encapsulated protocol on layer 2-4** for Ethernet II frames.

    For each frame, add the following information to the output from Task 1:

    > a)  Encapsulated protocol in frame header. (ARP, IPv4, IPv6 .... ) 
    >
    > b)  Source and destination IP address of the packet. 
    >
    > c)  For IPv4, also specify the encapsulated protocol. (TCP, UDP...) 
    >
    > d)  For the 4th layer i.e., TCP and UDP, indicate the source and destination port of the communication and if one of the ports is among the "well-known ports", also Include the name of the application protocol. Note that the IP header can range in size from 20B to 60B.

    Other **mandatory** requirements:

    > e)  Protocol numbers within Ethernet II (Ethertype field), in IP packet (Protocol field) and port numbers for transport protocols must be ***read from one or more external text files*** (Task 2 points a, c, and d). Example of possible external file formatting is at the end of this document.
    >
    > f)  ***Output also names*** in addition to numbers for ***well-known protocols and ports*** (at minimum for the protocols listed in tasks 1) and 2). The program shall output name of encapsulated protocol previously unknown protocol after its name and protocol (or port) number are added to the external file. 
    >
    > g)  A library file used by the program is not considered an external file. 

    Scoring: **1 point**

3.  Provide the following statistics for IPv4 packets **at the end of output from task 2**:

    > a)  A list of IP addresses of all sending nodes and number of packets each sent.
    >
    > b)  The IP address of the node that sent (regardless of the recipient) the most packets, and number of packets. If there are more that sent the most, list them all.

    **Poznámka**

    - IP adresy a počet odoslaných / prijatých paketov sa musia zhodovať s IP adresami vo výpise Wireshark -\> Statistics -\> IPv4 Statistics -\> Source and Destination Addresses.

    Scoring: **1 point**

4.  Your program ***with communication analysis*** for selected protocols:

    #### Pre-preparation:

    > a)  Implement the ***-p*** (as protocol) CLI option, which will be followed by another argument, namely the abbreviation of the protocol taken from the external file, e.g. analyzer.py -p HTTP. If the option is followed by any argument or the specified argument is a non-existent protocol, the program will print an error message and return to the beginning. Alternatively, a menu can be implemented, but ***the output must be written to a YAML file***.
    >
    > b)  The output of each frame in the following filters must also meet the requirements set in Tasks 1 and 2 (L2 and L3 analysis).
    
    #### If the argument following "-p" option specifies connection-oriented protocol communication (i.e. encapsulated in TCP):

    > c)  List ***all complete communications*** with their order number. Complete communication must include establishment (SYN) and termination (FIN on both sides; or FIN and RST; or RST only) of the connection. There are two ways for opening and four ways for closing a complete communication. 
    >
    > d)  List ***the first incomplete*** communication that contains only the connection establishment or only termination.
    >
    > e)  Your analyzer must support the following connection-oriented protocols: **HTTP, HTTPS, TELNET, SSH, FTP radiation, FTP data.**

    **Notes**
    
    - By default, the connection is opened using a 3-way handshake , 3 messages are sent together, but it may happen that 4 messages are sent, for more information, see [page 3](http://www.tcpipguide.com/free/t_TCPConnectionEstablishmentProcessTheThreeWayHandsh-3.htm) and [page 4](http://www.tcpipguide.com/free/t_TCPConnectionEstablishmentProcessTheThreeWayHandsh-4.htm) in [TCP Connection Establishment Process: The \"Three-Way Handshake"](http://www.tcpipguide.com/free/t_TCPConnectionEstablishmentProcessTheThreeWayHandsh.htm).
    
    - The connection is closed using a 4-way handshake , but two situations can occur, see [page 2](http://www.tcpipguide.com/free/t_TCPConnectionTermination-2.htm) and [page 4](http://www.tcpipguide.com/free/t_TCPConnectionTermination-4.htm) in [TCP Connection Termination](http://www.tcpipguide.com/free/t_TCPConnectionTermination.htm)
    - The connection can also be terminated using a flag [RST](https://medium.com/liveonnetwork/tcp-fin-rst-7e4eefd963b7).

    - The packet that initiates the start of the connection termination process may have other flags set, such as ***PUSH***, in addition to the ***FIN*** flag.

    Scoring: **3 points**

    #### If the argument following "-p" option specifies connectionless protocol (over UDP):

    > f) For the ***FTP protocol list all frames and clearly list them in communications***,not only the first frame on UDP port 69, but identify all frames for each TFTP communication and clearly show which frames belong to which communication. We consider a complete TFTP communication to be one where the size of the last datagram with data is smaller than the agreed block size when the connection is established, and at the same time the sender of this packet receives an ACK from the other side. See chapters: [TFTP General](http://www.tcpipguide.com/free/t_TFTPGeneralOperationConnectionEstablishmentandClie.htm) and [TFTP Detailed Operation](http://www.tcpipguide.com/free/t_TFTPDetailedOperationandMessaging-3.htm).

    Scoring: **1.5 points**

    #### If the argument following "-p" option specifies ICMP protocol:
    
    > g) The program identifies all types of ICMP messages. Split the Echo request and Echo reply (including Time exceeded) into complete communications based on the following principle. First, you need to identify the source and destination IP pairs that exchanged ICMP messages and associate each pair with their ICMP messages. Echo request and Echo reply contain fields [Identifier a Sequence](http://www.tcpipguide.com/free/t_ICMPv4EchoRequestandEchoReplyMessages-2.htm) in the header. The ***Identifier*** field indicates the communication number within the IP address pair and the ***Sequence*** field indicates the sequence number within the communication. Both fields can be the same for different IP source and IP destination pairs. This implies that the new communication is identified by the IP address pair and the ICMP field ***Identifier***. All other ICMP message types and ICMP Echo request/reply messages without a pair will be output as incomplete communications.
    >
    > h) For each ICMP frame, also indicate the ICMP message type [Type field](https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml) in the ICMP header), e.g. Echo request, Echo reply, Time exceeded, etc. For complete communications, also list the ICMP fields ***Identifier*** and ***Sequence***.

    Scoring: **1.5 points**

    #### If the argument following "-p" option specifies ARP protocol:

    > i) List all ARP pairs (request – reply), also indicate the IP address for which the MAC address is being sought, for Reply indicate a specific pair - IP address and MAC address found. If multiple ARP-Request frames were sent to the same IP address, first identify all ARP pairs and list them in one complete communication, regardless of the source address of the ARP-Request. If there are ARP-Requests frames without ARP-Reply, list them all in one incomplete communication. Likewise, if it identifies more ARP reply than ARP request messages to the same IP, then list all ARP reply without ARP request in one incomplete communication. Ignore other types of ARP messages within the filter.

    Scoring: **1 point**

    #### If the IP packet is fragmented:
    > j) If the size of the IP packet exceeds the MTU, the packet is split into several smaller packets called fragments before being sent and then the whole message is reassembled after receiving all the fragments on the receiver's side. For [ICMP filter](#if-the-argument-following--p-option-specifies-icmp-protocol), identify all fragmented IP packets and list for each such packet all frames with its fragments in the correct order. For fragment merging, study the fields ***Identification***, ***Flags*** and ***Fragment Offset*** in the IP header and include them also for packets in such communication that contain fragmented packets as ***id, flags_mf and frag_offset***, more details [HERE](https://packetpushers.net/ip-fragmentation-in-detail/). The task is just an extension of the [ICMP filter](#if-the-argument-following--p-option-specifies-icmp-protocol) task, so the input argument for the protocol is same.

    Scoring: **1 point**
    
5. The solution must include ***documentation***:

    > a)  Clarity and comprehensibility of the submitted documentation are required in addition to the overall solution quality. Full marks are awarded only for documents that provide all the essentials about the functioning of their program. This includes the processing diagram *.pcap files and a description of individual parts of the source code (libraries, classes, methods, etc.).
    >
    > b)  Documentation shall ***comprise***:
            >- Title page,
            >- Diagram (activity, flowchart) of processing (concept) and operation of the program,
            >- The proposed mechanism for protocol analysis on individual layers,
            >- An example of the structure of external files for specifying protocols and ports,
            >- Annotated user interface,
            >- Chosen implementation environment,
            >- Evaluation and possible extensions.

    Scoring: **1.5 points**

## Minimum requirements for accepting a submitted assignment:

-   The program must be implemented in C/C++ or Python using the pcap or scapy library, be compilable and executable in classrooms. Use libpcap for linux /BSD and winpcap / npcap for Windows to open pcap files. Library can be named any, but it should provide the following accepted functions:
    -   opening and closing pcap file,
    -   loading a frame as byte array or hexdump,
    -   loading the next frame from pcap file,
    -   getting the length of the frame.
    
    No other library functionality is allowed and custom logic must be implemented to parse the frames.

-   The program can use frame length data from struct pcap_pkthdr and functions for working with pcap file and loading frames:

    -   *pcap\_createsrcstr()*

    -   *pcap\_open()*

    -   *pcap\_open\_offline()*

    -   *pcap\_close()*

    -   *pcap\_next\_ex()*

    -   *pcap\_loop()*

-   **The output** from each task **must be in a YAML** (.yaml) file and in a YAML-compatible format (help, you get schemas to test your output).

-   Use of programming language or library functions for automatic frame analysis is disallowed. ***The entire frame needs to be processed byte by byte (e.g., bytes from bytearray)***. For example, using libpcap functions to directly list the specific fields of the framework (e.g. ih->saddr) will result in a zero score for the whole assignment.

-   The program must be **organized so** that frame analysis functionality **is easily extensible during additional implementation** during exercise.

-   The sequence number of the frame in the program dump must match the frame number in the analyzed file (checked using Wireshark).

-   On **final submission**, each frame in all outputs must **meet** all **requirements in Tasks 1 and 2**. 

-   The student must be able to run the program in the room in which they have the exercises. In case of distance learning, the student must be able to present the program online according to the tutor's instructions, e.g. via Webex, Meet, etc.

-   At the first exercise after final submission in AIS, the student must implement additional functionality into their program according to the tutor's instructions. The additional implementation only extends the analyzer’s functionality, it shall not disable the already existing functionality of the program.

-   The student submits the documentation and source code of the implementation in electronic form to AIS by the specified date.

    - The overall evaluation will also take into account the efficiency of your program and the ease of interaction with it.
>
-   Points for documentation will be awarded only if a fully functional solution (fulfilled at least minimum requirements) is demonstrated on the first try, without the need to restart the program, make modifications to the code, etc...

-   The submitted final submission must **pass the plagiarism check** for a passing grade.

-   An assignment that **does not meet any of the minimum requirements** above or does not meet the minimum scores for the individual tasks of the assignment according to the  [scoring table](#scoring-table), will not be accepted and result in **0 points score**. 

## Submitting the final assignment to AIS:
-   Deadline: **16.10.2023 23:59**

-   One **.ZIP** file named \<ais\_login\>.zip is uploaded. zip e.g. xpacket.zip.

-   The ZIP file use the following structure:

    -   **Documentation,** directory, which contains the documentation in **PDF** format. 

    -   **Protocols** directory, which will contain your files with defined ports and protocol names. 

    -   Next, the ZIP file will contain only your code file and your own written libraries/modules. Do not pass standard libraries or those that can be installed via pip.

        -   For example, in python it will be the main.py file and your own written modules that you will import.

        -   For example, in C it will be main.c and your own included *.c* and *.h* files.

-   Example of the structure of the uploaded ZIP file:
    ```
    -   Documentation

        -   documentation.pdf

    -   Protocols

        -   l2.txt

        -   l3.txt

    -   main.py

    -   IcmpFilter.py

    -   tcpFilter.py
    ```

## Scoring table
<table>
<thead>
  <tr>
    <th>Task num.</th>
    <th>Task</th>
    <th>Max points</th>
    <th>Min points</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>1</td>
    <td>Print out all frames in hexadecimal form</td>
    <td >2</td>
    <td >1</td>
  </tr>
  <tr>
    <td>2</td>
    <td>L2-L4 protocols frame analysis</td>
    <td >1</td>
    <td  rowspan="7">5</td>
  </tr>
  <tr>
    <td>3</td>
    <td>IPv4 packets statistics</td>
    <td >1</td>
  </tr>
  <tr>
    <td>4 (c-e)</td>
    <td>Connection-oriented protocols analysis</td>
    <td >3</td>
  </tr>
  <tr>
    <td>4 (f)</td>
    <td>Connectionless protocols analysis</td>
    <td >1.5</td>
  </tr>
  <tr>
    <td>4 (g-h)</td>
    <td>ICMP analysis</td>
    <td >1.5</td>
  </tr>
  <tr>
    <td>4 (i)</td>
    <td>ARP analysis</td>
    <td >1</td>
  </tr>
  <tr>
    <td>4 (j)</td>
    <td>IP fragmentation</td>
    <td >1</td>
  </tr>
  <tr>
    <td>5</td>
    <td>Documentation</td>
    <td >1.5</td>
    <td >0.5</td>
  </tr>
  <tr>
    <td>6</td>
    <td>Efficiency</td>
    <td >0,5</td>
    <td >-</td>
  </tr>
    <tr>
    <td>7</td>
    <td>Additional implementation</td>
    <td >1</td>
    <td >0.5</td>
  </tr>
  <tr>
    <td></td>
    <td>Total:</td>
    <td >15</td>
    <td >7</td>
  </tr>
</tbody>
</table>

## **Example of possible formatting of external files**
```
#Ethertypes
0x0800 IPv4
0x0806 ARP
0x86dd IPv6
#LSAPs
0x42 STP
0xaa SNAP
0xe0 IPX
#IP Protocol numbers
0x01 1 ICMP
0x06 6 TCP
0x11 17 UDP
#TCP ports
0x0015 22 SSH
0x0050 80 HTTP
#UDP ports
0x0035 53 DNS
0x0045 69 TFTP
```

## **Solution output samples**

Solution output samples are included in [validator](/202324/assignments/1_network_communication_analyzer/validator_yaml_output/examples/) to verify the correct format of your output. The contents of the frames do not correspond to real communication. Similarly, the IP addresses listed in decimal-point notation do not correspond to the real values in the frame.
