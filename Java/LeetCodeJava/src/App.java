import java.util.Arrays;

// import java.util.ArrayList;
// import java.util.List;

public class App {
// 
    boolean isUniqueChars(String str){

        if (str.length() > 128) return false;

        boolean[] char_set = new boolean[128];

        for(int i =0;i< str.length();i++){
            int val=str.charAt(i);
            if(char_set[val]) return false;
            char_set[val]=true;
        }

        return true;
    }

    boolean isUniqueChars_bit(String str) {
        int checker = 0;
        for (int i=0;i<str.length();i++){
            int val = str.charAt(i)-'a';
            if((checker &(1<< val))>0) return false;
            checker |= (1<<val);
        }
        return true;
    }

    String sort(String s) {
        char[] content = s.toCharArray();
        Arrays.sort(content);
        return new String(content);
    }
    boolean permutation(String s, String t){
        if (s.length() != t.length()) return false;
        return sort(s).equals(t);
    }

    boolean permutation_2(String s,String t){
        if (s.length() != t.length()) return false;

        int[] letters= new int[286];
        for (int i =0;i<s.length();i++){
            letters[s.charAt(i)]++;
        }

        for (int i=0;i<t.length();i++){
            letters[t.charAt(i)]--;
            if(letters[t.charAt(i)]<0) return false;
        }
        return true;
    }



    public static void main(String[] args) throws Exception {
        App app =new App();
        boolean result= app.isUniqueChars(" a");
        System.out.println(result);

        /**
//          * 
//         List<Integer> candyType = new ArrayList<Integer>();
//         candyType.add(6);
//         candyType.add(6);
//         candyType.add(6);
//         candyType.add(6);
//         candyType.add(6);
//         candyType.add(6);
//         // System.out.print(candyType);
//         DistributeCandies distributeCandies = new DistributeCandies();
//         int output =distributeCandies.solution(candyType);
//         System.out.println(output);

//         // Solution removePalindromicSubsequence = new Solution();
//         // System.out.print(removePalindromicSubsequence.removePalindromeSub(str));
//         */
        
        String[] words ={"apple"};
        PrefixAndSuffixSearch prefixAndSuffixSearch = new PrefixAndSuffixSearch(words);
        System.out.println(prefixAndSuffixSearch.solution("a", "e"));
    }
}
