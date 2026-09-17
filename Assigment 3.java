import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        
        Map< String, String> passwords = new HashMap<>();
        Map< String, String> roles = new HashMap<>();
        
        passwords.put("diego","tennis123");
        passwords.put("admin", "admin123");
        
        roles.put("diego", "user");
        roles.put("admin", "admin");
        
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Username: ");
        String username = scanner.nextLine();
        
        System.out.print("Password: ");
        String password = scanner.nextLine();
        
        if (passwords.containsKey(username) &&
            passwords.get(username).equals(password)) {
                
                System.out.println("Login succesful!");
                
                String role = roles.get(username);
                
                System.out.println("Role: " + role);
                
                System.out.println("\n--- MENU ---");
                System.out.println("1. View profile");
                System.out.println("2. Administrator seetings");
                
                System.out.print("\nChoose an option ");
                String choice = scanner.nextLine();
                
                if (choice.equals("1")) {
                    
                    System.out.println("Profile access granted.");
                    
                } else if (choice.equals("2")) {
                
                    if (role.equals("admin")) {
                        System.out.println("Administrator access granted.");
                    } else {
                        System.out.println("ACCESS DENIED: not an administraator");
                    } 
                    
                } else {
                    System.out.println("Invalid option.");
                }
            } else {
                System.out.println("Invalid username or password");
            }
            
            scanner.close();
    }
}
