#include "lists.h"
/**
 * insert_node - inserts a node based  on the ordre
 * @head: the head of the list
 * @number: the number to insert
 * Return: the address of the node inserted or NULL if failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new_member = malloc(sizeof(listint_t));

	if (!new_member)
		return (NULL);
	new_member->n = number;
	if (!*head || new_member->n < (*head)->n)
	{
		new_member->next = *head;
		*head = new_member;
		return (new_member);
	}
	current = *head;
	while (current && current->next && current->next->n < number)	
		current = current->next;
	new_member->next = current->next;
	current->next = new_member;
	return (new_member);
}