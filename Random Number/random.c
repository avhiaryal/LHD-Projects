//Generating ten random nunbers
#include<stdio.h>
#include<stdlib.h>
int main()
{
for(int i = 0; i< 10; i++)
{
int *p; //declaring a integer typepointer
p = (int*)malloc(sizeof(int)); //dynamically allocating memory for it of it's size
printf("%d\n",p);
}
return 0;
}
