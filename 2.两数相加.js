/*
 * @lc app=leetcode.cn id=2 lang=javascript
 *
 * [2] 两数相加
 */
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
  let dummyHead = new ListNode(0) // 表头
  let p = l1
  let q = l2
  curr = dummyHead
  let carry = 0 // 保存结果 和
  while (p != null || q != null) {
    x = p != null ? p.val : 0
    y = q != null ? q.val : 0
    sum = carry + x + y  // 从左往右对应位相加
    carry = parseInt(sum / 10) // 相加结果是否 > 10 , 是，进 1 (每个节点只能存储一位数字)
    curr.next = new ListNode(sum % 10)  // 取个位 保存结果到链表
    curr = curr.next // 保存结果和的链表指针移到下一个节点
    if (p != null) p = p.next  // 取链表下一个数
    if (q != null) q = q.next // 取下一个
  }
  if (carry > 0) { // 最后一位数相加，是否有进位，有加到链表后
    curr.next = new ListNode(carry)
  }
  return dummyHead.next // 返回结果，取 next 去掉初始化表头的0
}
