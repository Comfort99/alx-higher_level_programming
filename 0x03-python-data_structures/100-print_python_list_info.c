#include <Python.h>
#include <stdio.h>
#include <listobject.h>
#include <object.h>
/**
 * print_python_list_info - prints information about the Python list
 * @p: pointer as a argument
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid argument: not a Python list\n");
		return;
	}
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; ++i) 
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
