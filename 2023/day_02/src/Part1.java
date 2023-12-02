import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;


public class Part1 {

    public static void main(String[] args) {
        int sum = 0;
        int red = 12, green = 13, blue = 14;
        try {
            Scanner scanner = new Scanner(new File("input.txt"));
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                Game game = new Game(line);
                if (game.isPlayable(red, green, blue)) {
                    sum += game.getId();
                }
            }
            scanner.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        System.out.println(sum);
    }
}