#include "lists.h"

/**
 * check_cycle - checks if there a cycle in the linked list, we will use
 * the Floyd algo
 * @list: the list to check
 * Return: 0 if no cycle was found , 1 if yes
*/
int check_cycle(listint_t *list)
{
	listint_t *slow = NULL, *fast = NULL;

	if (!list)
	{
		return (0);
	}
	slow = fast = list;
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
