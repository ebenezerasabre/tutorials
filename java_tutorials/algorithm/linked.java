class Node {
	int data;
	Node next;
	Node prev;

	public Node(int data){
		this.data = data;
		this.next = next;
		this.prev = prev;
	}

}


class Dbl_lnk_list {
	private Node head;

	public Dbl_lnk_list(){
		this.head = null;
	}

	// Method to insert a new node at the end of the dbl lnk list
	public void insertEnd(int data){
		Node newNode = new Node(data);

		if(head == null){
			head = newNode;
		} else {
			Node current = head;
			while(current.next != null){
				current = current.next;
			}
			current.next = newNode;
			newNode.prev = current;
		}

	}


	// method to update the data of anode in the doubly llinked list
	public void updateNode(int old_data, int new_data){
		Node current = head;
		while(current != null){
			if(current.data == old_data){
				current.data = new_data;
				break;
			}
			current = current.next; // for looping
		}

	}


	// method to delete a node from the doubly list
	public void deleteNode(int data){
		Node current = head;
		while(current != null){
			if(current.data == data){
				if(current.prev != null){
					current.prev.next = current.next;
				} else {

					head = current.next;
				}

				if(current.next != null){

					current.next.prev = current.prev;
				}

				break;
			}

			current = current.next;
		}

	}

	// Method to display the elements of the doubly linked list in forward 
	// direction
	public void displayForward(){
		Node current = head;
		while(current != null){

			System.out.print(current.data + " ");
			current = current.next;
		}
		System.out.println();
	}

	// print elements backward
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





public class linked {

	public static void main(String[] args){
		Dbl_lnk_list dbl = new Dbl_lnk_list();

		// inserting node at end
		dbl.insertEnd(1);
		dbl.insertEnd(5);
		dbl.insertEnd(2);
		dbl.insertEnd(10);

		dbl.displayForward();

		System.out.println("linked");

		dbl.displayBackward();

	}

}
