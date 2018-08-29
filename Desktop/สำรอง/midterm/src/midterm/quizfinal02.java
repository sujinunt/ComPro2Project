package midterm;

import java.util.Scanner;

public class quizfinal02 {
private static Scanner sc = new Scanner(System.in);
private static int []x = new int [20];
private static int []y = new int [20];
	public static void main(String[] args) {
		sentValue();
}
	public static void sentValue() {
		String c;
		String m;
		int k=0;
		do {
			for(int i=0;i<k+1;i++) {
			System.out.printf("Enter x%d :",k+1);
			 x[k+1] = sc.nextInt();
			 break;
			 }
			for(int j=0;j<k+1;j++) {
			System.out.printf("Enter y%d :",k+1);
			 y[k+1] = sc.nextInt();
			 break;}
			System.out.print("(m)ore,(e)nd :");
			m = sc.next();
			k++;
		}while(m.equals("m"));
		do {
		System.out.print("(s)how points,(d)istance,(n)ew,(q)uit :");
		c = sc.next();
		if(c.equals("s")) {
			for(int value=1;value<=k;value++) {
			System.out.printf("Point %d = (%d,%d)\n",value,x[value],y[value]);}
		}else
		if(c.equals("q")) {
			System.out.println("Bye");
		}else if(c.equals("d")) {
			distance();
		}else if(c.equals("n")) {
			value();
		}
		
		}while(c.equals("s")||(c.equals("d")));
	}
public static void distance() {
	double v1 = x[1]-x[2];
	double v2 = y[1]-y[2];
	double pow01 = Math.pow(v1, 2);
	double pow02 = Math.pow(v2, 2);
	double g = Math.sqrt(pow01+pow02);
	System.out.printf("Distance from P1 to P2 is %.2f\n",g);
}
public static void value() {
	sentValue();
}
	}