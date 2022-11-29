#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: the list.
 * @number: the number to be inserted.
 * Return: the adress of the new node, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *checknode = *head, *temp = *head;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	
	newnode->n = number;

	if (*head == NULL || (*head)->n >= number)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}

	while (checknode != NULL)
	{
		if (checknode->n >= number)
		{
			break;
		}
		temp = checknode;
		checknode = checknode->next;
	}

	newnode->next = temp->next;
	temp->next = newnode;

	return (newnode);
}
