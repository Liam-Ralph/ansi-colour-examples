class CSharpColorTest {

    public static void Main(string[] args){

        // Foreground/Background Selection
        bool colorBackground = true;
        string positionControl = "48";
        if(!colorBackground){
            positionControl = "38";
        }
        
        // First Sixteen Colors
        for(int i = 0; i < 16; i++){
            Console.Write(string.Format("\u001b[{0};5;{1}m{2} ", positionControl, i, i.ToString().PadLeft(4)));
        }
        Console.WriteLine("\u001b[0m");

        // Remaining Colors
        for(int i = 16; i < 256; i++){

            // Print the color, extra space if needed
            Console.Write(string.Format("\u001b[{0};5;{1}m{2} ", positionControl, i, i.ToString().PadLeft(4)));

            // New line every 36 colors, adjust for the first 16
            if((i - 15) % 36 == 0){
                Console.WriteLine("\u001b[0m");
            }

        }
        Console.WriteLine("\u001b[0m");
        
    }
}
