public class MainApp {

    public static void main(String[] args){

        TallyCounter tallyCount = new TallyCounter();

        System.out.println(tallyCount);

        tallyCount.increment();
        System.out.println(String.valueOf(tallyCount.read()));
        tallyCount.reset();
        System.out.println(tallyCount);


    }
    
}
