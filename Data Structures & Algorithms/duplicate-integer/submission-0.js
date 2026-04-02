class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const numsSeen = {};

        // Initialising Seen Dictionary
        for (const num of nums) {
            numsSeen[num] = false;
        }

        for (const num of nums) {
            if (numsSeen[num] === true) {
                return true;
            } else {
                numsSeen[num] = true;
            } 
        }

        return false;
    }
}
