import java.nio.charset.StandardCharsets;
import java.security.SecureRandom;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        
        String message = "MY NAME IS UNKNOWN";
        
        byte[] plaintext = message.getBytes(StandardCharsets.UTF_8);
        
        byte[] key = new byte[plaintext.length];
        
        SecureRandom random = new SecureRandom();
        random.nextBytes(key);
        
        byte[] ciphertext = new byte[plaintext.length];
        
        for (int i = 0; i< plaintext.length; i++) {
            ciphertext[i] = (byte) (plaintext[i] ^ key[i]);
        }
        
        System.out.println("Original message: " + message);
        System.out.println("Ciphertext: " + Arrays.toString(ciphertext));
        
        byte[] decrypted = new byte[plaintext.length];
        
        for (int i = 0; i < ciphertext.length; i++){
            decrypted[i] = (byte) (ciphertext[i] ^ key[i]);
        }
        
        System.out.println("Decrypted message: " +
            new String (decrypted, StandardCharsets.UTF_8));
    }
}
