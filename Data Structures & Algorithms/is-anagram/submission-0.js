class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false;

        const sCount = {};
        const tCount = {};

        for (const letter of s) {
            if (!sCount[letter]) {
                sCount[letter] = 1;
            } else {
                sCount[letter] += 1;
            }
        }

        for (const letter of t) {
            if (!tCount[letter]) {
                tCount[letter] = 1;
            } else {
                tCount[letter] += 1;
            }
        }

        const sKeys = Object.keys(sCount);

        for (const key of sKeys) {
            if (sCount[key] !== tCount[key]) return false; 
        }
        return true;
    }
}
