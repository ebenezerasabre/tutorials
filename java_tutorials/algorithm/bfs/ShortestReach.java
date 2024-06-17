import java.util.*;


class Graph {
	private int V;
	private LinkedList<Integer> adj[];
	
	Graph(int v){
		V = v;
		adj = new LinkedList[v];
		for (int i=0; i<v; i++)
			adj[i] = new LinkedList<Integer>();
	}


	void addEdge(int v, int w){
		adj[v].add(w);
		adj[w].add(v);	// for undirected graph

	}


	void shortestReach(int start){
		boolean visited[] = new boolean[V];
		int dist[] = new int[V];

		Queue<Integer> queue = new LinkedList<Integer>();

		visited[start] = true;
		queue.add(start);
		dist[start] = 0;

		while (!queue.isEmpty()){
			int current = queue.poll();

			for(int neighbor : adj[current]){
				if(!visited[neighbor]){
					visited[neighbor] = true;
					queue.add(neighbor);
					dist[neighbor] = dist[current] + 6; // Adduming edge weights are all 6
	
				}
			
			}
		}

		for (int i=0; i<V; i++){
			if(i != start){
				System.out.print(dist[i] + " ");
			} else {
				System.out.print("-1 ");
			}

		}

		System.out.println();
	}
}


public class ShortestReach {
	public static void main(String args[]){
		Scanner scanner = new Scanner(System.in);
		int q = scanner.nextInt(); // Number of queries

		for(int k=0; k<q; k++){
			int n = scanner.nextInt(); // Number of noes
			int m = scanner.nextInt(); // Number of edges
		
			Graph graph = new Graph(n);

			for(int i=0; i<m; i++){
				int u = scanner.nextInt() - 1; // 0-based indexing
				int v = scanner.nextInt() - 1; // 0-based indexing
				graph.addEdge(u, v);

			}

			int s = scanner.nextInt() - 1; // starting node, 0-based indexing
			graph.shortestReach(s);
		
		
		}


	}


}






































