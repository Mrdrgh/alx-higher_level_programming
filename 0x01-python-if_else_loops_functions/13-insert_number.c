#include "lists.h"
/**
 * insert_node - inserts a node based  on the ordre
 * @head: the head of the list
 * @number: the number to insert
 * Return: the address of the node inserted or NULL if failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *temp, *new_member = malloc(sizeof(listint_t));

	if (!*head || new_member)
		return (NULL);
	new_member->n = number;
	if (number < (*head)->n)
	{
		new_member->next = *head;
		head = &new_member;
		return (*head);
	}
	current = *head;
	temp = current;
	while (current)
	{
		temp = current;
		current = current->next;
		if (current->n > number)
		{
			temp->next = new_member;
			new_member->next = current;
			return (new_member);
		}
	}
	return (NULL);
}