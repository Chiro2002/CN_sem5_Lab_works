import java.io.*;
import java.net.*;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class Server {
    private static List<ServerThread> clients = new ArrayList<>();

    public static void main(String[] args) {
        ServerSocket serverSocket = null;

        try {
            serverSocket = new ServerSocket(4445);
            System.out.println("Server listening");

            // Add a BufferedReader to read server messages
            BufferedReader serverMessages = new BufferedReader(new InputStreamReader(System.in));
            String serverMessage;

            while (true) {
                serverMessage = serverMessages.readLine();
                if (serverMessage.equalsIgnoreCase("EXIT")) {
                    // Inform all clients about the server's exit
                    String exitMessage = "Server has exited the chat.";
                    broadcastMessage(exitMessage, null);
                    System.exit(0);
                } else {
                    // Broadcast the server message to all clients
                    broadcastMessage("Server: " + serverMessage, null);
                }
            }

        } catch (IOException e) {
            System.out.println("Server error: " + e.getMessage());
        } finally {
            try {
                if (serverSocket != null) serverSocket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    public static synchronized void broadcastMessage(String message, ServerThread sender) {
        for (ServerThread client : clients) {
            if (client != sender) {
                client.sendMessage(message);
            }
        }
    }

    public static synchronized void removeClient(ServerThread client) {
        clients.remove(client);
    }
}

class ServerThread extends Thread {
    private Socket clientSocket;
    private PrintWriter out;
    private String name;

    public ServerThread(Socket clientSocket) {
        this.clientSocket = clientSocket;
    }

    @Override
    public void run() {
        try {
            BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            out = new PrintWriter(clientSocket.getOutputStream(), true);

            // Get the client's name
            name = in.readLine();
            String welcomeMessage = "Welcome, " + name + "!";
            Server.broadcastMessage(welcomeMessage, this);

            String message;
            while (true) {
                message = in.readLine();
                if (message == null || message.equalsIgnoreCase("QUIT")) {
                    break;
                }
                if (message.equalsIgnoreCase("EXIT")) {
                    String exitMessage = name + " has left the chat.";
                    Server.broadcastMessage(exitMessage, this);
                    break;
                }

                // Prepend the message with the current time and sender's name
                SimpleDateFormat dateFormat = new SimpleDateFormat("HH:mm:ss");
                String timestamp = dateFormat.format(new Date());
                String formattedMessage = "[" + timestamp + "] " + name + ": " + message;
                Server.broadcastMessage(formattedMessage, this);
            }
        } catch (IOException e) {
            System.err.println("Error in client thread: " + e.getMessage());
        } finally {
            try {
                if (clientSocket != null) clientSocket.close();
                Server.removeClient(this);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    public void sendMessage(String message) {
        out.println(message);
    }
}

