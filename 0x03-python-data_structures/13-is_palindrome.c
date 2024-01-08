#include "lists.h"
/**
 * is_palindrome - check if a linked list is a palindrome
 * @head: first node
 * Return: 1 if success 0 if failed
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int values[2048], l_len = 0, cLoop, limit;

	if (head == NULL || *head == NULL)
		return (1);

	while (tmp != NULL)
	{
		values[l_len] = tmp->n;
		l_len++;
		tmp = tmp->next;
	}

	limit = l_len / 2;

	for (cLoop = 0; cLoop < limit; cLoop++)
		if (values[cLoop] != values[l_len - 1 - cLoop])
			return (0);

	return (1);
}