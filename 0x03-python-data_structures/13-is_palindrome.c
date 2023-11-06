#include "lists.h"

/**
 * reverse - Reverses a singly linked list
 *
 * @head_ref: A pointer to the head of the second half
 */
void reverse_list(listint_t **head_ref)
{
	listint_t *prev = NULL;
	listint_t *current = *head_ref;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head_ref = prev;
}

/**
 * compare - Compares each int of the two halves
 *
 * @first_half: pointer to the head of the list (first half)
 * @second_half: pointer to the reversed second half
 *
 * Return: 1 if they're identical, 0 if not
 */
int compare_elements(listint_t *first_half, listint_t *second_half)
{
	listint_t *temp1 = first_half;
	listint_t *temp2 = second_half;

	while (temp1 != NULL && temp2 != NULL)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
		{
			return (0);
		}
	}

	if (temp1 == NULL && temp2 == NULL)
	{
		return (1);
	}

	return (0);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 *
 * @head: Pointer to the head of the list
 *
 * Return: 1 if it's a palindrome, 0 if it's not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow;
	listint_t *second_half, *mid_point;
	int is_palindrome;

	slow = fast = prev_slow = *head;
	mid_point = NULL;
	is_palindrome = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			mid_point = slow;
			slow = slow->next;
		}

		second_half = slow;
		prev_slow->next = NULL;
		reverse_list(&second_half);
		is_palindrome = compare_elements(*head, second_half);

		if (mid_point != NULL)
		{
			prev_slow->next = mid_point;
			mid_point->next = second_half;
		}
		else
		{
			prev_slow->next = second_half;
		}
	}

	return (is_palindrome);
}
