#include "lists.h"
/**
 * reverse_list - Reverses a linked list
 * @head: points to the first node in the list
 * Return: number of nodes
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (head != NULL)
	{
		next = head->next;
		head->next = prev;
		prev = head;
		head = next;
	}
	return (prev);
}
/**
 * is_palindrome - checks if the given linked list is a palindrome or not
 * @head: double points to the head of the linked list
 * Return: compared list
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *second_half, *prev_slow = *head;

	if (head == NULL || *head == NULL)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		slow = slow->next;
	}
	second_half = slow;
	prev_slow->next = NULL;
	second_half = reverse_list(second_half);
	while (*head != NULL && second_half != NULL)
	{
		if ((*head)->n != second_half->n)
			return (0);
		*head = (*head)->next;
		second_half = second_half->next;
	}
	return (1);
}
