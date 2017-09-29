package ske;

import java.util.Scanner;

public class skeres {
	private static Scanner sc = new Scanner(System.in);
	public static void main(String[] args) {
         menu();
		 
		 
	}
    
    public static void Pizza(int x) {
    	
    	int sum;
		sum = x*250;
		System.out.println("| Pizza            |      "+x+"  |      "+sum+"  |");
	}
    public static int total01(int t1) {
    	return t1*250;
    }
    public static void Chickens(int y) {
    	
    	int sum;
		sum = y*120;
		System.out.println("| Chickens         |      "+y+"  |      "+sum+"  |");
	}
    public static int total02(int t2) {
    	return t2*120;
    }
    public static void Coke(int z) {
    	
    	int sum;
		sum = z*45;
		System.out.println("| Coke             |      "+z+"  |      "+sum+"   |");
	}
    public static int total03(int t3) {
    	return t3*45;
    }
    public static void choice() {
    	int choice;
    	int quantity = 0;
    	int quantity2=0;
    	int quantity3=0;
    	do {
    		
    	do {
   		 System.out.print("Enter your Choice: ");
   		 choice = sc.nextInt();
   		 if (choice == 5) {
   			 break;
   		 }
   		if(choice == 1) {
   			System.out.print("Enter Quantity: ");
   		   quantity = sc.nextInt();
   		}
   		if(choice == 2) {
   			System.out.print("Enter Quantity: ");
   		   quantity2 = sc.nextInt();
   		}
   		if(choice == 3) {
   			System.out.print("Enter Quantity: ");
   		   quantity3 = sc.nextInt();
   		}
   		
    	}while(choice !=4);
    	
    	if(choice == 4) {
   			choice4(quantity,quantity2,quantity3);
   			
   		}
    	}while(choice !=5);
    	System.out.println("==== Thank you ====");
	}
   public static void menu() {
	   System.out.println("--------- Welcome to SKE Restaurant ---------");
		 System.out.println("1.) Pizza       250 Baht.");
		 System.out.println("2.) Chickens    120 Baht.");
		 System.out.println("3.) Coke        45 Baht.");
		 System.out.println("4.) Total");
		 System.out.println("5.) Exit");
		 choice();
   }
   public static void choice4(int quantity , int quantity2 , int quantity3) {
	   System.out.println("+------ Menu ------+-- Qty --+-- Price --+");
			if(quantity*250>0) {
			Pizza(quantity);
			total01(quantity);}
			if(quantity2*120>0) {
			Chickens(quantity2);
			total02(quantity2);}
			if(quantity3*45>0) {
			Coke(quantity3);
			total03(quantity3);}
			System.out.println("+------------------+---------+-----------+");
			System.out.printf("| Total                      |      %d  | \n",total01(quantity)+total02(quantity2)+total03(quantity3));
			System.out.println("+------------------+---------+-----------+");
   }
}
