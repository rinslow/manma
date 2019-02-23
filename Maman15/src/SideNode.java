public class SideNode implements Comparable<SideNode> {
    public double side;
    public RedBlackTree<Double> heights;

    SideNode(double side) {
        this.side = side;
        this.heights = new RedBlackTree();
    }

    @Override
    public int compareTo(SideNode node) {
        return Double.compare(this.side, node.side);
    }
}