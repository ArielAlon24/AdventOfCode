enum Color {
    RED,
    BLUE,
    GREEN,
}

class Game {
    private int id;
    private int red;
    private int blue;
    private int green;

    public Game(int id, int red, int blue, int green) {
        this.id = id;
        this.red = red;
        this.blue = blue;
        this.green = green;
    }

    public Game(String line) {
        String[] sections = line.split(":");
        this.id = Integer.valueOf(sections[0].split(" ")[1]);
        this.red = 0;
        this.blue = 0; 
        this.green = 0;
        for (String play: sections[1].trim().split("; ")) {
            for (String item: play.split(", ")) {
                int value = Integer.valueOf(item.split(" ")[0]);
                if (item.endsWith(Color.RED.name().toLowerCase())) {
                    this.red = Math.max(this.red, value);
                } else if (item.endsWith(Color.BLUE.name().toLowerCase())) {
                    this.blue = Math.max(this.blue, value);
                } else if (item.endsWith(Color.GREEN.name().toLowerCase())) {
                    this.green = Math.max(this.green, value);
                }
            }
        }
    }

    public boolean isPlayable(int red, int green, int blue) {
        return this.red <= red && this.green <= green && this.blue <= blue;
    }

    public int getId() {
        return this.id;
    }

    public int power() {
        return this.red * this.blue * this.green;
    }

    @Override
    public String toString() {
        return "Game " + this.id 
        + " | red: " + this.red 
        + " blue: " + this.blue 
        + " green: " + this.green;
    }
}
