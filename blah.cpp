#include <stdio.h>
#include <stdbool.h>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cctype>

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
        printf("The characteristic is: %i\n", c);
        printf("The mantissa numerator is: %i\n", n);

    }
    // handles error on input
    else
    {
        int num_plus = 0;
        // Checks if there is a letter, cover imaginary numbers or random letter chars
        if(isalpha(number))
        {      
               printf("test false \n");
        }
        
        // Another solution
        // Checks if there is another symbol besides a digit or a + - symbol
        for (int i = 0; i < strlen(number); i = i + 1)
        { 
          if(number >= '0' || number <= '9' && number != '+' && number != '-')
          {
                printf("test false");
          }
        }
        return 0; 
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
    char mantissa_value_string[100];
    char mantissa_buffer[100];
    int currentIndex = 0;
    int offset = 0;

    while (numString[currentIndex] != '.')
    {
        mantissa_buffer[currentIndex] = numString[currentIndex];
        currentIndex++;
    }

    currentIndex++;
    offset = currentIndex;

    while (numString[currentIndex] != '\0')
    {
      mantissa_value_string[currentIndex - offset] = numString[currentIndex];
      currentIndex++;
    }

    numerator = atoi(mantissa_value_string);
    //printf("The mantissa numerator is: %i\n", numerator);

    return numerator;
}
