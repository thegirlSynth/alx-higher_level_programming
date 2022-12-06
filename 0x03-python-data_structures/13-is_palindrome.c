#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: the singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int index = 0, count = 0, num, digit;
	listint_t *temp = *head, *checknode = *head;

	if (head == NULL || *head == NULL)
		return (1);

	while (checknode != NULL)
	{
		checknode = checknode->next;
		count++;
	}

	digit = count;
	while (index < count / 2)
	{
		checknode = *head;
		num = 1;
		while (num < digit)
		{
			checknode = checknode->next;
			num++;
		}

		if (checknode->n != temp->n)
			return (0);

		temp = temp->next;
		digit--;
		index++;
	}

	return (1);
}
