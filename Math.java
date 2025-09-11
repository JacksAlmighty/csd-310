// Jackson Webster
// Module 1 Assignment
// 9/10/2025
// This program shows the difference between multiplying with double vs int.

public class Math {
    public static void main(String[] args) {
        // The double output gives a more exact answer because it keeps the decimal numbers.
        double sum1 = 4.0 * (1.0 - 1.0 / 3.0 + 1.0 / 5.0 - 1.0 / 7.0 + 1.0 / 9.0 - 1.0 / 11.0 + 1.0 / 13.0);
        System.out.println(sum1);

        // The int output only keeps whole numbers and ignores decimals, so it is less exact.
        int sum2 = 4 * (1 - 1 / 3 + 1 / 5 - 1 / 7 + 1 / 9 - 1 / 11 + 1 / 13);
        System.out.println(sum2);

        // In this case, the double answer is better because it is more accurate.
        // But sometimes whole numbers (int) are fine, depending on what you need.
    }
}