#include "lists.h"
/**
 * check_cycle - function
 * @list: parameter
 * Return: 0
 */
int check_cycle(listint_t *list)
{
listint_t *m, *n;
m = list;
n = list;
while (n && n->next)
{
m = m->next;
n = n->next->next;
if (n == m)
return (1);
}
return (0);
}
