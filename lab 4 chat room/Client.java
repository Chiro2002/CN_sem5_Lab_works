import java.io.*;
import java.net.*;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Client {
    public static void main(String[] args) {
        Socket clientSocket = null;
        BufferedReader userInput = null;
        PrintWriter serverOutput = null;

        try {
            clientSocket = new Socket("localhost", 4445);
            userInput = new BufferedReader(new InputStreamReader(System.in));
            serverOutput = new PrintWriter(clientSocket.getOutputStream(), true);

            System.out.print("Enter your name: ");
            String name = userInput.readLine();
            serverOutput.println(name);

            Thread messageReceiver = new MessageReceiver(clientSocket);
            messageReceiver.start();

            String message;
            while (true) {
                message = userInput.readLine();
                // Check for the exit command and handle it
                if (message != null && message.equalsIgnoreCase("EXIT")) {
                    serverOutput.println("EXIT");
                    break;
                }
                // Prepend the message with the current time
                SimpleDateFormat dateFormat = new SimpleDateFormat("HH:mm:ss");
                String timestamp = dateFormat.format(new Date());
                serverOutput.println("[" + timestamp + "] " + message);
            }
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        } finally {
            try {
                if (clientSocket != null) clientSocket.close();
                if (userInput != null) userInput.close();
                if (serverOutput != null) serverOutput.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}

class MessageReceiver extends Thread {
    private Socket clientSocket;

    public MessageReceiver(Socket clientSocket) {
        this.clientSocket = clientSocket;
    }

    @Override
    public void run() {
        try {
            BufferedReader serverInput = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            String message;
            while ((message = serverInput.readLine()) != null) {
                if (message.equals("EXIT")) {
                    System.out.println("Server has exited. Chat room is closing.");
                    break;
                }
                System.out.println(message);
            }
        } catch (IOException e) {
            System.err.println("Error reading messages from server: " + e.getMessage());
        }
    }
}

