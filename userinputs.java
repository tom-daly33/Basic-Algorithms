import java.util.Scanner;

public class userinputs {

    public static void main(String[] args){

        Scanner keyboard = new Scanner(System.in);
        System.out.print("Enter Int >> ");
        int number = keyboard.nextInt();

        System.out.println("Number entered is: " + number);
    }
    
}
