#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

// I collaborated with Thomas Chiu

int convert(string input);

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    // Convert string to int
    printf("%i\n", convert(input));
}

int convert(string input)
{
    int length = strlen(input);
    if (length == 0)
    {
        return 0;
    }
    int last = strlen(input) - 1;
    int digit = (int) input[last] - '0';
    input[last] = '\0';
    return (convert(input) * 10) + digit;
}
