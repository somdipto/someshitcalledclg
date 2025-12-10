Here is the compiled content for your lab manual, covering Experiments 1 through 10. You can copy and paste this directly into your document editor..

-----

# Computer Networks Lab Manual (Experiments 1-10)

## Experiment 1: Point-to-Point Network Analysis

**Problem Statement:** Implement three nodes point-to-point network with duplex links between them. [cite\_start]Set the queue size, vary the bandwidth, and find the number of packets dropped[cite: 3, 4].

**TCL Script (`cn1.tcl`)**

```tcl
set ns [new Simulator]
set nf [open cn1.nam w]
$ns namtrace-all $nf
set tf [open cn1.tr w]
$ns trace-all $tf

proc finish {} {
    global ns nf tf
    $ns flush-trace
    close $nf
    close $tf
    exec nam cn1.nam &
    exit 0
}

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]

$ns duplex-link $n0 $n1 200Mb 10ms DropTail
$ns duplex-link $n1 $n2 1Mb 1000ms DropTail
$ns queue-limit $n0 $n1 10

set udp0 [new Agent/UDP]
$ns attach-agent $n0 $udp0
set cbr0 [new Application/Traffic/CBR]
$cbr0 set packetSize_ 500
$cbr0 set interval_ 0.005
$cbr0 attach-agent $udp0

set null0 [new Agent/Null]
$ns attach-agent $n2 $null0
$ns connect $udp0 $null0

$ns at 0.1 "$cbr0 start"
$ns at 1.0 "finish"
$ns run
```

[cite\_start][cite: 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114]

**AWK Script (`cn1.awk`)**

```awk
BEGIN { c=0; }
{
    if ($1 == "d") {
        c++;
        printf("%s\t%s\n", $5, $11);
    }
}
END { printf("The number of packets dropped is %d\n", c); }
```

[cite\_start][cite: 119, 120, 121, 122, 123, 124, 130]

-----

## Experiment 2: Ping Messages & Congestion

[cite\_start]**Problem Statement:** Implement transmission of ping messages/trace route over a network topology consisting of 6 nodes and find the number of packets dropped due to congestion[cite: 164].

**TCL Script (`cn2.tcl`)**

```tcl
set ns [new Simulator]
set nf [open lab2.nam w]
$ns namtrace-all $nf
set tf [open lab2.tr w]
$ns trace-all $tf

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]

$ns duplex-link $n0 $n4 100Mb 1ms DropTail
$ns duplex-link $n1 $n4 50Mb 1ms DropTail
$ns duplex-link $n2 $n4 200Mb 1ms DropTail
$ns duplex-link $n3 $n4 200Mb 1ms DropTail
$ns duplex-link $n4 $n5 1Mb 1ms DropTail

set p1 [new Agent/Ping]
$ns attach-agent $n0 $p1
$p1 set packetSize_ 50000
$p1 set interval_ 0.0001

set p2 [new Agent/Ping]
$ns attach-agent $n1 $p2
set p3 [new Agent/Ping]
$ns attach-agent $n2 $p3
$p3 set packetSize_ 30000
$p3 set interval_ 0.00001

set p4 [new Agent/Ping]
$ns attach-agent $n3 $p4
set p5 [new Agent/Ping]
$ns attach-agent $n5 $p5

$ns queue-limit $n0 $n4 5
$ns queue-limit $n2 $n4 3
$ns queue-limit $n4 $n5 2

Agent/Ping instproc recv {from rtt} {
    $self instvar node_
    puts "node [$node_ id] received answer from $from with round trip time $rtt msec"
}

$ns connect $p1 $p5
$ns connect $p3 $p4

proc finish {} {
    global ns nf tf
    $ns flush-trace
    close $nf
    close $tf
    exec nam lab2.nam &
    exit 0
}

$ns at 0.1 "$p1 send"
$ns at 0.2 "$p1 send"
$ns at 0.3 "$p1 send"
$ns at 0.4 "$p1 send"
$ns at 0.5 "$p1 send"
$ns at 0.6 "$p1 send"
$ns at 0.7 "$p1 send"
$ns at 0.8 "$p1 send"
$ns at 0.9 "$p1 send"
$ns at 1.0 "$p1 send"
$ns at 0.1 "$p3 send"
$ns at 0.2 "$p3 send"
$ns at 0.3 "$p3 send"
$ns at 0.4 "$p3 send"
$ns at 0.5 "$p3 send"
$ns at 0.6 "$p3 send"
$ns at 0.7 "$p3 send"
$ns at 0.8 "$p3 send"
$ns at 0.9 "$p3 send"
$ns at 1.0 "$p3 send"
$ns at 2.0 "finish"
$ns run
```

