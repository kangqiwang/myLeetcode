import java.util.HashMap;

public class twoSum{
    public static void main(String[] args) {
        Solution solution = new Solution();
        int [] nums = {2,7,11,15};
        System.out.println(solution.twosum(nums, 9));
    }
};


class Solution {
    public int[] twosum(int[] nums, int target) {
        HashMap<Integer, Integer> m = new HashMap<Integer, Integer>();
        int[] res = new int[2];
        for (int i=0;i<nums.length; ++i){
            if(m.containsKey(target-nums[i])){
                res[0]=i;
                res[1]=m.get(target-nums[i]);
                break;
            }
            m.put(nums[i], i);
        }
        return res;
    }
    
}