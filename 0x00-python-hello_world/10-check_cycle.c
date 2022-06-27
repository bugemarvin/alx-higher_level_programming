#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - function to find loop.
 * @list: pointer to a  struct
 *
 * Return: Always 1 for success.
 *		0 for NULL or empty cycle/failuer.
 */

int check_cycle(listint_t *list)
{
	listint_t *sl;
	listint_t *fs;
		sl = list;
		fs = list;
	while (fs)
	{
		sl = sl->next;
		if (fs->next == NULL)
		{
			break;
		}
		fs = fs->next->next;
		if (sl == fs)
		{
			return (1);
		}
	}
	return (0);
}