[cite\_start][cite: 262, 263, 264, 265, 266, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339]

**AWK Script (`cn2.awk`)**

```awk
BEGIN { drop=0; }
{
    if ($1 == "d") {
        drop++;
    }
}
END {
    printf("Total number of %s packets dropped due to congestion = %d\n", $5, drop);
}
```

[cite\_start][cite: 345, 346, 347, 349, 350, 351, 352, 353, 354, 355]

-----

## Experiment 3: Ethernet LAN & Congestion Window

[cite\_start]**Problem Statement:** Implement an Ethernet LAN using n nodes and set multiple traffic nodes and plot congestion window for different source / destination[cite: 1364].

**TCL Script (`cn3.tcl`)**

```tcl
set ns [new Simulator]
set tf [open lab3.tr w]
$ns trace-all $tf
set nf [open lab3.nam w]
$ns namtrace-all $nf

set n0 [$ns node]
$n0 color "magenta"
$n0 label "src1"
set n1 [$ns node]
set n2 [$ns node]
$n2 color "magenta"
$n2 label "src2"
set n3 [$ns node]
$n3 color "blue"
$n3 label "dest2"
set n4 [$ns node]
set n5 [$ns node]
$n5 color "blue"
$n5 label "dest1"

$ns make-lan "$n0 $n1 $n2 $n3 $n4" 100Mb 100ms LL Queue/DropTail Mac/802_3
$ns duplex-link $n4 $n5 1Mb 1ms DropTail

set tcp0 [new Agent/TCP]
$ns attach-agent $n0 $tcp0
set ftp0 [new Application/FTP]
$ftp0 attach-agent $tcp0
$ftp0 set packetSize_ 500
$ftp0 set interval_ 0.0001

set sink5 [new Agent/TCPSink]
$ns attach-agent $n5 $sink5
$ns connect $tcp0 $sink5

set tcp2 [new Agent/TCP]
$ns attach-agent $n2 $tcp2
set ftp2 [new Application/FTP]
$ftp2 attach-agent $tcp2
$ftp2 set packetSize_ 600
$ftp2 set interval_ 0.001

set sink3 [new Agent/TCPSink]
$ns attach-agent $n3 $sink3
$ns connect $tcp2 $sink3

set file1 [open file1.tr w]
$tcp0 attach $file1
set file2 [open file2.tr w]
$tcp2 attach $file2
$tcp0 trace cwnd_
$tcp2 trace cwnd_

proc finish {} {
    global ns nf tf
    $ns flush-trace
    close $tf
    close $nf
    exec nam lab3.nam &
    exit 0
}

$ns at 0.1 "$ftp0 start"
$ns at 5 "$ftp0 stop"
$ns at 7 "$ftp0 start"
$ns at 0.2 "$ftp2 start"
$ns at 8 "$ftp2 stop"
$ns at 14 "$ftp0 stop"
$ns at 10 "$ftp2 start"
$ns at 15 "$ftp2 stop"
$ns at 16 "finish"
$ns run
```

[cite\_start][cite: 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1399, 1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426]

**AWK Script (`cn3.awk`)**

```awk
BEGIN { drop=0; }
{
    if ($1 == "d") {
        drop++;
    }
}
END {
    printf("Total number of %s packets dropped due to congestion = %d\n", $5, drop);
}
```

[cite\_start][cite: 1430, 1431, 1435, 1436, 1439, 1440]

-----

## Experiment 4: CRC Error Detection (16-bit)

[cite\_start]**Problem Statement:** Develop a program for error detecting code using CRC-CCITT (16-bits)[cite: 1493].

**Java Code (`CRC.java`)**

