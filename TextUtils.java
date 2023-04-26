import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class TextUtils {
    
    public static String[] split(String text){

        List<String> list = new ArrayList<String>();

        int length = text.length();
        String word = "";
        for (int i = 0; i < length;i++){
            if (text.charAt(i) == ' '){
                list.add(word);
            }
            else{
                word += text.charAt(i);
            }

        }
        output = list.toArray(output)
        String[] output = new String[list.size()];
        foreach (String string; list){
            output.add(string);
        }

        return (output);
        }
        
}
