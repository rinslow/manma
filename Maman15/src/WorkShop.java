public class WorkShop {

    /**
     * Application entry point.
     *
     * @param args application command line arguments
     */
    public static void main(String[] args) {

        BoxStorage boxSorage = new BoxStorage();
        boxSorage.insertBox(10,10);
        Box box = boxSorage.getBox(10,10);
        System.out.print(box.volume);
    }

}
