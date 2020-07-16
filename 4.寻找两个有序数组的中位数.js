/*
 * @lc app=leetcode.cn id=4 lang=javascript
 *
 * [4] 寻找两个有序数组的中位数
 */

// @lc code=start
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
  let mergeArr = nums1.concat(nums2).sort((a, b) => a - b)
  let mid = Math.ceil(mergeArr.length / 2) - 1
  if (mergeArr.length % 2 === 1) {
    return mergeArr[mid]
  }
  return (mergeArr[mid] + mergeArr[mid + 1]) / 2

  // 归并排序
  // if (nums1.length > nums2.length) return findMedianSortedArrays(nums2, nums1)
  // const x = nums1.length, y = nums2.length
  // let lo = 0, hi = x

  // while(lo < hi) {
  //   let partitionX = (lo + hi) / 2,
  //       partitionY = (x + y + 1) / 2 - partitionX | 0
  // }
}
// @lc code=end
