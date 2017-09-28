package main

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	if l1 == nil && l2 == nil {
		return nil
	}
	ret := new(ListNode)
	curr := ret

	carry := 0
	for l1 != nil || l2 != nil {
		v1, v2 := 0, 0
		if l1 != nil {
			v1 = l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			v2 = l2.Val
			l2 = l2.Next
		}

		sum := v1 + v2 + carry
		curr.Val = sum % 10
		carry = sum / 10

		if l1 == nil && l2 == nil {
			if carry != 0 {
				curr.Next = &ListNode{Val: carry}
			}
			break
		}

		curr.Next = new(ListNode)
		curr = curr.Next
	}

	return ret
}
