#include "lists.h"
/**
 * insert_node - inserts a new node at the beginning of a linked list
 * @head: pointer to the head of the list
 * @number: value to be inserted in the new node
 *
 * Return: address of the new node, or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	/* Create a new node */
	listint_t *new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{/* Allocation failed */
		return (NULL);
	}
	/* Set the values for the new node */
	new_node->n = number;
	new_node->next = *head;
	/* Update the head to point to the new node */
	*head = new_node;
	/* Return the address of the new node */
	return (new_node);
}
