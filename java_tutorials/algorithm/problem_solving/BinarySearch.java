

class Node {
	public int key;
	public Node left;
	public Node right;

	public Node(){
		this.key = 0;
		this.left = null;
		this.right = null;
	}



}


public class BinarySearch {

	Node root;
	int[] results = {0};
	int ndx = 0;


	public void findRangeElements(Node node, int lh, int hk){
		if(node == null){
			return;
		}

		// if current tree key is in range
		if(node.key >= lh && node.key < hk){
			results[ndx] = node.key;
			ndx++;
		}
		// if left subtree is in range
		if(node.key >= lh){
			findRangeElements(node.left, lh, hk);
		}
		// if right subtree is in range
		if(node.key < hk){
			findRangeElements(node.right, lh, hk);
		}

	}

	private Node add_elem(Node node, int data){
		if(node == null){
			node = new Node();
			node.key = data;
			return node;
		}

		if(data < node.key){
			System.out.println("Left called");
			node.left = add_elem(node.left, data);
		} else if(data > node.key){
			System.out.println("Right called");
			node.right = add_elem(node.right, data);
		}


		return node;
	}

	// Method to insert new node into tree
	public void insert_elem(int data){
		this.root = add_elem(this.root, data);
	}

	public static void main(String[] args){
		System.out.println("Hello, world");
	}
}






