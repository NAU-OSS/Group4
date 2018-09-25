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
        printf("test true \n");
        return true;
    }
    else
    {
        //handle the error on input
        printf("test false \n");
        return false;    
    }
}    
    
bool characteristic(char numString[], int& c)
{
    //turn char into int
    int number = atoi(numString);
    printf("%i", number);
    return true;
}

bool mantissa(char numString[], int& numerator, int& denominator)
{
    return false;
}
