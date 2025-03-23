import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main { // Changed from MentalHealthChatbot to Main
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Hello! I'm here to talk. Type 'quit' to exit.");
        
        Map<String, String> responses = new HashMap<>();
        responses.put("stress", "I'm sorry to hear that. Have you tried relaxation techniques like deep breathing?");
        responses.put("anxiety", "Anxiety can be overwhelming. Would you like some coping strategies?");
        responses.put("sad", "It's okay to feel sad. Talking to someone can help. Would you like to share?");
        responses.put("help", "Of course! How can I assist you today?");
        responses.put("depressed", "I'm here to listen. You're not alone. Have you considered speaking to a professional?");
        responses.put("happy", "That's great! Keep embracing the good moments.");
        
        while (true) {
            System.out.print("You: ");
            String userInput = scanner.nextLine().toLowerCase();
            
            if (userInput.equals("quit")) {
                System.out.println("Bot: Take care! Remember, you’re not alone.");
                break;
            }
            
            boolean foundResponse = false;
            for (String keyword : responses.keySet()) {
                if (userInput.contains(keyword)) {
                    System.out.println("Bot: " + responses.get(keyword));
                    foundResponse = true;
                    break;
                }
            }
            
            if (!foundResponse) {
                System.out.println("Bot: I'm here for you. Tell me more.");
            }
        }
        
        scanner.close();
    }
}

