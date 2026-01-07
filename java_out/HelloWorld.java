```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World from VB!");
        System.out.println("Hello, My name is yogeshwar!");
        System.out.println("Hello, i am done successfully!");
        System.out.println("Hello, i am done successfully!");
        System.out.println("Hello, i am done successfully!");

        Calculator.main();
    }
}

class Calculator {
    public static void main() {
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        double a, b;
        String op;

        System.out.println("Enter first number:");
        a = scanner.nextDouble();

        System.out.println("Enter second number:");
        b = scanner.nextDouble();

        System.out.println("Enter operator (+, -, *, /):");
        op = scanner.next();

        if (op.equals("+")) {
            System.out.println("Result: " + (a + b));
        } else if (op.equals("-")) {
            System.out.println("Result: " + (a - b));
        } else if (op.equals("*")) {
            System.out.println("Result: " + (a * b));
        } else if (op.equals("/")) {
            System.out.println("Result: " + (a / b));
        } else {
            System.out.println("Invalid operator!");
        }
        scanner.close();
    }
}
```