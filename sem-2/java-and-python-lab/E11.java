import java.net.*;

class UDPServer {
    public static void main(String[] args) {
        try {
            // Create a UDP socket
            DatagramSocket serverSocket = new DatagramSocket(12345);

            byte[] receiveData = new byte[1024];

            System.out.println("UDP server is running...");

            while (true) {
                // Receive data from the client
                DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
                serverSocket.receive(receivePacket);

                String request = new String(receivePacket.getData(), 0, receivePacket.getLength());
                System.out.println("Received from client: " + request);

                InetAddress clientAddress = receivePacket.getAddress();
                int clientPort = receivePacket.getPort();
                byte[] sendData = "Hello, client!".getBytes();

                // Create a datagram packet with the response data, client address, and port
                DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, clientAddress, clientPort);

                // Send the packet to the client
                serverSocket.send(sendPacket);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}