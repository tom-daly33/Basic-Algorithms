

public class converter{

    public static double toBase10(String binary){
        double total = 0;
        int length = binary.length();
        for (int i = 0; i < length; i++){
            if (binary.charAt(i) == '1'){
                total += (Math.pow(2, length - 1 - i));
            }

        }
        return total;
        
    }
    
    public static void main(String[] args){

        System.out.println(converter.toBase10("11111111"));
    }
}

