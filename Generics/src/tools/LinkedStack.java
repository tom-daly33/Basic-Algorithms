package tools;

public class LinkedStack<T> implements IStack<T> {

    class Node {
        T data;
        Node next;

        Node(T data){
            this.data = data;
            this.next = null;
        }

        Node(T data, Node tail){
            this.data = data;
            this.next = tail;
        }
    }

    Node top; // index of the top of the stack, 0 if empty

    public LinkedStack(){
        top = null;
    }

    @Override
    public boolean isEmpty() {
        return top == null;
    }

    @Override
    public boolean push(T value) {
        top = new Node(value, top);
        return true;
    }

    @Override
    public T peek() {
        if(top == null){
            return null;
        }
        return top.data;
    }

    @Override
    public T pop() {
        if(top == null){
            return null;
        }
        T value = peek();
        top = top.next;
        return value;
    }

    public static void main(String[] args) {
        IStack<Integer> stack = new ArrayStack<Integer>(10);
        stack.push(3);
        stack.push(2);
        stack.push(5);
        int product = 1;
        while(!stack.isEmpty()){
            Integer element = (Integer) stack.pop();
            product *= element;
        }
        System.out.println("product is: " + product);
        product = -1;
        while(!stack.isEmpty()){
            Integer element = (Integer) stack.pop();
            product *= element;
        }
        System.out.println("product is: " + product);
        System.out.println("pop empty is: " + stack.pop());
    }
    
}
