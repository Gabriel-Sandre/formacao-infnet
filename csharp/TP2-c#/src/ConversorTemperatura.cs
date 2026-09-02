using System;

class Program
{
    static void Main()
    {
        Console.Write("Digite a temperatura em Celsius: ");
        double celsius = double.Parse(Console.ReadLine());

        double fahrenheit = celsius * 9 / 5 + 32;
        double kelvin = celsius + 273.15;

        Console.WriteLine();
        Console.WriteLine("===== CONVERSÃO DE TEMPERATURA =====");
        Console.WriteLine($"Celsius:    {celsius:F2} °C");
        Console.WriteLine($"Fahrenheit: {fahrenheit:F2} °F");
        Console.WriteLine($"Kelvin:     {kelvin:F2} K");
        Console.WriteLine("====================================");
    }
}