```java
import java.util.Scanner;

class CRC {
    static String xor(String a, String b) {
        StringBuilder stringBuilder = new StringBuilder();
        int len = Math.min(a.length(), b.length());
        for (int i = 0; i < len; i++) {
            if (a.charAt(i) == b.charAt(i)) {
                stringBuilder.append('0');
            } else {
                stringBuilder.append('1');
            }
        }
        return stringBuilder.toString();
    }

    static String divide(String dividend, String divisor) {
        int divisorLength = divisor.length();
        int dividendLength = dividend.length();
        while (dividendLength >= divisorLength) {
            String temp;
            if (dividend.charAt(0) == '1')
                temp = xor(divisor, dividend.substring(0, divisorLength));
            else
                temp = dividend.substring(0, divisorLength);
            dividend = temp.substring(1) + dividend.substring(divisorLength);
            dividendLength -= 1;
        }
        return dividend;
    }

    static String generateCodeWord(String message, String generator) {
        int msgLength = message.length();
        int gtrLength = generator.length();
        String dividend = String.format("%-" + (msgLength + gtrLength - 1) + "s", message).replace(' ', '0');
        String remainder = divide(dividend, generator);
        return message + remainder;
    }

    static boolean checkCodeWord(String codeword, String generator) {
        String temp = divide(codeword, generator);
        int len = temp.length();
        for (int i = 0; i < len; i++) {
            if (temp.charAt(i) == '1') {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter Generator String");
        String generator = scanner.next();
        while (true) {
            System.out.println("\nMenu");
            System.out.println("1. Generate Code Word");
            System.out.println("2. Check Code Word");
            System.out.println("3. Exit");
            int choice = scanner.nextInt();
            switch (choice) {
                case 1:
                    System.out.println("Enter Message");
                    String message = scanner.next();
                    String result = generateCodeWord(message, generator);
                    System.out.println("CodeWord: " + result);
                    break;
                case 2:
                    System.out.println("Enter Code Word");
                    String codeWord = scanner.next();
                    if (checkCodeWord(codeWord, generator)) {
                        System.out.println("Code Word is Valid");
                    } else {
                        System.out.println("Code Word is Invalid");
                    }
                    break;
                case 3:
                    System.exit(0);
            }
        }
    }
}
```

[cite\_start][cite: 1573, 1574, 1575, 1576, 1577, 1578, 1579, 1580, 1582, 1583, 1587, 1589, 1590, 1591, 1592, 1595, 1596, 1597, 1598, 1599, 1600, 1601, 1603, 1604, 1607, 1608, 1609, 1611, 1612, 1613, 1614, 1615, 1616, 1619, 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1642, 1644, 1645, 1646, 1647, 1648, 1649, 1650]

-----

## Experiment 5: Sliding Window Protocol

[cite\_start]**Problem Statement:** Develop a program to implement a sliding window protocol in the data link layer[cite: 385].

**Sender Code (`slidsender.java`)**

```java
import java.net.*;
import java.io.*;
import java.rmi.*;

public class slidsender {
    public static void main(String a[]) throws Exception {
        ServerSocket ser = new ServerSocket(10);
        Socket s = ser.accept();
        DataInputStream in = new DataInputStream(System.in);
        DataInputStream in1 = new DataInputStream(s.getInputStream());
        String sbuff[] = new String[8];
        PrintStream p;
        int sptr = 0, sws = 8, nf, ano, i;
        String ch;
        do {
            p = new PrintStream(s.getOutputStream());
            System.out.print("Enter the no. of frames: ");
            nf = Integer.parseInt(in.readLine());
            p.println(nf);
            if (nf <= sws - 1) {
                System.out.println("Enter " + nf + " Messages to be send\n");
                for (i = 1; i <= nf; i++) {
                    sbuff[sptr] = in.readLine();
                    p.println(sbuff[sptr]);
                    sptr = ++sptr % 8;
                }
                sws -= nf;
                System.out.print("Acknowledgment received");
                ano = Integer.parseInt(in1.readLine());
                System.out.println(" for " + ano + " frames");
                sws += nf;
            } else {
                System.out.println("The no. of frames exceeds window size");
                break;
            }
            System.out.print("\nDo you wants to send some more frames: ");
            ch = in.readLine();
            p.println(ch);
        } while (ch.equals("yes"));
        s.close();
    }
}
```

[cite\_start][cite: 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 435, 436, 437, 438, 439, 440, 442, 443, 444, 445, 447, 448, 449, 450, 452, 453, 454, 456, 457, 459, 460, 461]

**Receiver Code (`slidreceiver.java`)**

