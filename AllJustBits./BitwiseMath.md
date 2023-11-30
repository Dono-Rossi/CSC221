3. Bitwise operations effect one or more bits in a binary value.
Common bitwise operations are:
   *  AND
       * Combines two binary values into a result. Each bit in result is 1 iff bit is 1 in both values being combines
            * 0 & 0 = 0
            * 1 & 0 = 0
            * 0 & 1 = 0
            * 1 & 1 = 1
   *  OR(|)
       * Combines two binary value, if either of them is on, the value is on
          * 0 | 0 = 0
          * 1 | 0 = 1
          * 0 | 1 = 1
          * 1 | 1 = 1
   *  XOR(^)
      * Combines two binary numbers. Result is on is only one is on
          * 0 ^ 0 = 0
          * 0 ^ 1 = 1
          * 1 ^ 0 = 1
          * 1 ^ 1 = 0
   *  NOT(~)
      * Inverst each bit in a value
          * ~0 = 1
          * ~1 = 0
   *  Shifts (<<,>>)
      *Moves the bits left or right, includes and operator to indicate how many places to shift
          * 1_2 << 1_10 = 10_2
          * 1_2 << 2_10 = 100_2
          * 100_2 >> 1_10 = 10_2
          * shifting zeroes leaves it as a zero
          * when you shift left, zeroes are added on, when you shift right, the rightmost digits are chopped off.

4.

Binary values as strict powers of 2 can only represent positive number
Computers store numbers in memory

   *  A group of 8 bits is a byte
 
  One byte can contain from:

        * 0_10 to 255_10 or 0_2 to 1111 1111_2

To store numbers larger than 255 you need multiple bytes
   *  C language has 4 different integer types: char, short, int, and long and  allows for signed and unsigned values of integer types.

       * Unsigned char is a single byte ranging from 0 to 255
       * Signed char is a single byte in decimal ranging from -128 to 127
       * same 256 spots are used but mapped to different numbers

Sign magnitude is one strategy to represent negative numbers

    * Uses the left most bit to indicate positive or negative
    * Left most bit of one means a negative number
    * positive numbers range from:
         * 0000 0000_2 to 0111 1111_2 or 0 to 127 in decimal
    * negative numbers range from
         * 1000 0001_2 to 1111 1111_2

This gives two zeroes which is weird
Additionally you cannot just add the bits together

A solution to this was one's compliment
    * still uses the left-most bit to indicate positive or negative
    * Negative numbers are stored as their complement: their NOT value
    * positive values are the as sign magnitude
    * still has ambiguous 0
        * for example positive 2 = 0000 0010 and negative 2 = 1111 1101

Two's compliment
    * Removes the problem of ambiguous zero, simplifies binary arithmetic
    * Still uses the left most bit to indicate positive or negative
    * negative values are stored as their complement plus 1
    * Asymmetrical representation:
        * More negative numbers are availiable than positive ones
        *  8-bit twos complement ranges from: -128_10 to 127_10

Floating Point
Lossy representation of Non-Integers and composed of three parts:

    * Signed bit
    * exponent
    * mantissa

Similar to scientific notation except the decimal point is not fixed, it 
"floats"

 value = (-1)^sign * 2^(exponent - 127) * (Mantissa+1)

Single: 32 bits
   * Sign bit
   * 8 exponent bits
   * 23 mantissa bits
Double: 64 bits
   * sign bit
   * 11 exponent bits
   * 52 mantissa bits

Fixed point
    *  Stores digits to specified precision but the your CPU not optimized for
 these
