package src;



public class _0002_add_two_sum {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode tails = new ListNode(0);
        ListNode dummy = tails;
        int sum =0;
        while(l1 !=null || l2 != null || sum>0){
            sum+=(l1 == null? 0:l1.val) +(l2==null?0:l2.val);
            tails.next=new ListNode(sum%10);
            tails=tails.next;
            if (l1!=null) l1=l1.next;
            if (l2!=null) l2=l2.next;
            sum/=10;
        }
        return dummy.next;
    }
}
