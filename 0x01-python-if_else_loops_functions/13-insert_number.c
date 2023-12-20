#include "lists.h"

/**
 * insert_node - adds a number into a sorted singly-linked list.
 * @head: Pointer to head of the list.
 * @number: The number to add
 * Return: If the function fails - NULL or 0.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *insert = *head;
	listint_t *update;

	update = malloc(sizeof(listint_t));

	if (!update)
		return (NULL);
	update->n = number;

	if (insert == NULL || insert->n >= number)
	{
		update->next = insert;
		*head = update;
		return (update);
	}

	while (insert && insert->next && insert->next->n < number)
		insert = insert->next;
	update->next = insert->next;
	insert->next = update;

	return (update);
}
