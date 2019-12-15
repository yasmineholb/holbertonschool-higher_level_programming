#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - fn
 *@head: param
 * Return: Always 0.
 */
int is_palindrome(listint_t **head)
{
unsigned int m;
listint_t *ch;
if (!head || !*head)
return (1);
ch = *head;
m = 1;
while (ch)
{
ch = ch->next;
m++;
}
return (0);
}
