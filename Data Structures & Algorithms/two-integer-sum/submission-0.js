class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const numsHash = {};
        const result = [];

        for (const numIndex in nums) {
            const difference = target - nums[numIndex];

            if (numsHash[difference] === undefined) {
                numsHash[nums[numIndex]] = numIndex;
            } else {
                result.push(Number(numsHash[difference]));
                result.push(Number(numIndex));
                break;
            }
        }

        result.sort();
        return result;
    }
}
