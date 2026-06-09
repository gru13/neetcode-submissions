/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public void reorderList(ListNode head) {
        if(head == null || head.next == null || head.next.next == null)
            return ;

        
        ListNode mid = head;
        ListNode start = head;
        ListNode temp = head.next;

        while(temp!=null){
            mid = mid.next;
            temp = (temp.next==null)?null:temp.next.next;
        }

        ListNode a = null;
        ListNode b = mid.next;
        while(b.next != null){
            temp = b.next;
            b.next = a;
            a = b;
            b = temp; 
        }
        b.next = a;
        mid.next = b;

    
        while(mid.next != null){
            temp = mid.next.next;
            mid.next.next = start.next;
            start.next = mid.next;
            start = start.next.next;
            mid.next = temp;
        }


        for(temp = head;temp!=null;temp=temp.next){
            System.out.print(temp.val+", ");
        }
        
    }
}
