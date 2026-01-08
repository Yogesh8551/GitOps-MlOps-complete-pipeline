Module HelloWorld
    Sub Main()
        Console.WriteLine("Hello, World from VB!")
        Console.WriteLine("Hello, My name is Yogeshwar!")
        Console.WriteLine("Hello, I am done successfully!")
        Console.WriteLine("Hello, I am done successfully!")
        Console.WriteLine("Hello, I am done successfully!")
        Console.WriteLine("Hello, World from VB!")
        Console.WriteLine("Hello, My name is Yogeshwar!")
        Console.WriteLine("Hello, I am done successfully!")
        Console.WriteLine("Hello, I am done successfully!")
        Console.WriteLine("Hello, I am done successfully!")
        #this is chagnes
        
        hjgjhffkjghkljfgfhjf

        ' Call calculator
        Calculator.RunCalculator()
    End Sub
End Module

Module Calculator
    Public Sub RunCalculator()
        Dim a, b As Double
        Dim op As String

        

        Console.WriteLine("Enter first number:")
        a = Double.Parse(Console.ReadLine())

        Console.WriteLine("Enter second number:")
        b = Double.Parse(Console.ReadLine())

        Console.WriteLine("Enter operator (+, -, *, /):")
        op = Console.ReadLine()

        If op = "+" Then
            Console.WriteLine("Result: " & (a + b))
        ElseIf op = "-" Then
            Console.WriteLine("Result: " & (a - b))
        ElseIf op = "*" Then
            Console.WriteLine("Result: " & (a * b))
        ElseIf op = "/" Then
            Console.WriteLine("Result: " & (a / b))
        Else
            Console.WriteLine("Invalid operator!")
        End If
    End Sub
End Module
