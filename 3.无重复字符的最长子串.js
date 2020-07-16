/*
 * @lc app=leetcode.cn id=3 lang=javascript
 *
 * [3] 无重复字符的最长子串
 */
/** 滑动窗口法 ><
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
  // let n = s.length
  // let set = new Set()
  // let ans = 0
  // let i = 0
  // let j = 0
  // while (i < n && j < n) {
  //   if (!set.has(s.charAt(j))) {
  //     set.add(s.charAt(j++))
  //     ans = Math.max(ans, j - i)
  //   } else {
  //     set.delete(s.charAt(i++))
  //   }
  // }

  // 优化
  let n = s.length
  let ans = 0
  let map = new Map()
  for (let i = (j = 0); j < n; j++) {
    if (map.has(s.charAt(j))) {
      i = Math.max(map.get(s.charAt(j)), i)
    }
    ans = Math.max(ans, j - i + 1)
    map.set(s.charAt(j), j + 1)
  }

  return ans
}
