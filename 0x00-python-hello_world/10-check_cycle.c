#include "lists.h"
#include <stdio.h>
/**/
int check_cycle(listint_t *list)
{
	listint_t *first = list;
    listint_t *second = list;

	if  (list == NULL || list->next == NULL)
		return (0);

    while (second != NULL && second->next != NULL)
	{
        first = first->next;
        second = second->next->next;

        if (first == second)
            return (1);
    }

    return (0);
}
