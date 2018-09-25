#include <stdio.h>
#include <stdbool.h>
#include <iostream>

bool characteristic(char numString[], int& c);
bool mantissa(char numString[], int& numerator, int& denominator);

int main()
{
    char number[] = "123.456";
    int c, n, d;

    //if the conversion from C string to integers can take place
    if(characteristic(number, c) && mantissa(number, n, d))
    {
        //do some math with c, n, and d
        //printf("test true \n");
        printf("Characteristic: %i\n", c);
    }
    else
    {
        //handle the error on input
        //printf("test false \n");   
    }
}    
    
bool characteristic(char numString[], int& c)
{
    //turn char into int
    c = atoi(numString);
    //printf("%i", c);
    return c;
}

bool mantissa(char numString[], int& numerator, int& denominator)
{
    float fnumber = atof(numString);
    int inumber = atoi(numString);
    //printf("%f and %i\n", fnumber, inumber);
    //handle negative numbers correctly
    if (fnumber && inumber > 0)
    {
        float decimal = fnumber - inumber;
        //printf ("%.3f\n", decimal);
    }
    else
    {
        float decimal = -(fnumber) - -(inumber);
        //printf ("%f\n", decimal);
    }
    
    //where n is the number of places after the decimal,
    //take this decimal and multiply it by 10^n to get the numerator
    //and 10^n is the denominator
    
    return true;
}
