import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

import Game;


public class Part2 {
    public static void main(String[] args) {
        int sum = 0;
        int red = 12, green = 13, blue = 14;
        try {
            File myObj = new File("input.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                Game game = new Game(data);
                if (game.isPlayable(red, green, blue)) {
                    sum += game.getId();
                }
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

        System.out.println(sum);
    }
}