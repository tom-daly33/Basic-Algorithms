""" package tools;

import java.util.Map;

public class ArraySet<E> implements ISet<E> {
    
    E[] set;
    int members;

    public ArraySet(int size){
        set = (E[]) new Object[size];
        members = 0;
    }

    @Override
    public boolean contains(E elt){
        for (E member : set){
            if (member.equals(elt)){
                return true;
            }
        }
        return false;
    }

    @Override
    public boolean isEmpty(){
        if (this.size() == 0){
            return true;
        }
        return false;
    }

    @Override public int size(){
        return (this.members);
    }

    public boolean add(E elt){
        if (this.contains(elt)){
            return false;
        }
        set[this.members] = elt;
        members += 1;
        return true;
    }

    public void clear(){

    }

    public boolean remove(E elt){
        if (this.contains(elt)){
            int index = 0;
            for (E member : set){
                if (member == elt){
                    break;
                }
                index += 1;
            }
            // change pos of other items :(
        }
        return false;
    }
}



        
        """;