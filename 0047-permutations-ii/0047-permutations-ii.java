import java.util.*;

public class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        backtrack(result, nums, new ArrayList<Integer>(), used);
        return result;
    }

    private void backtrack(List<List<Integer>> result, int[] nums, List<Integer> tempList, boolean [] used){
        if(tempList.size() == nums.length){
            result.add(new ArrayList<>(tempList));
        } else{
            for(int i = 0; i < nums.length; i++){
                if(used[i] || i > 0 && nums[i] == nums[i-1] && !used[i - 1]) continue; // skip duplicates
                used[i] = true; 
                tempList.add(nums[i]);
                backtrack(result, nums, tempList, used);
                used[i] = false; 
                tempList.remove(tempList.size() - 1);
            }
        }
    }
}
