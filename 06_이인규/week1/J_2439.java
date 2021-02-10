import java.util.*;

public class J_2439 {
	
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		
		for(int i=1; i<a+1; i++) {
			for(int one=0; one<a-i; one++) {
				System.out.print(' ');
			}
			for(int one=0; one<i; one++) {
				System.out.print('*');
			}
			System.out.print('\n');
		}
		sc.close();
	}
}
