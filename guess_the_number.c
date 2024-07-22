# include <cs50.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int main (void)
{
    srand(time(NULL));
    int input_number = get_int("what's int ");
    int random_number = rand() % 100;
    while (true ){
        if (random_number == input_number){
            printf("good work\n");
            break;

        }
        else if(input_number > random_number){
            printf("ваше число больше \n");
            input_number = get_int("Ведите новое число ");
        }
        else{
            printf("Ваше число меньше \n");
            input_number = get_int("Ведите новое число ");
        }


    }
    return 0;
}
