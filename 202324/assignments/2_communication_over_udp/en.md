# **Assignment 2: Communication application using the UDP protocol**  ([SK](README.md))

## **Task Assignment**

Design and implement an application using a custom protocol over the User Datagram Protocol (UDP) of the transport layer of the TCP/IP network model. The application will enable communication between two participants in a local Ethernet network, i.e., the transfer of text messages and any file between computers (nodes).

The application consists of two parts: transmitting and receiving. The sending node sends the file to another node in the network. It is assumed that there is data loss in the network. If the sent file is larger than the user-defined maximum fragment size, the sending party breaks the file into smaller parts - fragments, which it sends separately. The user must be able to set the maximum fragment size so that they are not fragmented again on the lower layer.

If the file is sent as a sequence of fragments, the destination node reports information about the message and whether the message was transferred without errors. When the entire file is received on the destination node, it will display a message about its reception and the absolute path where the received file was saved. 

The application must include communication error checking and re-requesting of erroneous fragments, including both positive and negative acknowledgement. After starting the program, the communicator automatically sends a packet to maintain the connection every 5 seconds until the user ends the connection. We recommend solving via self-defined signalling messages and separate thread.

## The application must fulfil the following functions (minimum):

1. The application must be implemented in C/C++ or Python using libraries for working with UDP socket, compilable, and executable in classrooms. We recommend using the Python socket module, C/C++ libraries sys/socket.h for Linux/BSD and winsock2.h for Windows. Other libraries and functions to work with sockets must be approved by the trainee. Libraries for working with IP addresses and ports can also be used in the application: *arpa/inet.h* a *netinet/in.h*.
2. The application must work with data optimally (e.g., do not store IP addresses in 4x int).

3. When sending a file, it must allow the user to specify the destination IP and port.

4. The user (just on the transmitter side) must be able to choose the max fragment size and change it dynamically during the program run before sending message/file (no for keep-alive packets).

5. Both communicating parties must be able to display:
    >   a) the name and absolute path to the file on the given node,
    >
    >   b) the size and number of fragments, including the total size of the message/file.
    
6. Possibility of simulating a transmission error by sending at least 1 erroneous fragment during file transfer (an error is purposefully inserted into the data part of the fragment, that is, the receiving party detects an error during transmission).

7. The receiving party must be able to notify the sender of the correct and incorrect delivery of fragments. If a fragment is delivered incorrectly, the application will ask to re-send the damaged data. 

8. The possibility to send a 2MB file and in that case save them on the receiving side as the same file, while the user only enters the path to the directory where it should be saved. 

9. The application must be organized so that both communicating nodes can switch between transmitter and receiver functions without restarting the application (one side sends a switching message, receives an ACK from the other side, and the nodes automatically switch); the application does not have to (but can) be a transmitter and receiver at the same time.

## Submitted by: 

1. Proposal of a solution

2. Demonstration of the solution in accordance with the presented proposal 
   
When presenting the solution, the ability to implement a simple functionality in the exercise is a condition of the assessment.

## Scoring criteria:  

The whole solution - max. 20 points (min. 10), of which:
   - max. 4 points for the proposed solution; 

   - max. 1 point for added functionality (additional implementation) directly at the exercise in the required time according to the exercise schedule; If the student does not complete the task assigned directly in the exercises, the resulting solution will not be evaluated; 

   - max. 15 points for the resulting solution.  

The student submits the proposal and the source code of the implementation in electronic form to AIS until 4.12.2023 23:59.

