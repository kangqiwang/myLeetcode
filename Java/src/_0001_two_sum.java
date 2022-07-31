/*
 * 
 * Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

 */

package src;
import java.util.HashMap;


public class _0001_two_sum{
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

    // time complexity: O(n^2)
    public int[] twosum1(int[] nums,int target){
        
        for(int i=0;i<nums.length;i++){
            for(int j=0;j<nums.length;j++){
                if(nums[i]+nums[j] == target){
                    return new int[] {i,j};
                }
            }
        }
        return new int[] {};
    }


    public int[] twosum2(int[] nums,int target){
        
        return new int[] {};
    }
};