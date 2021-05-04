class Solution {

    public int removePalindromeSub(String s) {
        if(s == null){
            return 0;
        }
        int size = s.length();
        
        for (int i = 0; i< size/2;i++){

            if(s.charAt(i) !=s.charAt(size-i-1)){
                return 2;
            }
            //extendLongestPalindrome(s,i,i+1);
        }
        return 1;
    }

    



}