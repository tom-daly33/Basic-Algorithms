public class TallyCounter {

    private int counter;
    private int digits;

    public TallyCounter(){
        this.counter = 0;
        this.digits = 3;
    }

    public TallyCounter(int digits){
        if (digits < 3){
            digits = 3;
        }
        this.counter = 0;
        this.digits = digits;
        
    }

    public void increment(){
        this.counter += 1;
        if (this.counter == this.digits * 10){
            this.counter = 0;
        }
    }

    public void decrement(){
        if (this.counter != 0){
            this.counter -= 1;
        }
    }

    public int read(){
        return this.counter;
    }

    public void reset(){
        this.counter = 0;
    }

    public String toString(){
        return (String.format("%03d", this.counter));
    }
    
}