```java
import java.net.*;
import java.io.*;

class slidreceiver {
    public static void main(String a[]) throws Exception {
        Socket s = new Socket(InetAddress.getLocalHost(), 10);
        DataInputStream in = new DataInputStream(s.getInputStream());
        PrintStream p = new PrintStream(s.getOutputStream());
        int i = 0, rptr = -1, nf, rws = 8;
        String rbuf[] = new String[8];
        String ch;
        System.out.println();
        do {
            nf = Integer.parseInt(in.readLine());
            if (nf <= rws - 1) {
                for (i = 1; i <= nf; i++) {
                    rptr = ++rptr % 8;
                    rbuf[rptr] = in.readLine();
                    System.out.println("The received Frame " + rptr + " is: " + rbuf[rptr]);
                }
                rws -= nf;
                System.out.println("\nAcknowledgment sent\n");
                p.println(rptr + 1);
                rws += nf;
            } else
                break;
            ch = in.readLine();
        } while (ch.equals("yes"));
    }
}
```

[cite\_start][cite: 464, 465, 466, 468, 470, 471, 472, 473, 474, 475, 476, 477, 479, 480, 481, 482, 483, 485, 486, 487, 488, 489, 490, 493, 494, 495]

-----

## Experiment 6: Bellman-Ford Algorithm

[cite\_start]**Problem Statement:** Develop a program to find the shortest path between vertices using the Bellman-Ford and path vector routing algorithm[cite: 522].

**Java Code (`BellmanFord.java`)**

```java
import java.util.Scanner;

class BellmanFord {
    static int n, dest;
    static double[] prevDistanceVector, distanceVector;
    static double[][] adjacencyMatrix;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter number of nodes");
        n = scanner.nextInt();
        adjacencyMatrix = new double[n][n];
        System.out.println("Enter Adjacency Matrix (Use 'Infinity' for No Link)");
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                adjacencyMatrix[i][j] = scanner.nextDouble();
        System.out.println("Enter destination vertex");
        dest = scanner.nextInt();
        distanceVector = new double[n];
        for (int i = 0; i < n; i++)
            distanceVector[i] = Double.POSITIVE_INFINITY;
        distanceVector[dest - 1] = 0;
        bellmanFordAlgorithm();
        System.out.println("Distance Vector");
        for (int i = 0; i < n; i++) {
            if (i == dest - 1) {
                continue;
            }
            System.out.println("Distance from " + (i + 1) + " is " + distanceVector[i]);
        }
        System.out.println();
    }

    static void bellmanFordAlgorithm() {
        for (int i = 0; i < n - 1; i++) {
            prevDistanceVector = distanceVector.clone();
            for (int j = 0; j < n; j++) {
                double min = Double.POSITIVE_INFINITY;
                for (int k = 0; k < n; k++) {
                    if (min > adjacencyMatrix[j][k] + prevDistanceVector[k]) {
                        min = adjacencyMatrix[j][k] + prevDistanceVector[k];
                    }
                }
                distanceVector[j] = min;
            }
        }
    }
}
```

[cite\_start][cite: 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 572, 573, 574, 575, 576, 578, 579, 580, 581, 582, 583, 584, 585, 586, 588, 593, 594, 595, 596, 597, 598, 599, 600, 602, 605, 609]

-----

## Experiment 7: TCP Client-Server

[cite\_start]**Problem Statement:** Using TCP/IP sockets, write a client-server program to make the client send the file name and to make the server send back the contents of the requested file if present[cite: 1084].

**Client Code (`TCPClient.java`)**

```java
import java.net.*;
import java.io.*;

public class TCPClient {
    public static void main(String args[]) throws Exception {
        Socket sock = new Socket("127.0.0.1", 4000);
        System.out.print("Enter the file name\n");
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String fname = br.readLine();
        OutputStream os = sock.getOutputStream();
        PrintWriter pw = new PrintWriter(os, true);
        pw.println(fname);
        InputStream is = sock.getInputStream();
        BufferedReader socketRead = new BufferedReader(new InputStreamReader(is));
        String str;
        while ((str = socketRead.readLine()) != null) {
            System.out.println(str);
        }
        pw.close();
        socketRead.close();
        br.close();
        sock.close();
    }
}
```

[cite\_start][cite: 1133, 1134, 1135, 1137, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1151, 1153, 1154, 1155, 1156, 1158]

**Server Code (`TCPServer.java`)**

