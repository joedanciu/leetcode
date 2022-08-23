/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func isPalindrome(head *ListNode) bool {
    index, counter, convertedLL, startIndex, endIndex := head, 0, make([]int, 0), 0, 0
    
    for index != nil{
        convertedLL = append(convertedLL, index.Val)
        counter += 1
        index = index.Next
    }
    
    endIndex = len(convertedLL) - 1
    for endIndex >= startIndex{
        if convertedLL[endIndex] != convertedLL[startIndex]{
            return false
        }
        endIndex -= 1
        startIndex += 1
    }
    return true
}
