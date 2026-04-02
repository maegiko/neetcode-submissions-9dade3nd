class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const res = {};

        for (const s of strs) {
            const count = new Array(26).fill(0);

            for (const c of s) {
                const charA = "a".charCodeAt(0);
                const charStr = c.charCodeAt(0);

                count[charStr - charA] += 1;
            }

            if (!res[count]) {
                res[count] = [];
            }

            res[count].push(s);
        }

        return Object.values(res);
    }
}
