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
	listint_t *new_node;
	listint_t *current;
	/* Allocate memory for new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)  /* If memory allocation failed, return NULL */
		return (NULL);
	new_node->n = number;  /* Assign the data to the new node */
	new_node->next = NULL;  /* Initialize the next pointer of new node to NULL */
	/* If the list is empty or the new node should be inserted before the head node */
	if (*head == NULL || (*head)->n >= new_node->n)
	{
		new_node->next = *head;  /* Make the new node point to the current head node */
		*head = new_node;  /* Update the head pointer to point to the new node */
	}
	else
	{/* Find the node before the point of insertion */
		current = *head;
		while (current->next != NULL && current->next->n < new_node->n)
		{
			current = current->next;
		}/* Insert the new node */
		new_node->next = current->next;
		current->next = new_node;
	}
	return (new_node);  /* Return the new node */
}
