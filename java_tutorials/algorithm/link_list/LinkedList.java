class Node {
	int data;
	Node next;
	Node prev;

	public Node(int data){
		this.data = data;
		this.next = null;
		this.prev = null;

	}

}


class doubly_linked_list {
	private Node head;

	public doubly_linked_list(){
		head = null;
	}

	// insert node
	public void insertEnd(int data){
		Node newNode = new Node(data);
		if(head == null){
			head = newNode;
		} else {
			Node current = head;
			// find a free node to insert
			while(current.next != null){
				current = current.next;
			}
			current.next = newNode;
			newNode.prev = current;
		}
	}
	// delete node
	public void deleteNode(int data){
		Node current = head;
		while(current != null){
			if(current.data == data){

				// check if there's previous node
				if(current.prev != null){
					current.prev.next = current.next;

				} else {
					// current is head, move head to next node
					head = current.next;
				}

				// check if there's next node
				if(current.next != null){
					current.next.prev = current.prev;
				}
				// delete completed break
				break;
			}

			// increment to next node
			current = current.next;
		}

	}
	// update node
	public void updateNode(int old_data, int new_data){
		Node current = head;
		while(current != null){
			if(current.data == old_data){
				current.data = new_data;
			}
			current = current.next;
		}

	}

	public void displayForward(){
		Node current = head;
		while(current != null){
			System.out.print(current.data + " ");
			current = current.next;
		}
		System.out.println();
	}

	public void displayBackward(){
		Node current = head;
		while(current.next != null){
			current = current.next;
		}

		while(current != null){
			System.out.print(current.data + " ");
			current = current.prev;
		}
		System.out.println();

	}


}

public class LinkedList {
	
	public static void main(String[] args){
		doubly_linked_list linked = new doubly_linked_list();
		linked.insertEnd(5);
		linked.insertEnd(12);
		linked.insertEnd(45);
		linked.insertEnd(100);
		linked.insertEnd(1);
		linked.insertEnd(30);

		//linked.deleteNode(1);
		linked.displayForward();
		linked.deleteNode(1);
		linked.deleteNode(30);
		linked.updateNode(5, 155);
		linked.displayForward();
		//linked.updateNode(100, 450);
		//linked.displayForward();
	}

}
