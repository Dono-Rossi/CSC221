1. CPUs are built on transistors which are essentially very small switches. 
   *  These switches are represented as either on or off, and make up your 
entire computer
   *   Binary numbers are used to represent these switches, 1 for on and 0 for
off
   *  Python is a high level language that allows it to manipulate binaru but 
many user friendly features make that hard to do
   *  Bitwise operations are used to combine or change binary numbers
        *   z = x AND y where bits in z are on only if corresponding bits in X  and Y are on
        *   z = x OR y where bits in z are on if corresponding bits in either x or y are on
        *   Z = x XOR (exclusive or) y where bits in z are on if corresponding bits in only one of x or y are on
        *   z = NOT x where bits in z are opposite of corresponding bits in x
        *   z = x << n where bits in z are shifted left by n postitions
        *   z = x >> n where bits in z are shifted right by n positions

Bitwise operators allow you to:

   * Create and manipulate flags
   * Access a portion of a number
   * Manipulate raw binary data

2. Transistors are small switches, when you apply power, it turn on. Take the 
power away, it turns off.

With different charges on a series of switches you can make a pattern.
   *  Switches that are on represent 1 and switches that are off represent 0
        * 101 represents 5
        * a is 97 in decimal, or 1100001 in binary
        * for colors, take a square, which would be a hex number. Ex: 0x7F8053, 7F is red, 80 is green and 53 is blue. the decimal number for 7F is 8355923, 
leading the binary to be 011111111000000001010011
!!!
   *  octal has a base of 8 and hex has a base of 16 and binary is base 2

   *  x(b)^n where x is a number, b is the base and x is the placement of the
digit starting from the right
   *  for example, 25 in binary is 00011001. the first 1 from the left would
be 1(2)^5
   * in hex, A is 10, B is 11, C is 12, D is 13, E is 14, and F is 15
!!!

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
