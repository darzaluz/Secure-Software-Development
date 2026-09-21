class Person {
    String name;
}
public class Main {
    
    public static void changeNumber(int number) {
        number = 20;
    }
    
    public static void changeName(Person person) {
        person.name = "Landon";
    }
    public static void main(String[] args) {
        
        int number = 10;
        
        System.out.println("Primitive before: " + number);
        changeNumber(number);
        System.out.println("Primitive after: " + number);
        
        Person person = new Person();
        person.name = "Diego";
        
        System.out.println("Object before: " + person.name);
        changeName(person);
        System.out.println("Object after: " + person.name);
    }
}
