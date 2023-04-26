import javax.management.ValueExp;

public class Vector {

    private double[] vector;

    public Vector(double[] input){

        for (int i = 0; i < 3; i++){
            vector[i] = input[i];
        }

    }

    public String toString(){
        String output = "[";
        for (double vectorComponant : this.vector){
            
            output = output + (Double.toString(vectorComponant)) + ", ";
        }
        output = output.substring(0, output.length() - 2);
        output += "]";
        return output;
    }

    public int size(){
        return this.vector.length;
    }

    public Double get(int index){
         return this.vector[index];
    }

    public Double set(int index, double value){
        double temp = this.vector[index];
        this.vector[index] = value;
        return temp;
    } 

    public Vector scalarProduct(double scalar){
        double[] doubleList = new double[this.size()];
        for (int i = 0; i < this.size(); i++) doubleList[i] = this.vector[i] * scalar;
        Vector scaledVector = new Vector(doubleList);
        return scaledVector;
    }

    public Vector add(Vector otherVector){
        if (otherVector.size() == this.size())
    }

    public static void main(String[] args){

        double[] data = {1, 1, 1};
        Vector myVector = new Vector(data);

        System.out.println(myVector);


    }
}
    


