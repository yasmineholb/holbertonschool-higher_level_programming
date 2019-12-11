#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - fn
 * @head: param
 * @number: param
 * Return: listint
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *m, *ch;
m = *head;
ch = malloc(sizeof(listint_t));
if (ch == NULL)
return (NULL);
ch->n=number;
if (m == NULL || m->n >= number)
{
ch->next=m;
*head=ch;
return (ch);
}
while (m && m->next && m->next->n < number)
{
m = m->next;
}
ch->next = m->next;
m->next=ch;
return (ch);
}
