//package com.abc.solutions;

public class SpiralPrint {

    static void spiralPrint(int myArray[][]) {

        int numOfRows = myArray.length; // Number of rows
        int numOfCols = myArray[0].length; // Number of columns
        int iterations = numOfRows * numOfCols; // Number of iterations/elements

        // Current Row and Column Position, Initial Position is (0,0)
        int currRowPos = 0;
        int currColPos = 0;

        String direction = "right"; // Direction of the Spiral Path
        int loop = 0; // Number of times the spiral has looped

        // Loop until all the elements are printed
        for (int i = 0; i < iterations; i++) {

            System.out.print(myArray[currRowPos][currColPos] + " ");

            if (currColPos < numOfCols - loop - 1 && direction.equals("right")) {
                currColPos += 1;

                if (currColPos == numOfCols - 1 - loop) {
                    direction = "down";
                }

            } else if (currRowPos < numOfRows - loop - 1 && direction.equals("down")) {
                currRowPos += 1;

                if (currRowPos == numOfRows - loop - 1) {
                    direction = "left";
                }
            } else if (currColPos > 0 + loop && direction.equals("left")) {
                currColPos -= 1;

                if (currColPos == 0 + loop) {
                    direction = "up";
                }
            } else if (currRowPos > 0 + loop && direction.equals("up")) {
                currRowPos -= 1;
                if (currRowPos == loop + 1) {
                    direction = "right";
                    loop += 1;

                }
            }
        }
    }

    public static void main(String[] args) {
        
        int list[][] = {
            {1,2,3,4},
            {5,6,7,8},
            {9,10,11,12},
            {13,14,15,16}
        };

        spiralPrint(list);
    }

}