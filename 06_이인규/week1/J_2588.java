import java.util.Scanner;

public class J_2588 {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();

        System.out.println((int) a * (int)b%10);
        System.out.println(a * (int)b/10);
        System.out.println(a * (int)b/100);
        System.out.println(a*b);
    }
}