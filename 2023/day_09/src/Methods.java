import java.util.ArrayList;

public class Methods {
    public static ArrayList<Integer> generateList(String line) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        for (String number: line.split(" ")) {
            list.add(Integer.valueOf(number));
        }
        return list;
    }

    public static <T> T last(ArrayList<T> list) {
        return list.get(list.size() - 1);
    }

    public static int predictNext(ArrayList<Integer> list) {
        ArrayList<ArrayList<Integer>> differences = generateDifferences(list);

        int current = 0;
        for (int i = differences.size() - 2; i >= 0; i--) {
            current += last(differences.get(i));
        }

        return last(list) + current;
    }

    public static int predictPrevious(ArrayList<Integer> list) {
        ArrayList<ArrayList<Integer>> differences = generateDifferences(list);

        int current = 0;
        for (int i = differences.size() - 2; i >= 0; i--) {
            current = differences.get(i).get(0) - current;
        }

        return list.get(0) - current; 
    }

    public static boolean allZeros(ArrayList<Integer> list) {
        for (Integer num: list) {
            if (num != 0) return false;
        }
        return true;
    }

    public static ArrayList<ArrayList<Integer>> generateDifferences(ArrayList<Integer> list) {
        ArrayList<ArrayList<Integer>> differences = new ArrayList<ArrayList<Integer>>();
        differences.add(calculateDifference(list));

        while (!allZeros(last(differences))) {
            differences.add(calculateDifference(last(differences)));
        }
        return differences;
    }

    public static ArrayList<Integer> calculateDifference(ArrayList<Integer> list) {
        ArrayList<Integer> difference = new ArrayList<Integer>();
        for (int i = 0; i < list.size() - 1; i++) {
            difference.add(list.get(i + 1) - list.get(i));
        }
        return difference;
    }
}