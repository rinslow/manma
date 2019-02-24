public class Box implements Comparable<Box>{
    public double side;
    public double height;
    public double volume;

    Box(double side, double height){
        this.side = side;
        this.height = height;
        this.volume = side * side * height;
    }

    @Override
    public int compareTo(Box box) {
        return Double.compare(this.volume, box.volume);
    }
}
