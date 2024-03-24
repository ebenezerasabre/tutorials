import java.util.Arrays;

public class MinHeap {
	private int capacity = 10;
	private int size = 0;

	int[] items = new int[capacity];

	private int getLeftChildIndex(int parentIndex) { return 2 * parentIndex + 1; }
	private int getRightChildIndex(int parentIndex) { return 2 * parentIndex + 2; }
	private int getParentIndex(int childIndex){ return (childIndex - 1) / 2; }

	private boolean hasLeftChild(int index) { return getLeftChildIndex(index) < size; }
	private boolean hasRightChild(int index) { return getRightChildIndex(index) < size; }
	private boolean hasParent(int index){ return getParentIndex(index) >= 0; }

	private int leftChild(int index) { return items[getLeftChildIndex(index)]; }
	private int rightChild(int index) { return items[getRightChildIndex(index)]; }
	private int parent(int index) { return items[getParentIndex(index)]; }

	private void swap(int indexOne, int indexTwo){
		int temp = items[indexOne];
		items[indexOne] = items[indexTwo];
		items[indexTwo] = temp;
	}

	private void ensureExtraCapacity(){
		if(size == capacity){

			items = Arrays.copyOf(items, capacity * 2);
			capacity *= 2;
		}

	}

	private int peek(){
		if (size == 0) throw new IllegalStateException();
		return items[0];
	}


	private int poll(){
		if (size == 0) throw new IllegalStateException();
		int item = items[0];
		items[0] = items[size - 1]; 	 // replace first item with last item
		size--;				 // reduce size of heap
		heapifyDown();			 // reorder heap down
		return item;			 // return removed item
	}


	// add element to heap
	public void add(int item){
		ensureExtraCapacity();
		items[size] = item;
		size++;
		heapifyUp();
	
	}


	// when we add an item ( to the end )
	public void heapifyUp(){
		int index = size - 1;
		while (hasParent(index) && parent(index) > items[index]){
			swap(getParentIndex(index), index);
			index = getParentIndex(index); // set parent index
		}

	}


	// when we remove the minimum element
	public void heapifyDown(){
		int index = 0;
		// we only check if there's a left child because
		// if there's no leftchild theres certainly no right child
		while(hasLeftChild(index)){
			int smallerChildIndex = getLeftChildIndex(index);
			if(hasRightChild(index) && rightChild(index) < leftChild(index)){
				smallerChildIndex = getRightChildIndex(index);
			}

			if (items[index] < items[smallerChildIndex]){
				break;
			} else {
				swap(index, smallerChildIndex);
	
			}
			index = smallerChildIndex;	
		}
	}

	public static void main(String[] args){
		MinHeap min_heap = new MinHeap();
		min_heap.add(40);
		min_heap.add(3);
		min_heap.add(13);
		min_heap.add(35);
		min_heap.add(2);
		min_heap.add(46);
		System.out.println("items: " + Arrays.toString(min_heap.items));
	}

}
