#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the pointer to the first node of list
 *
 * Return: 1 if given list is a palindrome. 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	int arr[1024];
	int i, n = 0;
	listint_t *trav;

	if (head == NULL)
		return (0);

	/* copy numbers from linked list to arr */
	trav = *head;
	while (trav)
	{
		arr[n++] = trav->n;
		trav = trav->next;
	}

	/* check if arr is a palindrome */
	for (i = 0; i < n / 2; i++)
	{
		if (arr[i] != arr[n - i - 1])
			return (0);
	}

	return (1);
}