```java
import java.net.ServerSocket;
import java.net.Socket;
import java.io.*;

public class TCPServer {
    public static void main(String args[]) throws Exception {
        ServerSocket sersock = new ServerSocket(4000);
        System.out.println("SERVER ready for connection");
        Socket sock = sersock.accept();
        System.out.println("Connection succesful! waiting for file name");
        InputStream is = sock.getInputStream();
        BufferedReader br = new BufferedReader(new InputStreamReader(is));
        String fname = br.readLine();
        BufferedReader contentRead = new BufferedReader(new FileReader(fname));
        OutputStream os = sock.getOutputStream();
        PrintWriter pw = new PrintWriter(os, true);
        String str;
        while ((str = contentRead.readLine()) != null) {
            pw.println(str);
        }
        System.out.println("File contents sent successfully!");
        sersock.close();
        pw.close();
        contentRead.close();
        br.close();
        sock.close();
    }
}
```

[cite\_start][cite: 1160, 1161, 1162, 1163, 1165, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1178, 1180, 1182, 1183, 1184, 1185, 1186, 1187, 1189]

-----

## Experiment 8: UDP Client-Server

[cite\_start]**Problem Statement:** Develop a program on a datagram socket for client/server to display the messages on client side, typed at the server side[cite: 1230].

**Client Code (`UDPC.java`)**

```java
import java.io.*;
import java.net.*;

public class UDPC {
    public static void main(String[] args) throws Exception {
        BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
        DatagramSocket clientSocket = new DatagramSocket();
        InetAddress IPAddress = InetAddress.getByName("localhost");
        byte[] sendData = new byte[1024];
        byte[] receiveData = new byte[1024];
        System.out.println("Enter \"start\" to connect to server");
        String sentence = inFromUser.readLine();
        sendData = sentence.getBytes();
        DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, IPAddress, 9876);
        clientSocket.send(sendPacket);
        DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length, IPAddress, 9876);
        clientSocket.receive(receivePacket);
        String modifiedSentence = new String(receivePacket.getData());
        System.out.println("Message received from SERVER: " + modifiedSentence);
        clientSocket.close();
    }
}
```

[cite\_start][cite: 1271, 1272, 1273, 1275, 1277, 1278, 1279, 1280, 1281, 1282, 1283, 1284, 1285, 1286, 1288, 1289, 1290, 1291, 1293]

**Server Code (`UDPS.java`)**

```java
import java.io.*;
import java.net.*;
import java.util.Scanner;

public class UDPS {
    public static void main(String[] args) throws Exception {
        DatagramSocket serverSocket = new DatagramSocket(9876);
        System.out.println("SERVER started on port number 9876");
        byte[] sendData = new byte[1024];
        byte[] receiveData = new byte[1024];
        while (true) {
            DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
            serverSocket.receive(receivePacket);
            receivePacket.getData();
            InetAddress IPAddress = receivePacket.getAddress();
            int port = receivePacket.getPort();
            System.out.println("CLIENT connected");
            Scanner input = new Scanner(System.in);
            System.out.println("Enter the message to be sent");
            String message = input.nextLine();
            sendData = message.getBytes();
            DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, IPAddress, port);
            serverSocket.send(sendPacket);
            System.exit(0);
        }
    }
}
```

[cite\_start][cite: 1295, 1296, 1297, 1298, 1300, 1301, 1302, 1303, 1304, 1305, 1307, 1308, 1309, 1310, 1311, 1312, 1313, 1314, 1315, 1316, 1317, 1318, 1321]

-----

## Experiment 9: RSA Algorithm

[cite\_start]**Problem Statement:** Develop a program for a simple RSA algorithm to encrypt and decrypt the data[cite: 651, 652].

**Java Code (`rsa.java`)**

```java
import java.math.BigInteger;
import java.io.*;

public class rsa {
    BigInteger p, q, d, e, n, z, m, c;
    BufferedReader keyin = new BufferedReader(new InputStreamReader(System.in));
    String msg, rmsg, code;
    int size;

    void read() throws IOException {
        System.out.println("Enter the large prime numbers(p and q: such that p*q>127):");
        p = new BigInteger(keyin.readLine());
        q = new BigInteger(keyin.readLine());
        System.out.println("Enter the public exponent ");
        e = new BigInteger(keyin.readLine());
        n = p.multiply(q);
        z = (p.subtract(BigInteger.ONE)).multiply(q.subtract(BigInteger.ONE));
        d = new BigInteger("0");
        while (z.gcd(e).compareTo(BigInteger.ONE) != 0) {
            e = e.add(BigInteger.TWO);
        }
        d = e.modInverse(z);
        System.out.println("Enter the message to encrypt");
        msg = keyin.readLine();
        size = msg.length();
        code = "";
        rmsg = "";
    }

    void encrypt() {
        for (int i = 0; i < size; i++) {
            m = BigInteger.valueOf((int) msg.charAt(i));
            c = m.modPow(e, n);
            code += (char) c.intValue();
        }
    }

    void decrypt() {
        for (int i = 0; i < size; i++) {
            c = BigInteger.valueOf((int) code.charAt(i));
            m = c.modPow(d, n);
            rmsg += (char) m.intValue();
        }
    }

    void show() {
        System.out.println("\nThe message entered at sender's end is\"" + msg + "\"");
        System.out.println("\nThe encrypted message sent to the receiver is\"" + code + "\"");
        System.out.println("\nThe decrypted message at receiver's end is\"" + rmsg + "\"");
    }

    public static void main(String args[]) throws IOException {
        rsa r = new rsa();
        r.read();
        r.encrypt();
        r.decrypt();
        r.show();
    }
}
```

