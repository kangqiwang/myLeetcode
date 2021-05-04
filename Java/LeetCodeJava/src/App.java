
import java.util.ArrayList;
import java.util.List;

public class App {
    public static void main(String[] args) throws Exception {
        /**
         * 
        List<Integer> candyType = new ArrayList<Integer>();
        candyType.add(6);
        candyType.add(6);
        candyType.add(6);
        candyType.add(6);
        candyType.add(6);
        candyType.add(6);
        // System.out.print(candyType);
        DistributeCandies distributeCandies = new DistributeCandies();
        int output =distributeCandies.solution(candyType);
        System.out.println(output);

        // Solution removePalindromicSubsequence = new Solution();
        // System.out.print(removePalindromicSubsequence.removePalindromeSub(str));
        */
        
        String[] words ={"apple"};
        PrefixAndSuffixSearch prefixAndSuffixSearch = new PrefixAndSuffixSearch(words);
        System.out.println(prefixAndSuffixSearch.solution("a", "e"));
    }
}
