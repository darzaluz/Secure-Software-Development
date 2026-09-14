class Vehicle {
    void forward () {
        System.out.println("Vehicle is moving forward");
    }
    
    void reverse () {
        System.out.println("Vehicle is moving in reverse");
    }
}

class SUV extends Vehicle{
    @Override
    void forward() {
        System.out.println("SUV is moving slowly forward");
    }
    @Override
    void reverse() {
        System.out.println("SUV is moving slowly in reverse");
    }
}

class SportsCar extends Vehicle {
    @Override
    void forward() {
        System.out.println("Sports car accelerates fast forward");
    }
    @Override
    void reverse () {
        System.out.println("Sports car reverses fast");
    }
}
class Hybrid extends Vehicle {
    @Override
    void forward() {
        System.out.println("Hybrid car moves forward using electric power and gas");
    }
    @Override
    void reverse() {
        System.out.println("Hybrid car reverses using electric power and gas");
    }
}
public class Main {
    
    public static void main(String[] args) {
        
        Vehicle car = new Vehicle();
        car.forward();
        car.reverse();
        
        SUV suv = new SUV();
        suv.forward();
        suv.reverse();
        
        SportsCar sportsCar = new SportsCar();
        sportsCar.forward();
        sportsCar.reverse ();
        
        Hybrid hybrid = new Hybrid();
        hybrid.forward();
        hybrid.reverse();
    }
}
