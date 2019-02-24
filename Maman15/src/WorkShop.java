import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.stream.Stream;

public class WorkShop {

    /**
     * Application entry point.
     *
     * @param args application command line arguments
     */
    public static void main(String[] args) {
        String filePath = args[0];
        BoxStorage boxStorage = new BoxStorage();

        try (Stream<String> stream = Files.lines(Paths.get(filePath))) {
            stream.forEach(command -> runCommand(boxStorage, command));
        } catch (IOException e) {
            System.out.println("Failed to read file " + filePath);
            return;
        }
    }

    private static void runCommand(BoxStorage boxStorage, String command) {
        double side = (double) Character.digit(command.charAt(command.indexOf('(') + 1 ), 10);
        double heigth = (double) Character.digit(command.charAt(command.indexOf(')')- 1 ), 10);
        if (command.startsWith("INSERTBOX")){
            boxStorage.insertBox(side,heigth);
        }
        else if(command.startsWith("REMOVEBOX")){
            boxStorage.removeBox(side,heigth);
        }
        else if(command.startsWith("GETBOX")){
            boxStorage.getBox(side,heigth);
        }
        else if(command.startsWith("CHECKBOX")){
            boxStorage.checkBox(side,heigth);
        }

    }

}
