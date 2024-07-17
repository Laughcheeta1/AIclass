import DFS, BFS

def main():
    graph = {
        "West-Vlaanderen": ["Oost-Vlaanderen", "Hainaut"],
        "Oost-Vlaanderen": ["West-Vlaanderen", "Hainaut", "Antwerpen", "Vlaams-Brabant"],
        "Hainaut": ["West-Vlaanderen", "Oost-Vlaanderen", "Namur", "Brabant Wallon", "Vlaams-Brabant"],
        "Antwerpen": ["Oost-Vlaanderen", "Limburg", "Vlaams-Brabant"],
        "Vlaams-Brabant": ["Oost-Vlaanderen", "Hainaut", "Antwerpen", "Limburg", "Brussels", "Brabant Wallon", "Liege"],
        "Brussels": ["Vlaams-Brabant"],
        "Brabant Wallon": ["Hainaut", "Vlaams-Brabant", "Liege", "Namur"],
        "Namur": ["Hainaut", "Brabant Wallon", "Liege", "Luxembourg"],
        "Limburg": ["Antwerpen", "Vlaams-Brabant", "Liege"],
        "Liege": ["Vlaams-Brabant", "Brabant Wallon", "Namur", "Luxembourg", "Limburg"],
        "Luxembourg": ["Liege", "Namur"]
    }

    limit = 3

    print("Using DFS:")
    dfs = DFS.DFS(graph)
    print(f"The answer without limit is: {dfs.get_answer()}\nThe steps it took is: {dfs.get_nodes_visited()}\n")

    dfs = DFS.DFS(graph, limit)
    print(f"The answer with limit {limit} is: {dfs.get_answer()}\nThe steps it took is: {dfs.get_nodes_visited()}\n\n")

    print("Using BFS:")
    bfs = BFS.BFS(graph)
    print(f"The answer without limit is: {bfs.get_answer()}\nThe steps it took is: {dfs.get_nodes_visited()}\n")

    bfs = BFS.BFS(graph, limit)
    print(f"The answer with limit {limit} is: {bfs.get_answer()}\nThe steps it took is: {dfs.get_nodes_visited()}\n")


if __name__ == "__main__":
    main()
