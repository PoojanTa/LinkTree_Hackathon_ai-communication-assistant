# Simple Knowledge Graph implementation for support emails
import networkx as nx
import pandas as pd

class SupportKnowledgeGraph:
    def __init__(self):
        self.graph = nx.Graph()

    def build_from_csv(self, csv_path):
        df = pd.read_csv(csv_path)
        for _, row in df.iterrows():
            sender = row['sender']
            subject = row['subject']
            body = row['body']
            # Add nodes and edges for sender, subject, and keywords
            self.graph.add_node(sender, type='sender')
            self.graph.add_node(subject, type='subject')
            self.graph.add_edge(sender, subject)
            # Extract keywords from body
            keywords = [kw for kw in body.lower().split() if len(kw) > 3]
            for kw in keywords:
                self.graph.add_node(kw, type='keyword')
                self.graph.add_edge(subject, kw)

    def query_related(self, node):
        """Return all nodes directly connected to the given node."""
        return list(self.graph.neighbors(node))

    def visualize(self, out_path='knowledge_graph.png'):
        import matplotlib.pyplot as plt
        plt.figure(figsize=(12,8))
        nx.draw(self.graph, with_labels=True, node_size=500, font_size=8)
        plt.savefig(out_path)
        plt.close()
