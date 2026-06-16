/**
 * Definition for singly-linked list.
 */
 struct ListNode {
    int val;
    struct ListNode *next;
 };
struct ListNode* deleteMiddle(struct ListNode* head) {
    if(head == NULL || head->next == NULL) {
        return NULL;
    }

    struct ListNode* p1=head;
    struct ListNode* p2=head;
    struct ListNode* temp=NULL;

    while(p2 && p2->next) {
        temp = p1;
        p1 = p1->next;
        p2 = p2->next->next;
    }
    temp->next = p1->next;
    free(p1);
    return head;
}