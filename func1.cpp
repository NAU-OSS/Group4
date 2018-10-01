#include <stdio.h>
#include <stdbool.h>
#include <iostream>
#include <cstring>
#include <cstdlib>

bool characteristic(char num_string[], int& c)
{
  // turn char into int
  c = atoi(num_string);

  // printf("%i", c);
  return c;
}

bool mantissa(char num_string[], int& numerator, int& denominator)
{
  // declaration of variables
  char mantissa_value_string[100];
  char mantissa_buffer[100];
  int curr_index = 0;
  int offset = 0;

  while (num_string[curr_index] != '.')
  {
    mantissa_buffer[curr_index] = num_string[curr_index];
    curr_index++;
  }

  // increments index
  curr_index++;

  // resets offset
  offset = curr_index;

  // loops to end of char
  while (num_string[curr_index] != '\0')
  {
    mantissa_value_string[curr_index - offset] = num_string[curr_index];
    curr_index++;
  }

  numerator = atoi(mantissa_value_string);
  // printf("The mantissa numerator is: %i\n", numerator);

  return numerator;
}

void valid(char num_string[])
{
  // checks if there is another symbol besides a digit or a + - symbol
  for (int i = 0; i < strlen(num_string); i = i + 1)
  {
    // loops through number and checks if there are letter or symbols not including + or -
    if(num_string[i] >= '0' || num_string[i] <= '9')
    {
      if (num_string[i] != '-' && numStsring[i] != '+')
      {
        // declares false
        printf("test false");
      }
    }
  }
}
