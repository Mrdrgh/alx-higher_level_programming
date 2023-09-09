#include "lists.h"
/**
 * reverse_list - reverses a list
 * @head: the head of the list
 * Return: the newly created list
*/
listint_t* reverse_list(listint_t *head)
{
    listint_t *previous, *next;

    previous = NULL;
    while (head)
    {
        next = head->next;
        head->next = previous;
        previous = head;
        head = next;
    }
    head = previous;
    return (head);
}
/**
 * is_palindrome - checks for if its a palindrom
 * @head: the head of the list
 * Return: 1 if it is a palindrom 0 if not
*/

int is_palindrome(listint_t **head)
{
    listint_t *new_list = NULL, *current, *current_2;

    current = *head;
    while (current)
    {
        add_nodeint_end(&new_list, current->n);
        current = current->next;
    }
    reverse_list(new_list);
    current = *head;
    current_2 = new_list;
    while (current && current_2)
    {
        if (current->n != current_2->n)
        {
            return (0);
        }
        current = current->next;
        current_2 = current_2->next;
    }
    return (1);
}