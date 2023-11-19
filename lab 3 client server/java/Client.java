import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) {
        if (args.length != 2) {
            System.err.println("Usage: java Client <server_ip> <server_port>");
            System.exit(1);
        }

        String serverIP = args[0];
        int serverPort = Integer.parseInt(args[1]);

        try {
            Socket clientSocket = new Socket(serverIP, serverPort);

            // Send an image to the server
            OutputStream outputStream = clientSocket.getOutputStream();
            FileInputStream fileInputStream = new FileInputStream("image.jpg");
            byte[] buffer = new byte[1024];
            int bytesRead;
            while ((bytesRead = fileInputStream.read(buffer)) != -1) {
                outputStream.write(buffer, 0, bytesRead);
            }
            fileInputStream.close();

            // Receive a reply from the server
            InputStream inputStream = clientSocket.getInputStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));
            String reply = reader.readLine();
            System.out.println("Server reply: " + reply);

            clientSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

