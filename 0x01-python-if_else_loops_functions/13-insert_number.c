#include "lists.h"

/**
 * insert_node - inserts a number into a singly linked list
 * @head: head of the linked list
 * @number: data in the new node
 * Return: address of the node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *first;

	first = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || first->n > new_node->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (first->next != NULL)
	{
		if ((first->next->n > new_node->n && first->n < new_node->n)
			|| new_node->n == first->n)
		{
			new_node->next = first->next;
			first->next = new_node;
			return (new_node);
		}
		first = first->next;
	}
	new_node->next = first->next;
	first->next = new_node;
	return (new_node);
}
