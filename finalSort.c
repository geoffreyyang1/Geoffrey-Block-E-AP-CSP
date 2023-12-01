#include <cs50.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

#define SIZE1 5000
#define SIZE2 10000
#define SIZE3 50000
int *readFile(string fileName, int size, int size2);  //pointer to return and int array
int linearSearch(int array[], int guess, int size);  //linear search
int binarySearch(int array[]);
char *bubbleSort(int array[]);
char *selectionSort(int array[]);
void printArray(int array[], int size);
int main(void)
void menu();
{
    string fileName=get_string("Enter File name ");
    FILE* file=(fopen(fileName, "r"));
    if(!file)
    {
    printf("\n Unable to open : %s ", fileName);
    return -1;
    }
    fclose(file);
    int *array;
    array=readFile(fileName, 10000, 5);   // call of the function
    int guess=get_int("give me a number in between ");
    int indx = linearSearch(array, guess, SIZE2); //call to linear
    if menu = get_int("4: Use Linear Search");
    {
      int indx = linearSearch(array, guess, SIZE2);
    }
    printf("the index is %i \n", indx);
    int *sorted=selectionSort(array);
    if menu = get_int("3: Use Selection Sort");
    {
      int *sorted=selectionSort(array);
    }
    printArray(sorted)
}
int *readFile(string fileName, int size, int size2 )
    {
    FILE* file=(fopen(fileName, "r"));

    char line[size2]; //how many characers per line
    char options[size][size2];//array to put all the numbers from the file

    int  static numbers[SIZE2];  // file to be returned

    for (int i=0; i <size; i++)
    {
        fscanf(file, "%s", options[i]);
        // printf("%s \n", options[i]);
        numbers[i]= atoi(options[i]);
    }
    fclose(file);
   return numbers;
}
int linearSearch(int array[],int guess,int size )
{
    for(int i=0; i < size; i++)
    {
        if (array[i]== guess)
        {
            return i;
        }
    }
    return -1;
}
int *selectionSort(int array[])
{
  int index=0;
  for (int i=0; i<SIZE2; i++)
  {
    int min = SIZE3+1;
    for (int j=i; j<SIZE2; j++);
    {
      if (array[j]<min)
      {
        min = array[j];
        index=j;
      }
    }
    int temp=array[i];
    array[i]<main;
    array[index]<temp;
  }
}
void printArray(int array[], int size);
{
  for (int i=0l i < size; i++)
  {
    printf(" %i \n", array[i]);
  }
}

void menu()
{
  printf("Menu");
  printf("Choices:");
  printf("1: Read a file");
  printf("2: Use Bubble Sort");
  printf("3: Use Selection Sort");
  printf("4: Use Linear Search");
  printf("5: Use Binary Search");
  printf("Exit \n");
}
