/*
 * @file <main.cpp, func1.cpp>
 *
 * @author [Morgan Lovato, Jasmine Mitchell, Gwen Morris]
 *
 * @brief <Break a character array into a characteristic and a mantissa. Stores in the reference parameters c, numerator and denominator>
 */

#include <stdio.h>
#include <stdbool.h>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include "func1.h"
#include "func1.cpp"


int main()
{
    // initialization of variables
    char number[] = "123.456";
    int c, n, d;

    //if the conversion from C string to integers can take place
    if (characteristic(number, c) && mantissa(number, n, d))
    {
        //do some math with c, n, and d
        //printf("test true \n");
        printf("The characteristic is: %i\n", c);
        printf("The mantissa numerator is: %i\n", n);

    }

    else
    {
      isValid(number);
      return 0;
    }
}
