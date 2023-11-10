#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - print bytes
 * @p: list to print info about
 *
 * No Return
**/
void print_python_bytes(PyObject *p)
{
	const char *str = PyBytes_AsString(p);
	Py_ssize_t size = PyBytes_Size(p), i;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", str);
    size++;
	printf("  first %zd bytes:", size > 10 ? 10 : size);

	for (i = 0; i < (size > 10 ? 10 : size); ++i)
	{
		printf(" %02x", (unsigned char)str[i]);
	}
	printf("\n");
}


/**
 * print_python_list - print info about P (list)
 * @p: list to print info about
 *
 * No Return
**/
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t s = PyList_Size(p), alloc = list->allocated, x;
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", alloc);
	for (x = 0; x < s; x++)
	{
		item = PyList_GET_ITEM(p, x);
			printf("Element %ld: ", x);
		if (PyBytes_Check(item))
		{
			print_python_bytes(item);
		}
		else if (PyFloat_Check(item))
		{
			printf("float\n");
		}
		else if (PyTuple_Check(item))
		{
			printf("tuple\n");
		}
		else if (PyList_Check(item))
		{
			print_python_list(item);
		}
		else if (PyLong_Check(item))
		{
			printf("int\n");
		}
		else if (PyUnicode_Check(item))
		{
			printf("str\n");
		}
	}
}