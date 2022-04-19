
import java.util.ArrayList;
import java.util.*;


public class DistributeCandies {

    private static <T> List<T> removeDuplicates(List<T> list){
        
        Set<T> set =new LinkedHashSet<>();

        set.addAll(list);
        list.clear();

        list.addAll(set);
        System.out.println(list);
        return list;
    }

    public int solution(List candyType){
        
        // System.out.print(candyType.size()/2);

        List candyTypeRemoveDups = new ArrayList<Integer>();

        candyTypeRemoveDups = removeDuplicates(candyType);
        
        if(candyTypeRemoveDups.size() > candyType.size()/2){
            return candyTypeRemoveDups.size();
        }else{
            return candyType.size()/2;
        }
    }

    public int betterSolution(int[] candyType) {
        // Create an empty Hash Set, and add each candy into it.
        Set<Integer> uniqueCandiesSet = new HashSet<>();
        for (int candy: candyType) {
            uniqueCandiesSet.add(candy);
        }
        // Then, find the answer in the same way as before.
        return Math.min(uniqueCandiesSet.size(), candyType.length / 2);
    }

}
