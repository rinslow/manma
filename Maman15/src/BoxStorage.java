import java.util.List;

public class BoxStorage {

    private RedBlackTree<SideNode> sides;

    BoxStorage(){
        this.sides = new RedBlackTree<>();
    }

    public void insertBox(double side, double height){
        SideNode sideNode = new SideNode(side);
        RedBlackNode<SideNode> existedSideNode = this.sides.search(sideNode);

        if(existedSideNode == null) // The side we want does not exist
        {
            sideNode.heights.insert(height);
            this.sides.insert(sideNode);
        }
        else {
            existedSideNode.key.heights.insert(height);
        }
    }

    public void removeBox(double side, double height){
        SideNode sideNode = new SideNode(side);
        RedBlackNode<SideNode> existedSideNode = this.sides.search(sideNode);
        existedSideNode.key.heights.remove(existedSideNode.key.heights.search(height));
    }

    public Box getBox(double side, double height){
        SideNode sideNode = new SideNode(side);

        double minimalVolume = Double.MAX_VALUE;
        double minimalVolumeSide = 0;
        double minimalVolumeHeight = 0;

        for (SideNode matchSideNode : this.sides.getGreaterOrEqualsThan(sideNode, this.sides.size())){

            RedBlackNode<Double> minimalHeightNode = matchSideNode.heights.serachSuccessor(height);
            if(minimalHeightNode == null){
                continue;
            }

            double volume = matchSideNode.side * matchSideNode.side * minimalHeightNode.key;
            if(volume < minimalVolume){
                minimalVolume = volume;
                minimalVolumeHeight = minimalHeightNode.key;
                minimalVolumeSide = matchSideNode.side;
            }
        }

        return new Box(minimalVolumeSide,minimalVolumeHeight);
    }

    public boolean checkBox(double side, double height) {
        SideNode sideNode = new SideNode(side);
        for (SideNode matchSideNode : this.sides.getGreaterOrEqualsThan(sideNode, this.sides.size())) {
            if (matchSideNode.heights.serachSuccessor(height) != null)
                return true;
        }

        return false;
    }
}
