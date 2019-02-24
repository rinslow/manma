public class BoxStorage {

    private RedBlackTree<SideNode> sides;

    /**
     * The BoxStorage class represent the storage of the workshop.
     * We choose to use RedBlackTree to keep all the available sides.
     * Each node contain a RedBlackTree of the available heights.
     */
    BoxStorage(){
        this.sides = new RedBlackTree<>();
    }

    // @param: side and height
    // insert the box to the storage. If the side already exists we add the new height to his heights tree.
    //O(lgnm)
    public void insertBox(double side, double height){
        System.out.println("Insert new box - height: " + height + " ,side: " + side);

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

    // @param: side and height
    // remove the box from the storage.
    //O(lgnm)
    public void removeBox(double side, double height){
        System.out.println("Remove box - height: " + height + " ,side: " + side);

        SideNode sideNode = new SideNode(side);
        RedBlackNode<SideNode> existedSideNode = this.sides.search(sideNode);
        existedSideNode.key.heights.remove(existedSideNode.key.heights.search(height));
    }

    // @param: side and height
    // @return: the mach box
    //O(mlgn)
    public Box getBox(double side, double height){
        System.out.println("Get box - height: " + height + " ,side: " + side);

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

        System.out.println("Returned box - height: " + minimalVolumeHeight + " ,side: " + minimalVolumeSide);

        return new Box(minimalVolumeSide,minimalVolumeHeight);
    }

    // @param: side and height
    // @return: true if mach box exists, otherwise false
    //O(mlgn)
    public boolean checkBox(double side, double height) {
        System.out.println("Check if box exists - height: " + height + " ,side: " + side);

        SideNode sideNode = new SideNode(side);
        for (SideNode matchSideNode : this.sides.getGreaterOrEqualsThan(sideNode, this.sides.size())) {
            if (matchSideNode.heights.serachSuccessor(height) != null )
            {
                System.out.println("The box exists");
                return true;
            }
        }

        System.out.println("The box doesn't exist");
        return false;
    }
}
