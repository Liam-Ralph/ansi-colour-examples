class JavaColorExample{
    public static void main(String[] args){

        // Foreground/Background Selection
        Boolean colorBackground = true;
        String positionControl = "48";
        if(!colorBackground){
            positionControl = "38";
        }
        
        // First Sixteen Colors
        for(int i = 0; i < 16; i++){
            System.out.print("\u001b[" + positionControl + ";5;" + i + "m " + i + " ");
            if(i < 10){
                System.out.print(" ");
            }
            if(i < 100){
                System.out.print(" ");
            }
        }
        System.out.println("\u001b[0m");

        // Remaining Colors
        for(int i = 16; i < 256; i++){

            // Print the color, extra space if needed
            System.out.print("\u001b[" + positionControl + ";5;" + i + "m " + i + " ");
            if(i < 100){
                System.out.print(" ");
            }

            // New line every 36 colors, adjust for the first 16
            if((i - 15) % 36 == 0){
                System.out.println("\u001b[0m");
            }

        }
        System.out.println("\u001b[0m");

    }
}