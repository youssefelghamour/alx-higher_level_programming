#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked lis
 *
 * @head: pointer to pointer of first node of listint_t list
 * @number: the number to be added
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new, *prev;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	current = *head;
	prev = NULL;

	if (current == NULL || number < current->n)
	{
		new->next = current;
		*head = new;

		return (*head);
	}

	while (current != NULL && number > current->n)
	{
		prev = current;
		current = current->next;
	}

	prev->next = new;
	new->next = current;

	return (*head);
}
