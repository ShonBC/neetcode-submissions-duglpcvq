/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = head;
        int count{0};
        while (dummy->next) {
            dummy = dummy->next;
            count++;
        }
        if (count + 1 == n) return head->next;
        dummy = head;
        while (count > n) {
            dummy = dummy->next;
            count--;
        }
        ListNode* next = dummy->next ? dummy->next : nullptr;
        dummy->next = next->next ? next->next : nullptr;
        return head;
    }
};
