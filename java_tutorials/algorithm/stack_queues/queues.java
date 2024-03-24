class Node {
	 int data;
	 Node next;

	public Node(int data){
		this.data = data;
	}

}


public class queues {

	private Node head;	 // remove from head
	private Node tail;	// add to tail

	public queues(){
		this.head = null;
		this.tail = null;
	}

	public boolean isEmpty(){

		return head == null;
	}

	public int peek(){
		
		return head.data;
	}

	public void add(int data) {
		Node node = new Node(data);
		if(tail != null){
			tail.next = node;
		} else {
			tail = node;
		}

		if(head == null){
			head = node;
		}
	}

	// remove first element ie head
	public int remove(){
		int data = head.data;
		head = head.next;
		if(head == null){
			tail = null;
		}
		return data; // return data from removed head
	}




	public static void main(String[] args){

		System.out.println("Hello, world");
		queues movie_line = new queues();
		movie_line.add(3);

		System.out.println(movie_line.peek());


	}


}
