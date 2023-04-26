import java.lang.reflect.Field;
import java.util.function.DoubleUnaryOperator;

public class Square extends Rectangle {

    public Square(){
        super();
    }
    public Square(double side){
        super(side, side);
    }
    public Square(double side, String color, boolean filled){
        super(side, side, color, filled);
    }
   
    public void setWidth(double width){
        super.setLength(width);
        super.setWidth(width);
    }
    public void setLength(double length){
        this.setWidth(length);
    }
    
    public String toString(){
        return ("A Square of side=" + String.valueOf(this.getWidth())
         + ", which is a subclass of" + super.toString());
    }
}
