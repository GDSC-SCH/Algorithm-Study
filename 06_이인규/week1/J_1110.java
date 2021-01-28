import java.util.*;

public class J_1110 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = a;
        int cnt = 0;
        
        while (true) {
            int c = (b/10 + b%10) % 10;
            b = c + (b % 10) * 10;
            cnt++;
            if (a == b){
                break;
            }
        }
        System.out.println(cnt);
        }
}