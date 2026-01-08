```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World from VB!");
        System.out.println("Hello, My name is Yogeshwar!");
        System.out.println("Hello, I am done successfully!");
        System.out.println("Hello, I am done successfully!");
        System.out.println("Hello, I am done successfully!");
        System.out.println("Hello, World from VB!");
        System.out.println("Hello, My name is Yogeshwar!");
        System.out.println("Hello, I am done successfully!");
        System.out.println("Hello, I am done successfully!");
        System.out.println("Hello, I am done successfully!");
        System.out.println("Hello, I am done successfully!");
        System.out.println("Hello, World from VB!");
        System.out.println("Hello, My name is Yogeshwar!");
        System.out.println("Hello, I am done successfully!");
        System.out.println("Hello, I am done successfully!");
        System.out.println("Hello, I am done successfully!");

        // Call calculator
        Calculator.runCalculator();
    }
}

class Calculator {
    public static void runCalculator() {
        double a, b;
        String op;

        System.out.println("Enter first number:");
        a = Double.parseDouble(System.console().readLine());

        System.out.println("Enter second number:");
        b = Double.parseDouble(System.console().readLine());

        System.out.println("Enter operator (+, -, *, /):");
        op = System.console().readLine();

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
    }
}
```