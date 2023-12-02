import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;


public class Part2 {

    public static void main(String[] args) {
        int sum = 0;
        try {
            Scanner scanner = new Scanner(new File("input.txt"));
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                Game game = new Game(line);
                sum += game.power();
            }
            scanner.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        System.out.println(sum);
    }
}