import java.util.Scanner;

public class Areas {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Área del cuadrado
        System.out.print("Ingrese el lado del cuadrado: ");
        double lado = sc.nextDouble();
        double areaCuadrado = lado * lado;
        System.out.println("Área del cuadrado: " + areaCuadrado);

        // Área del triángulo
        System.out.print("Ingrese la base del triángulo: ");
        double base = sc.nextDouble();
        System.out.print("Ingrese la altura del triángulo: ");
        double altura = sc.nextDouble();
        double areaTriangulo = (base * altura) / 2;
        System.out.println("Área del triángulo: " + areaTriangulo);

        // Área del círculo
        System.out.print("Ingrese el radio del círculo: ");
        double radio = sc.nextDouble();
        double areaCirculo = Math.PI * radio * radio;
        System.out.println("Área del círculo: " + areaCirculo);

        // Área del rectángulo
        System.out.print("Ingrese la base del rectángulo: ");
        double baseRect = sc.nextDouble();
        System.out.print("Ingrese la altura del rectángulo: ");
        double alturaRect = sc.nextDouble();
        double areaRectangulo = baseRect * alturaRect;
        System.out.println("Área del rectángulo: " + areaRectangulo);

        sc.close();
    }
}