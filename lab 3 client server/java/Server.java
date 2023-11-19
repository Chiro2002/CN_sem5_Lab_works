import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) {
        final int port = 9998;
        ServerSocket serverSocket = null;

        try {
            serverSocket = new ServerSocket(port);
            System.out.println("Server listening on port " + port + "...");
            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("Accepted connection from " + clientSocket.getInetAddress() + ":" + clientSocket.getPort());
                new Thread(new ClientHandler(clientSocket)).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if (serverSocket != null) {
                    serverSocket.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    static class ClientHandler implements Runnable {
        private final Socket clientSocket;

        ClientHandler(Socket socket) {
            this.clientSocket = socket;
        }

        @Override
        public void run() {
            try {
                InputStream inputStream = clientSocket.getInputStream();
                OutputStream outputStream = clientSocket.getOutputStream();

                // Read data from the client (in this case, an image)
                FileOutputStream fileOutputStream = new FileOutputStream("received_image.jpg");
                byte[] buffer = new byte[1024];
                int bytesRead;
                while ((bytesRead = inputStream.read(buffer)) != -1) {
                    fileOutputStream.write(buffer, 0, bytesRead);
                }
                fileOutputStream.close();

                System.out.println("Image received from " + clientSocket.getInetAddress() + ":" + clientSocket.getPort());

                // Send a reply to the client
                String replyMessage = "Server received the image successfully";
                outputStream.write(replyMessage.getBytes());

                clientSocket.close();
                System.out.println("Client disconnected: " + clientSocket.getInetAddress() + ":" + clientSocket.getPort());
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}

