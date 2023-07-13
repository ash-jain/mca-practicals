import java.net.*;

class UDPClient {
    public static void main(String[] args) {
        try {
            // Create a UDP socket
            DatagramSocket clientSocket = new DatagramSocket();

            InetAddress serverAddress = InetAddress.getByName("localhost");
            int serverPort = 12345;
            byte[] sendData = "Hello, server!".getBytes();

            // Create a datagram packet with the data to send, server address, and portkt
            DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, serverAddress, serverPort);

            // Send the packet to the server
            clientSocket.send(sendPacket);

            byte[] receiveData = new byte[1024];

            // Receive a response from the server
            DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
            clientSocket.receive(receivePacket);

            String response = new String(receivePacket.getData(), 0, receivePacket.getLength());
            System.out.println("Received from server: " + response);

            // Close the socket
            clientSocket.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