[cite\_start][cite: 766, 767, 768, 770, 772, 773, 775, 777, 778, 779, 780, 781, 782, 783, 784, 785, 787, 789, 791, 802, 803, 804, 805, 806, 807, 809, 813, 814, 815, 816, 818, 822, 823, 824, 825, 827, 828, 829, 830, 831, 833, 834, 835, 836, 837, 839]

-----

## Experiment 10: Leaky Bucket Algorithm

[cite\_start]**Problem Statement:** Develop a program for congestion control using a leaky bucket algorithm[cite: 870].

**Java Code (`LeakyBucket.java`)**

```java
import java.util.*;

public class LeakyBucket {
    int I, B, N;
    int dt[];
    int t, p, bs;
    boolean inCtrl = true;
    boolean outCtrl = true;

    void read() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the value of I(size of packets in bytes)");
        I = sc.nextInt();
        System.out.println("Enter the Bucket Size");
        B = sc.nextInt();
        System.out.println("Enter the number of packets of size I to transfer");
        N = sc.nextInt();
        dt = new int[N];
        System.out.println("Enter the arrival time(in seconds) for all to packets in ascending order");
        for (int i = 0; i < N; i++)
            dt[i] = sc.nextInt();
        p = bs = t = 0;
    }

    void insert() {
        if (p < N) {
            if (dt[p] == t) {
                if (bs + I <= B) {
                    bs += I;
                    System.out.println("Packet received at t=" + t + "\t" + bs + " bytes still left in the Bucket");
                } else
                    System.out.println("Bucket overflow. Packet lost at t=" + t);
                p++;
            }
            t++;
        } else
            inCtrl = false;
    }

    void delete() {
        if (bs > 0) {
            bs--;
            System.out.println("1 Byte Leaked.\t\t" + bs + " bytes still left in Bucket");
        } else {
            System.out.println("Bucket is empty. Waiting for incoming packets");
        }
        if (p == N && bs == 0)
            outCtrl = false;
    }

    public static void main(String[] args) {
        LeakyBucket bkt = new LeakyBucket();
        bkt.read();
        InsertThread insThread = new InsertThread(bkt);
        DeleteThread delThread = new DeleteThread(bkt);
    }
}

class InsertThread implements Runnable {
    LeakyBucket bkt1;

    public InsertThread(LeakyBucket bkt) {
        bkt1 = bkt;
        Thread insThread = new Thread(this);
        insThread.start();
    }

    public void run() {
        try {
            while (bkt1.inCtrl) {
                bkt1.insert();
                Thread.sleep(1000);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

class DeleteThread implements Runnable {
    LeakyBucket bkt1;

    public DeleteThread(LeakyBucket bkt) {
        this.bkt1 = bkt;
        Thread delThread = new Thread(this);
        delThread.start();
    }

    public void run() {
        try {
            while (bkt1.outCtrl) {
                bkt1.delete();
                Thread.sleep(1000);
            }
            System.out.println("\nAll packets have been sent");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

[cite\_start][cite: 916, 917, 919, 920, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 937, 939, 941, 943, 945, 946, 947, 950, 951, 953, 960, 962, 964, 966, 968, 973, 974, 975, 976, 978, 979, 982, 983, 984, 986, 987, 989, 991, 992, 993, 995, 997, 998, 1005, 1006, 1008, 1012, 1014, 1015, 1017, 1019, 1020, 1021, 1023, 1025, 1029, 1030, 1031, 1032, 1033]

-----

Would you like me to clarify how any of these specific algorithms work, or explain the NS-2 topology logic?
