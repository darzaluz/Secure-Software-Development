import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {
    

    public static void main(String[] args) {
        
            Scanner input = new Scanner(System.in);
    
    System.out.println("Enter the number of the file that you want to open, example \"file1\"");
    String fileName = input.nextLine();
    
        try {
            FileReader file = new FileReader(fileName);
            BufferedReader reader = new BufferedReader(file);
            
            String line = reader.readLine();
            
            System.out.println("File content: " + line);
            
            reader.close();
        } catch (FileNotFoundException e){
            System.out.println("The file doesn't exist");
        }
        catch (IOException e) {
            System.out.println("The file can not be found or read");
        }
    }
}
