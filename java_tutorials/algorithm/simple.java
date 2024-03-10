public class simple {

	public static void main(String args[]){

		// class instance
		//secondClass obj = new secondClass();
		BinaryTree b_tree = new BinaryTree();

		//System.out.println("Hello, java");
		//System.out.println(show());
		//obj.new_era();

		b_tree.insert(50);
		b_tree.insert(24);
		b_tree.insert(78);
		b_tree.insert(12);
		b_tree.insert(3);
		//b_tree.insert(1);
		b_tree.insert(120);

		System.out.println("In-Order traversal:");
		b_tree.inOrderTraversal();
	}


	private static String show(){
		String name = "Ebenezer";
		return name;
	}
 }

class secondClass {
	int length;

	void new_era(){
		System.out.println("secondClass called");
	}

	public secondClass(){
		this.length = 10;
	}
}

class TreeNode {
	int data;
	TreeNode left;
	TreeNode right;

	public TreeNode(int data){
		this.data = data;
		this.left = null;
		this.right = null;
	}
}

class BinaryTree {
	TreeNode root;

	public BinaryTree(){
		this.root = null;
		System.out.println("BianryTree called");
	}


	// Method to inset a new node in the binary tree
	public void insert(int data){
		this.root = insertRecursive(this.root, data);
	
	}

	private TreeNode insertRecursive(TreeNode root, int data){
	
		if(root == null){
			System.out.println("root == null callled");
			root = new TreeNode(data);
			return root;
		}

		if(data < root.data){
			
			System.out.println("data < root.data called " + data + " < " + root.data);
			root.left = insertRecursive(root.left, data);
		}else if(data > root.data){
			System.out.println("data > root.data called "  + data + " > " + root.data);
			root.right = insertRecursive(root.right, data);
		}
		
		System.out.println("insertRecursive- return root called ");
		return root;
	}

	// Method to perform an in-order traversal of the binary tree

	public void inOrderTraversal(){
		inOrderTraversalRecursive(this.root);
	}


	private void inOrderTraversalRecursive(TreeNode root){
		if(root  != null){
			inOrderTraversalRecursive(root.left);
			System.out.println(root.data + " ");
			inOrderTraversalRecursive(root.right);
		}
	}



}















