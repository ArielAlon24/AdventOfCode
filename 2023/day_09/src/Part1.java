import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;

public class Part1 {

    public static void main(String[] args) {
        try {
            Scanner scanner = new Scanner(new File("input.txt"));
            int sum = 0;
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                sum += Methods.predictNext(Methods.generateList(line));
            }
            System.out.println(sum);
            scanner.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}