## Scoring table
<table>
<thead>
  <tr>
    <th>Task num.</th>
    <th>Task name</th>
    <th>Max points</th>
    <th>Min points</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>1</td>
    <td><b>Design of the program and communication protocol</b>
    <td>4</td>
    <td>2</td>
  </td>
  </tr>
  <tr>
    <td>2</td>
    <td><b>Preparation</b>
    <td>0.5</td>
    <td  rowspan="7">7.5</td>
  </td>
  </tr>
  <tr>
    <td>3</td>
    <td><b>IP and port settings</b>
    <td>0.5</td>
  </td>
  </tr>
  <tr>
    <td>4</td>
    <td><b>Transferring a file smaller than the set fragment size</b>
    <td>2</td>
  </td>
  </tr>
  <tr>
  <td>5</td>
    <td><b>Simulating a File Transfer Error</b>
    <td>4</td>
  </td>
  </tr>
  <tr>
  <td>6</td>
    <td><b>Transferring a 2MB file</b>
    <td>2</td> 
  </td>
  </tr>
  <tr>
  <td>7</td>
    <td><b>Keep alive</b>
    <td>3</td>
  </td>
  </tr>
  <tr>
  <td>8</td>
    <td><b>Final documentation and overall quality</b>
    <td>3</td> 
  </td>
  </tr>
  <tr>
    <td>9</td>
    <td><b>Added functionality (additional implementation) directly in the exercise</b>
    <td>1</td>
    <td>0.5</td>
  </td>
  </tr>
    <tr>
    <td></td>
    <td><b>Total</b>
    <td>20</td>
    <td>10</td>
  </td>
  </tr>
</tbody>
</table>

### Description of the tasks in the scoring table
A student should be able to filter application segments using the tool Wireshark and determine the type of messages of the designed protocol when demonstrating their application to the trainer.

#### Task 1 - Design of the program and communication protocol
The clarity and comprehensibility of the submitted documentation, as well as the quality of the proposed solution are evaluated. A student gains 5 points if he writes all the essential info about the program functioning: correctly designed structure. A student gains 5 points if the documentation contains all essential information about the functioning of his program. <ins>Correctly designed structure of the header of the own protocol</ins>, description of the used checksum method and ARQ operation, <ins>methods for maintaining the connection, diagram (Sequence diagram) of communication processing on both nodes</ins>, description of individual parts of the source code (libraries, classes, methods, etc.). Underlined requirements are minimal.

#### Task 2 - Preparation
Set up and verify connectivity between the 2 nodes, run Wireshark on both nodes.
Start the capture in Wireshark and set the filter to display only the communication of your own program. Every transmission is also checked through Wireshark.

#### Task 3 - IP and port settings
A student gains points if the receiving node allows setting the port on which the application listens and the IP address and port of the receiver on the transmitting node.

#### Task 4 - Transferring a file smaller than the set fragment size
A student gains points if the application allows one to successfully transfer a file smaller than the set fragment size according to the trainer's instructions.

#### Task 5 - Simulating a File Transfer Error
A student gains point if the application allows a message/file to be successfully transferred while simulating a transfer error and has a correctly implemented error detection and ARQ method. By the correct usage of a more complex ARQ method, it is possible to obtain another 3 points. Examples of ARQ methods are in Literature section below. Your suggestions for improvement are discouraged. Individual methods are rated as follows:
   - Stop & wait + 0b (including one ACK for a group of segments)
   - Go Back-N + 1b
   - Selective Repeat + 2b
   - Enhanced Go Back-N/Selective Repeat + 3b (dynamic sliding window, optimizing the number of ACK messages, .... )

#### Task 6 - Transferring a 2MB file
A student gains points if the application successfully transfers a file with a size of 2MB when setting the fragment size according to the trainer's instructions and saving it as the same file, showing the absolute path to the file and the number of fragments along with their size.

#### Task 7 - Keep alive
A student gains 2 points if the application maintains the connection after transferring the file using its own signaling messages and displays information if the connection was interrupted. By correctly using a more complex method to maintain the connection, it is possible to obtain another 1 point. 

#### Task 8 - Final documentation and ovarall quality
The clarity and comprehensibility of the submitted documentation, as well as the quality of the overall solution are evaluated. A student gains 3 points if the documentation contains all essential information about the functioning of his program, including the changes that occurred in the implementation compared to the proposal. The documentation must also include at least 1 sample test scenario (ideally as screenshots from Wireshark).

#### Task 9 - Added functionality (additional implementation) directly in the exercise
A student gains point if he implements the task in its full scope and demonstrates its functionality without the application crashing or throwing any error messages related to this task.

## Literature
1) Stop & Wait - [Sliding Window Protocol](https://www.youtube.com/watch?v=LnbvhoxHn8M&ab_channel=NesoAcademy)
2) [Selective repeat](https://www.youtube.com/watch?v=WfIhQ3o2xow&t=5s&ab_channel=NesoAcademy)
3) [Go Back-N](https://www.youtube.com/watch?v=QD3oCelHJ20&ab_channel=NesoAcademy)
