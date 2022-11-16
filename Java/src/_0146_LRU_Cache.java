package src;
import java.util.HashMap;
import java.util.Map;

class _0146_LRU_Cache {
    class Node{
        int key;
        int value;
        Node prev, next;
        Node(int _key,int _value){
            key = _key;
            value=_value;
        }
    }

    Node head= new Node(0, 0);
    Node tail = new Node(0, 0);
    Map<Integer,Node> map = new HashMap();
    int capacity;

    public _0146_LRU_Cache(int capacity){
        this.capacity = capacity;
        head.next= tail;
        tail.prev = head;
    }

    public int get(int key){
        return key;
        
    }

    public void put(int key, int value){

    }


    public static void main(String[] args) {
        
    }
}

