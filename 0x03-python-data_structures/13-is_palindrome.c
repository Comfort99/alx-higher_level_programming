#include "lists.h"
/**
 * count_nodes - Function to count the number of nodes in the linked list
 * @head: points to the first node in the list
 * Return: number of nodes
 */
int count_nodes(listint_t *head)
{
	int count = 0;

	while (head != NULL)
	{
		count++;
		head = head->next;
	}
	return (count);
}
/**
 * is_palindrome - checks if the given linked list is a palindrome or not
 * @head: double points to the head of the linked list
 * Return: compared list
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int *stack;
	int top = 0;

	if (head == NULL || *head == NULL)
        return (1);
	top = count_nodes(*head);
	stack = (int *)malloc(top * sizeof(int));if (stack == NULL)
	{
		fprintf(stderr, "Failed to allocate memory for stack\n");
		return (0);
	}
	while (temp != NULL)
	{
		stack[--top] = temp->n;
		temp = temp->next;
	}
	temp = *head;
	while (temp != NULL)
	{
		if (temp->n != stack[top++])
		{
			free(stack);
			return (0);
		}
		temp = temp->next;
	}
	free(stack);
	return (1);
}
