class Solution {
    isAlphanumeric(char) {
        return (
            (char >= 'a' && char <= 'z') ||
            (char >= 'A' && char <= 'z') ||
            (char >= '0' && char <= '9')
        );
    } 

    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let str = "";

        for (const c of s) {
            if (this.isAlphanumeric(c)) {
                str += c.toLowerCase();
            }
        }

        let left = 0;
        let right = str.length - 1;

        while (left < right) {
            if (str[left] !== str[right]) return false;
            left++;
            right--;
        }

        return true;
    }
}
